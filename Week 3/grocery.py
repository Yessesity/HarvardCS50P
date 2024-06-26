from collections import OrderedDict

def main():
    grocery_list = {}
    try:
        while True:
            inp = input("").upper()
            if inp in grocery_list:
                grocery_list[inp] += 1
            else:
                grocery_list[inp] = 1
    except EOFError:
        sorted_list = OrderedDict(sorted(grocery_list.items()))
        print("")
        for item in sorted_list:
             print(f"{sorted_list[item]} {item}")
    except KeyError:
        pass

main()
