## Basic tests of constituent classes and behavior
print("-------------\nrunning tests\n-------------\n")

VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\test\\"
CONF_PATH = "C:\\Users\cappr\Projects\Stories\conf\config.yml"

## vignette.py
print("testing vignette.py")
from vignette import Vignette
vign1 = Vignette()
print("  loading 0_start.yml")
vign1.load(VIGNETTE_DIR + "0_start.yml")
print("  confirming contents")
if not vign1.title == "start test vignette":
  raise Exception("vignette title incorrectly loaded")
if not vign1.actions[0] == "CREATE (:Character {name:'Protagonist', isProtagonist:true}) -[:OWNS]-> (:Thing {name:'sword'})":
  raise Exception("vignette contents incorrectly loaded")
if not vign1.isValid():
  raise Exception('vignette invalid')
print("vignette.py succeeded\n")

## story.py
print("testing story.py")
# read config
import yaml
config = None
with open(CONF_PATH) as cFile:
  config = yaml.load(cFile, Loader=yaml.SafeLoader)
from story import Story
print("  connecting to db")
story1 = Story(config) #fails if can't connect
print("  pushing start vignette")
if not story1.canPush(vign1):
  raise Exception("cannot push start vignette")
story1.push(vign1) #also should always succeed (just CREATE)
vign2 = Vignette()
vign2.load(VIGNETTE_DIR + "1_middle.yml")
print("  pushing middle vignette")
if not story1.canPush(vign2):
  raise Exception("cannot push middle vignette")
story1.push(vign2)
vign3 = Vignette()
vign3.load(VIGNETTE_DIR + "2_end.yml")
print("  pushing end vignette")
if not story1.canPush(vign3):
  raise Exception("cannot push end vignette")
story1.push(vign3)
print("story.py succeeded\n")

## author.py
print("testing author.py")
from author import Author
author1 = Author(config)
print("  loading vignettes")
author1.loadAll(VIGNETTE_DIR)
print("  creating story")
story2 = author1.compile(3)
print("  verifying story")
if not str(story2.vignettes) == str(story1.vignettes):
  raise Exception("somehow produced the wrong story")
print("author.py succeeded\n")