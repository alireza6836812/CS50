from pyfiglet import Figlet
import random
import sys

fonts = Figlet()
fonts = fonts.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid arguments.")
else:
    sys.exit("Invalid number of arguments.")

my_input = input("Input: ")
output = Figlet(font=font).renderText(my_input)
print("Output:\n", output)
