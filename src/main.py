from author import Author

# load vignettes
VIGNETTE_DIR = "C:\\Users\cappr\Projects\Stories\etc\\"
storyBuilder = Author()
storyBuilder.loadAll(VIGNETTE_DIR)

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