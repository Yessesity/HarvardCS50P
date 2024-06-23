import re

def main():
    twttr = input("Input: ")
    print(f"Output: {rem_vow(twttr)}")

def rem_vow(txt):
    return re.sub(r"[aeiou]", "", txt, flags=re.IGNORECASE).strip()

main()
