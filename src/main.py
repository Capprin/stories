from author import Author

VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\"
mom = Author()
mom.loadAll(VIGNETTE_DIR)

for h in mom.inputsDict:
  print(h)
  for v in mom.inputsDict[h]:
    print(" " + v.toString())