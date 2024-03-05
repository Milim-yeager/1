def typeNumber(Dawn):
    try:
        num = float(Dawn)
        if num.is_integer():
            print(int)
        else:
            print(float)
    except ValueError:
        if Dawn[0] == '[' and Dawn[-1] == ']':
            print(list)
        else:
            print(str)


dawn = input("please enter: ")
typeNumber(dawn)  #:)
