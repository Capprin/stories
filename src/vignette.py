import yaml

# encapsulating class for vignette .yml files
class Vignette:

  TITLE_NAME = "title"
  INPUTS_NAME = "inputs"
  OUTPUTS_NAME = "outputs"

  CHARACTER_NAME = "character"
  SETTING_NAME = "setting"
  THING_NAME = "thing"

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
      
      poss = [self.CHARACTER_NAME, self.SETTING_NAME, self.THING_NAME]
      if not provInputs is None:
        for i in provInputs:
          if not i in poss:
            raise Exception("input \"" + i + "\" is not one of [" + ", ".join(poss) + "].")
        self.inputs = provInputs
      if not provOutputs is None:
        for o in provOutputs:
          if not o in poss:
            raise Exception("output \"" + i + "\" is not one of [" + ", ".join(poss) + "].")
        self.outputs = provOutputs

  def inputsHash(self):
    return self.hash(self.inputs)

  def outputsHash(self):
    return self.hash(self.outputs)

  def hash(self, localDict):
    occurrences = self.__getOccurrences(localDict)
    return "c{}s{}t{}".format(occurrences[self.CHARACTER_NAME], occurrences[self.SETTING_NAME], occurrences[self.THING_NAME])

  def __getOccurrences(self, localDict):
    # count occurrences of ea. type in dict
    occurrences = {self.CHARACTER_NAME:0, self.SETTING_NAME:0, self.THING_NAME:0}
    for item in localDict:
      if item in occurrences:
        occurrences[item] += 1
    return occurrences

  def inputLength(self):
    return self.__length(self.inputs)

  def outputLength(self):
    return self.__length(self.outputs)

  def __length(self, localDict):
    if localDict is None:
      return 0
    return len(localDict)

  def toString(self):
    return "Vignette: \"" + self.title + "\"; inputs: {" + ", ".join(self.inputs) + "}; outputs: {" + ", ".join(self.outputs) + "}."