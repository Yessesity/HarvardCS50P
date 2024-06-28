from pyfiglet import Figlet
import random
import sys

def main():
    if len(sys.argv) == 1:
        figlet = Figlet()
        f = Figlet.getFonts(figlet)
        font = random.choice(f)
        Figlet.setFont(figlet, font=font)
        print(figlet.renderText("Hi"))
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" or sys.argv[1] != "--f":
            pass
        else:
            figlet1 = Figlet()
            if sys.argv[2] not in Figlet.getFonts(figlet1):
                pass
            else:
                font1 = sys.argv[2]
                Figlet.setFont(figlet1, font=font1)
                print(figlet1.renderText("Hi"))
    else:
        print("Invalid usage")

main()
