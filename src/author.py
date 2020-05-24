import os, random
from vignette import Vignette

# responsible for compiling many vignettes into stories
class Author:

  def __init__(self):
    # initialize vignette dicts (hash -> list)
    self.startDict = {}
    self.inputsDict = {}
    self.outputsDict = {}

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
    if tmp.inputLength() == 0:
      # starts have their own storage
      self.__addVignette(self.startDict, tmp, tmp.outputsHash())
    else:
      self.__addVignette(self.inputsDict, tmp, tmp.inputsHash())
      self.__addVignette(self.outputsDict, tmp, tmp.outputsHash())
  
  def __addVignette(self, localDict, vignette, vHash):
    if not vHash in localDict:
      localDict[vHash] = [vignette]
    else:
      localDict[vHash].append(vignette)

  def compile(self, numVignettes):
    story = []
    # pick end (randomly, for now)
    possEndings = self.outputsDict["c0s0t0"]
    story.append(random.choice(possEndings))

    # add body vignettes
    for i in range(numVignettes-2):
      # use inputs for last item as needed outputs for next item
      needOutputHash = story[i].inputsHash()
      if not needOutputHash in self.outputsDict:
        raise Exception("cannot solve story; necessary output hash \"" + needOutputHash + "\" does not exist.")
      possVignettes = self.outputsDict[needOutputHash]
      story.append(random.choice(possVignettes))

    # add beginning
    needOutputHash = story[-1].inputsHash()
    if not needOutputHash in self.startDict:
      raise Exception("cannot solve story; initial vignette with output hash \"" + needOutputHash + "\" does not exist.")
    possBeginnings = self.startDict[needOutputHash]
    story.append(random.choice(possBeginnings))

    # flip for chronology
    return reversed(story)