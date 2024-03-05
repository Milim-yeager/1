balance = 0
while True:
    print("1:afzayesh mojoodi\n2:daryaft pool\n3:mojoodi\n4:exit")
    select = int(input("adad amaliat ra vared konid: "))
    if select == 1:
        value = float(input("meghdar afzayesh ra vared konid: "))
        balance = value + balance
        print("mojoodi = ", balance)
    elif select == 2:
        value = float(input("meghdar pool ra vared konid: "))
        if value > balance:
            print("mojoodi kafi nemibashad.")
        else:
            balance = balance - value
            print("mpjoodi = ", balance)
    elif select == 3:
        print("mojoodi = ", balance)
    elif select == 4:
        print("movafagh bashid!")
        break
    else:
        print("amaliat ra be dorosti entekhab konid!")
