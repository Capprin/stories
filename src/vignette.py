import yaml

# encapsulating class for vignette .yml files
class Vignette:

  TITLE_NAME = "title"
  INPUTS_NAME = "inputs"
  ACTIONS_NAME = "actions"
  BAD_OPS = ["CREATE", "DELETE", "SET", "REMOVE"]

  def __init__(self):
    # required of vignettes
    # inputs, actions are lists of queries
    self.title = None
    self.inputs = []
    self.actions = []

  def load(self, fileName):
    # load file as yaml
    with open(fileName) as file:
      contents = yaml.load(file, Loader=yaml.SafeLoader) #doesn't flag problems

      # parse into params, checking for requesite vars
      if self.TITLE_NAME in contents:
        self.title = contents[self.TITLE_NAME]
      else:
        raise Exception("the '" + self.TITLE_NAME + "' property is missing in " + fileName)
      if self.INPUTS_NAME in contents:
        self.inputs = contents[self.INPUTS_NAME]
      else:
        raise Exception("the '" + self.INPUTS_NAME + "' property is missing in " + fileName)
      if self.ACTIONS_NAME in contents:
        self.actions = contents[self.ACTIONS_NAME]
      else:
        raise Exception("the '" + self.ACTIONS + "' property is missing in " + fileName)

  def isValid(self):
    if not self.inputs and not self.actions:
      # must have one/the other
      return False
    if not self.inputs or not self.actions:
      # start/end vignettes are okay
      return True
    for query in self.inputs:
      if any(operation in query for operation in self.BAD_OPS):
        # ensure none of the input operations modify graph
        return False
    return True

  def __str__(self):
    return "(vignette: \"" + self.title + ")"

  def __repr__(self):
    return str(self)