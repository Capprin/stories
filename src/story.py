from neo4j import GraphDatabase

class Story:

  DB_HOST_NAME = "db_host"
  DB_PORT_NAME = "db_port"
  DB_USER_NAME = "db_user"
  DB_PASS_NAME = "db_pass"

  def __init__(self, config):
    self.config = config
    # driver handles connection to db
    # can't do encrypted conn in Neo4j>4.0
    self._driver = GraphDatabase.driver("bolt://" + config[self.DB_HOST_NAME] + ":" + str(config[self.DB_PORT_NAME]),
                                        auth=(config[self.DB_USER_NAME], config[self.DB_PASS_NAME]),
                                        encrypted=False)
    # clear db
    self.clear()
    self.vignettes = []

  def push(self, vignette):
    if not vignette.isValid():
      raise Exception("vignette " + vignette + " is invalid")
    # setup
    with self._driver.session() as session:
      queryItems = []
      if vignette.inputs and vignette.actions:
        # add both inputs, actions if existent
        queryItems = vignette.inputs + vignette.actions
      elif vignette.actions:
        # add actions if only existent
        queryItems = vignette.actions
      else:
        # just push if only inputs
        self.vignettes.append(vignette)
        return
      query = '\n'.join(queryItems)
      tx = session.begin_transaction()
      try:
        tx.run(query)
      except:
        tx.rollback()
        raise Exception("failed to push vignette " + str(vignette))
      tx.commit()
    self.vignettes.append(vignette)

  def canPush(self, vignette):
    if not vignette.inputs:
      return True
    if not vignette.isValid():
      return False
    # run vignette input queries
    with self._driver.session() as session:
      try:
        # do dryrun of inputs with return
        tx = session.begin_transaction()
        queryItems = vignette.inputs + ["RETURN *"]
        query = '\n'.join(queryItems)
        tx.run(query)
        tx.rollback()
      except Exception as e:
        # generic failure, quantize later (maybe wrap with exec fn?)
        return False
    return True

  def clear(self):
    self.vignettes = []
    # rm all nodes
    with self._driver.session() as session:
      session.run("MATCH (n) DETACH DELETE n")