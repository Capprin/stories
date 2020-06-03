from author import Author
import yaml

CONFIG_PATH = "C:\\Users\cappr\Projects\Stories\conf\config.yml"
VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\"

# load vignettes
config = None
with open(CONFIG_PATH) as cFile:
  config = yaml.load(cFile, Loader=yaml.SafeLoader)
storyBuilder = Author(config)
storyBuilder.loadAll(VIGNETTE_DIR)

# generate stories
while True:
  i = input("Enter the story length to create, or q to quit: ")
  if i == 'q':
    break
  # generate story
  try:
    story = storyBuilder.compile(int(i))
  except Exception as e:
    print("Story writing failed. Reason: " + str(e))
  else:
    print("Compiled story:")
    for v in story.vignettes:
      print("  " + str(v))