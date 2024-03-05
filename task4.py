x = int(input("if you want convert C to F, Enter 1\n\
if you want convert F to C,Enter 2."))  # PEP8 :)
if x == 1:
    C = float(input("please enter C: "))
    print("F = ", C * 1.8 + 32)
elif x == 2:
    F = float(input("please enter F: "))
    print("C = ", (F - 32) / 1.8)
else:
    print("please enter only 1 or 2:)")