import inflect
p = inflect.engine()

def main():
    list_name=[]
    while True:
        try:
            name = input("Name: ")
            list_name.append(name)
        except EOFError:
            final_list = p.join((list_name))
            print(f"Adieu, adieu, to {final_list}")
            break

main()
