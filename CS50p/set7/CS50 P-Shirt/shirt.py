from PIL import Image, ImageOps
import sys

l = len(sys.argv)
if l > 3 or l < 3:
    sys.exit("Invalid arguments.")

input,output = sys.argv[1],sys.argv[2]
types = (".jpg", ".jpeg", ".png")

if not input.endswith(types):
    sys.exit("Invalid arguments.")
if not output.endswith(types):
    sys.exit("Invalid arguments.")
if input.split(".")[1] != output.split(".")[1]:
    sys.exit("Invalid arguments.")


shirt = Image.open("shirt.png")
try:
    with Image.open(input) as image:
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, shirt)
        image.save(output)
except FileNotFoundError:
    sys.exit("File does not exist.")
