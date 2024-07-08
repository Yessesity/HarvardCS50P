import re

email = input("What's your emaiL? ")

# "^" = start of string, "$" = end of string
# "." = any char, "+" = one or more char, "*" = 0 or more char, "?" = 0 or 1
# {m} = m number of char, {m-n} = m to n number of char
# [] = set of char, [^] = every char except the set of these char
#\w = word characters including underscores, \s = whitespace, \d = 0-9\
#\W, \S, \D = not

#my version, excludes whitespace, @ sign
#if re.search(r"^[^@\s]+@[^@\s]+\.edu$", email, re.IGNORECASE):
    #print("Valid")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")