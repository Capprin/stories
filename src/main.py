from author import Author

# load vignettes
VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\"
storyBuilder = Author()
storyBuilder.loadAll(VIGNETTE_DIR)

# show loaded vignettes
print("Loaded Vignettes:")
for h in storyBuilder.inputsDict:
  print(h)
  for v in storyBuilder.inputsDict[h]:
    print(" " + v.toString())
print("")

# generate story
try:
  story = storyBuilder.compile(3)
except Exception as e:
  print("Story writing failed. Reason: " + str(e))
else:
  print("Compiled story:")
  for v in story:
    print(v.toString())