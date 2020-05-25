import os, random
from vignette import Vignette
from story import Story

# responsible for compiling many vignettes into stories
class Author:

  def __init__(self):
    # initialize vignette dicts (hash -> list)
    self.startsList = []
    self.inputsDict = {}
    self.outputsDict = {}
    self.endsDict = {}

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
    if len(tmp.inputs) == 0:
      # starts have their own storage
      self.startsList.append(tmp)
    elif len(tmp.outputs) == 0:
      # so do ends
      self.__addVignette(self.endsDict, tmp.hash(tmp.inputs), tmp)
    else:
      self.__addVignette(self.inputsDict, tmp.hash(tmp.inputs), tmp)
      self.__addVignette(self.outputsDict, tmp.hash(tmp.outputs), tmp)
  
  def __addVignette(self, localDict, vHash, vignette):
    if not vHash in localDict:
      localDict[vHash] = [vignette]
    else:
      localDict[vHash].append(vignette)

  def compile(self, numVignettes):
    story = Story()

    # pick beginning (randomly, for now)
    if len(self.startsList) == 0:
      raise Exception("cannot solve story; there are no starting vignettes.")
    story.push(random.choice(self.startsList))

    # add body vignettes
    for i in range(numVignettes-2):
      # use possible story inputs as condition
      possKeys = story.possActors()
      possVignettes = []
      for key in possKeys:
        if key in self.inputsDict:
          possVignettes.extend(self.inputsDict[key])
      if len(possVignettes) == 0:
        # no matches
        raise Exception("cannot solve story; no vignettes can use current state. Current state: " + str(story.stateProgression[-1]))
      story.push(random.choice(possVignettes))

    # find an ending (redundant, but WIP for now)
    possKeys = story.possActors()
    possVignettes = []
    for key in possKeys:
      if key in self.endsDict:
        possVignettes.extend(self.endsDict[key])
    if len(possVignettes) == 0:
        # no matches
        raise Exception("cannot solve story; no end vignettes can use current state. Current state: " + str(story.stateProgression[-1]))
    story.push(random.choice(possVignettes))

    return story