import yaml

# encapsulating class for vignette .yml files
class Vignette:

  TITLE_NAME = "title"
  INPUTS_NAME = "inputs"
  OUTPUTS_NAME = "outputs"

  def __init__(self):
    # required of vignettes
    self.title = None
    self.inputs = {}
    self.outputs = {}

  def load(self, fileName):
    # load file as yaml
    with open(fileName) as file:
      contents = yaml.load(file, Loader=yaml.SafeLoader)
      # TODO: handle case where file not found

      # parse into params, checking for requesite vars
      provInputs = {}
      provOutputs = {}
      if self.TITLE_NAME in contents:
        self.title = contents[self.TITLE_NAME]
      else:
        raise Exception("the '" + TITLE_NAME + "' property is missing in " + fileName)
      if self.INPUTS_NAME in contents:
        provInputs = contents[self.INPUTS_NAME]
      else:
        raise Exception("the '" + INPUTS_NAME + "' property is missing in " + fileName)
      if self.OUTPUTS_NAME in contents:
        provOutputs = contents[self.OUTPUTS_NAME]
      else:
        raise Exception("the '" + OUTPUTS_NAME + "' property is missing in " + fileName)

      # additional constraints
      if self.inputs is None and self.outputs is None:
        raise Exception("either '" + INPUTS_NAME + "' or '" + OUTPUTS_NAME + "' must have nonzero length in " + fileName)
      
      if not provInputs is None:
        self.__addActors(self.inputs, provInputs)
      if not provOutputs is None:
        self.__addActors(self.outputs, provOutputs)

  def __addActors(self, localDict, actorDict):
    for a in actorDict:
      k = list(a)[0]
      v = a[k]
      if not k in localDict:
        localDict[k] = v
      else:
        localDict[k] += v

  def hash(self, localDict):
    if localDict is None or len(localDict) == 0:
      return ""
    keysAlpha = list(localDict)
    keysAlpha.sort()
    outHash = ""
    for key in keysAlpha:
      outHash += key[0]
      outHash += str(localDict[key])
    return outHash

  def __str__(self):
    return "vignette: \"" + self.title + "\", with input hash \"" + self.hash(self.inputs) + "\", and output hash \"" + self.hash(self.outputs) + "\""

  def __repr__(self):
    return str(self)