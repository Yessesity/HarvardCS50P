def main ():
    greeting = input ("Greeting: ")
    greetinginator(greeting)

def greetinginator(g):
    if g.strip().lower().startswith("hello"):
        print ("$0")
    elif g.strip().lower().startswith("h"):
        print ("$20")
    else:
        print ("$100")

main()
