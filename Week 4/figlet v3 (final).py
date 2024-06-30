from pyfiglet import Figlet
import random
import sys


def main():
    if len(sys.argv) == 1:
        figlet = Figlet()
        input_text = input("Input: ")
        f = Figlet.getFonts(figlet)
        font = random.choice(f)
        Figlet.setFont(figlet, font=font)
        print(figlet.renderText(input_text))
    else:
        if is_invalid_argument():
            sys.exit("Invalid usage")
        else:
            figlet1 = Figlet()
            input_text = input("Input: ")
            font1 = sys.argv[2]
            Figlet.setFont(figlet1, font=font1)
            print(figlet1.renderText(input_text))


def is_invalid_argument():
    if len(sys.argv) != 3 and len(sys.argv) != 1:
        return True
    else:
        if "-f" != sys.argv[1] and "--font" != sys.argv[1]:
            return True
        else:
            figlet1 = Figlet()
            if sys.argv[2] not in Figlet.getFonts(figlet1):
                return True
            else:
                return False


main()
