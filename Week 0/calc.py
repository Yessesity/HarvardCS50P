#input screen
print("Welcome to addition calculator")
x = float(input("Enter the first num: "))
y = float(input("Enter the second num: "))
#round number to nearest hundredths
z = round(x + y, 2)
#print ans
print (f"Answer = {z:,}")