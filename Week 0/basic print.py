#printing a variable on the same line as text sol.1
action1=input("What do you want to do? ").strip().title()
print (f"cool, I also want to {action1}")
#printing a variable on the same line as text sol.2
print("What do you want to do?")
action2=input("- ").strip().title()
print ("cool, I also want to "+action2)
#printing a variable on the same line as text sol.3
action3=input("What do you want to do? ").strip().title()
print ("cool, I also want to", action3)
#printing a variable on the same line as text sol.4
action4=input("What do you want to do? ").strip().title()
print ("cool, I also want to ", end="")
print (action4)
#point=lots of solutions to the same problem
print (f"cool, it seems humans like you want to do a lot of stuff huh? stuff like {action1}, {action2}, {action3}, and {action4}")
