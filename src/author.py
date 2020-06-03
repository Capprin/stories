import os, random
from vignette import Vignette
from story import Story

# responsible for compiling many vignettes into stories
class Author:

  def __init__(self, config):
    self.config = config
    # initialize vignette storage
    self.startsList = []
    self.mainsList = []
    self.endsList = []

  def loadAll(self, directory):
    # find all .yml files in supplied directory
    for file in os.listdir(directory):
      if file.endswith(".yml"):
        self.loadOne(directory + file)

  def loadOne(self, path):
    tmp = Vignette()
    try:
      tmp.load(path)
    except Exception as e:
      # don't want to load if there's a problem
      print("failed to load vignette at " + path + ". Reason: " + str(e))
      return
    # add to storage
    if not tmp.inputs:
      # starts have their own storage
      self.startsList.append(tmp)
    elif not tmp.actions:
      # so do ends
      self.endsList.append(tmp)
    else:
      self.mainsList.append(tmp)

  def compile(self, numVignettes):
    story = Story(self.config)

    # pick beginning (randomly, for now)
    if len(self.startsList) == 0:
      raise Exception("cannot solve story; there are no starting vignettes.")
    story.push(random.choice(self.startsList))

    # add body vignettes
    for i in range(numVignettes-2):
      possVignettes = []
      for vignette in self.mainsList:
        if story.canPush(vignette):
          possVignettes.append(vignette)
      if len(possVignettes) == 0:
        # no matches
        raise Exception("cannot solve story; no vignettes can use current state.")
      story.push(random.choice(possVignettes))

    # find an ending (redundant, but WIP for now)
    possVignettes = []
    for vignette in self.endsList:
      if story.canPush(vignette):
        possVignettes.append(vignette)
    if len(possVignettes) == 0:
        # no matches
        raise Exception("cannot solve story; no end vignettes can use current state. Current state: " + str(story.stateProgression[-1]))
    story.push(random.choice(possVignettes))

    return story