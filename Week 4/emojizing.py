import emoji

def main():
    text = input()
    print(emoji.emojize(text, language = "alias"))

main()
