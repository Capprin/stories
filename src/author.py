import os
from vignette import Vignette

# responsible for compiling many vignettes into stories
class Author:

  def __init__(self):
    # initialize vignette dicts (hash -> list)
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
    self.__addVignette(self.inputsDict, tmp, tmp.inputsHash())
    self.__addVignette(self.outputsDict, tmp, tmp.outputsHash())
  
  def __addVignette(self, localDict, vignette, vHash):
    if not vHash in localDict:
      localDict[vHash] = [vignette]
    else:
      localDict[vHash].append(vignette)

  def compile(self, numVignettes):
    # pick end (randomly, for now)
    # for numVignettes:
    #   search for vignettes with correct outputs
    #     (maybe take advantage of another type of data struct)
    #     think about different types of inputs/outputs too
    #   add random one to end
    # on end, pick start at random
    return