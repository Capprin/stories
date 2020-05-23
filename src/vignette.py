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
      # TODO: add checks for different types of inputs/outputs as objects
      if self.TITLE_NAME in contents:
        self.title = contents[self.TITLE_NAME]
      else:
        raise Exception("the '" + TITLE_NAME + "' property is missing in " + fileName)

      if self.INPUTS_NAME in contents:
        self.inputs = contents[self.INPUTS_NAME]
      else:
        raise Exception("the '" + INPUTS_NAME + "' property is missing in " + fileName)

      if self.OUTPUTS_NAME in contents:
        self.outputs = contents[self.OUTPUTS_NAME]
      else:
        raise Exception("the '" + OUTPUTS_NAME + "' property is missing in " + fileName)

      # additional constraints
      if self.inputs is None and self.outputs is None:
        raise Exception("either '" + INPUTS_NAME + "' or '" + OUTPUTS_NAME + "' must have nonzero length in " + fileName)

  def inputLength():
    return self.__length(self.inputs)

  def outputLength():
    return self.__length(self.outputs)

  def __length(localDict):
    if localDict is None:
      return 0
    return len(localDict)