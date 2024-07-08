import re

#(...) = captures text from inside and returns it, (?:...) = not capture
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
#matches.groups() = gathers all parenthesis groups
#matches.groups(n) = gathers data from parenthesis number n
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")

#this is what the walrus operator replaces
#matches = re.search(r"^(.+), *(.+)$", name)
#if matches: