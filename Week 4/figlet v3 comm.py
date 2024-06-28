# import necessary packages
from pyfiglet import Figlet
import random
import sys


def main():
    # if sys.argv has only 2 arguments then proceed with randomized font
    if len(sys.argv) == 1:
        # activate figlet
        figlet = Figlet()
        # ask for user text input
        input_text = input("Input: ")
        # get all figlet fonts in a standard list, assign it to variable "f"
        f = Figlet.getFonts(figlet)
        # randomly choose 1 font from list "f"
        font = random.choice(f)
        # set the figlet font
        Figlet.setFont(figlet, font=font)
        # render the inputted text using randomzied font
        print(figlet.renderText(input_text))

    # if else, proceed with user selected font
    else:
        # activate figlet
        figlet1 = Figlet()
        # check if argument is invalid
        # (arg len =/= 3, sys.argv[1] not in correct format,
        # and sys.argv[2] not in font list)
        if is_invalid_argument():
            sys.exit("Invalid usage")
        # if argument is valid then proceed with user inputted font
        else:
            # ask for user text input
            input_text = input("Input: ")
            # assign user inputted font as "font1"
            font1 = sys.argv[2]
            # set the figlet font
            Figlet.setFont(figlet1, font=font1)
            # render the inputted text with user specifiied font
            print(figlet1.renderText(input_text))


def is_invalid_argument():
    # check if user inputted correct no. of arguments
    if len(sys.argv) != 3 and len(sys.argv) != 1:
        return True
    else:
        # check if user inputter correct format for font inputting
        if "-f" != sys.argv[1] and "--font" != sys.argv[1]:
            return True
        else:
            # check if user inputted font is in figlet font list
            figlet1 = Figlet()
            if sys.argv[2] not in Figlet.getFonts(figlet1):
                return True
            else:
                return False


main()
