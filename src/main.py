from vignette import Vignette

# load vignettes
VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\"

tmp = Vignette()
tmp.load(VIGNETTE_DIR + "1_middle.yml")
print(tmp.toString())