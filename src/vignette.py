import yaml

# encapsulating class for vignette .yml files
class vignette:

  def __init__(self):
    # required of vignettes
    self.title = None
    self.setting = None
    self.inputs = []
    self.outputs = []

  def load(self, fileName):
    # load file as yaml
    # parse into requesite params
    # do necessary checking to ensure yaml and contents are acceptable (separate method?)
