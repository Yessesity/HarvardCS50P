import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
if len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hi, my name is", sys.argv[1])