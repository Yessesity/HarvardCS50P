def main():
    #starting amount due
    amount_due = 50
    #prevent code from ending if amount due is not paid
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coins = int(input("Insert coin: "))
        #only allow coins of certain value
        if coins in [5, 10, 25, 50]:
        #subtract coins from amount due
            amount_due -= coins
        #once fully paid, calculate if there is change
        if amount_due <= 0:
            print(f"Change Owed: {-amount_due}")

main()
