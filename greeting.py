def main ():
    greeting = input ("Greeting: ")
    greetinginator(greeting)

def greetinginator(g):
    if g.lower().startswith("h", "hello"):
        print ("$20")   
    else:
        print ("$100")

main()