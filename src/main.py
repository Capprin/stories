import os
import sys
import json
from vignette import Vignette

VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\"

# load .yml files
for file in os.listdir(VIGNETTE_DIR):
  if (file.endswith(".yml")):
    print("Loading " + file)
    tmp = Vignette()
    tmp.load(VIGNETTE_DIR + file)
    print("Vignette \"" + tmp.title + "\" has inputs " + json.dumps(tmp.inputs) + ", and outputs " + json.dumps(tmp.outputs) + ".")
