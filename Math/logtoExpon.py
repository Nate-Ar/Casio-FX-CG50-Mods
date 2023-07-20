# Nate-ar
while True:
    print("1. Log to Expon")
    print("2. Expon to Log")
    print("3. exit")
    choice = input("> ")
    choice = int(choice)
    if 0 < choice < 4:
        if choice == 2:
            print("LogA(b)=x")
            a = input("A >")
            b = input("b >")
            x = input("x >")
            print("log" + a + "(" + b + ")" + "=" + x)
        elif choice == 1:
            print("A^x = b")
            a = input("A >")
            b = input("x >")
            x = input("b >")
            print(a+"^"+x+"="+b)
        else: break
