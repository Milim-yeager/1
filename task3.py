operator = input("please enter operator: ")
num1 = float(input("please enter first number: "))
num2 = float(input("please enter second nymber: "))
operator = operator.lower()
if operator == "sum":
    print(f"{num1} + {num2} = ", num1 + num2)
if operator == "difference":
    print(f"{num1} - {num2} = ", num1 - num2)
if operator == "multiple":
    print(f"{num1} * {num2} = ", num1 * num2)
if operator == "divide":
    if num2 == 0:
        print("you cannot use 0 in the denominator")
    else:
        print(f"{num1} / {num2} = ", num1 / num2)
else:
    print("the operation is invalid")