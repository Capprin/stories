import itertools

# responsible for storage of the "story"
# contains:
#   - representation of story state over time (characters, items, etc)
#       - for now, dict
#       - eventually graph rep. (for associations)
#   - actual list of vignettes

class Story:

  def __init__(self):
    # state progression over time
    # list contains dicts of actor counts at every event step
    self.stateProgression = []
    self.vignettes = []
    self.step = 0

  def push(self, vignette):
    # check if vignette can be added (confirm existence & sufficience)
    if not self.canPush(vignette):
      raise Exception("cannot push " + str(vignette) + "; insufficient state")

    self.vignettes.append(vignette)
    self.stateProgression.append({})
    # handle inputs
    if len(vignette.inputs) != 0:
      self.stateProgression[self.step] = self.stateProgression[self.step-1] #replicate old state
      for k, v in vignette.inputs.items():
        self.stateProgression[self.step][k] -= v
    # handle outputs
    if len(vignette.outputs) != 0:
      for k,v in vignette.outputs.items():
        if k in self.stateProgression[self.step]:
          self.stateProgression[self.step][k] += v
        else:
          self.stateProgression[self.step][k] = v
    self.step += 1

  def canPush(self, vignette):
    if len(vignette.inputs) == 0:
      return True
    # for now, check if we have enough of each actor to add this vignette
    currentState = self.stateProgression[-1]
    for k, v in vignette.inputs.items():
      if not k in currentState or currentState[k] < v:
        return False
    return True

  def possActors(self):
    # get all combinations of state (could get really slow)
    actorQuants = []
    # iterate over keys
    for k, v in self.stateProgression[-1].items():
      possNums = [""]
      firstChar = k[0]
      # iterate over values
      for i in range(v):
        possNums.append(firstChar + str(i+1))
      actorQuants.append(possNums)
    # cartesian product
    tuples = itertools.product(*actorQuants)
    out = []
    for t in tuples:
      out.append(''.join(t))
    return out

  def clear(self):
    self.__init__()