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
    elif len(sys.argv) == 3:
        figlet1 = Figlet()
        if is_invalid_argument():
            sys.exit("Invalid usage")
        else:
            input_text = input("Input: ")
            font1 = sys.argv[2]
            Figlet.setFont(figlet1, font=font1)
            print(figlet1.renderText(input_text))
    else:
        sys.exit("Invalid usage")

def is_invalid_argument():
    figlet1 = Figlet()
    if "-f" != sys.argv[1] and "--font" != sys.argv[1]:
        return True
    else:
        if sys.argv[2] not in Figlet.getFonts(figlet1):
            return True
        else:
            return False

main()
