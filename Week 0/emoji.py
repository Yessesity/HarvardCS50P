def main ():
    text = input()
    print(emoji(text))

def emoji(face):
    return face.replace(":)", "🙂").replace(":(", "🙁")

main()