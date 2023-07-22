def is_int(lacey):
    # converts input to string so it can be indexed
    now_string = str(lacey)
    # makes sure the input is not int (checks non string variable)
    if not isinstance(lacey, int):
        # if the last index(-1) is = to the string 0 then you know its a whole number
        if now_string[-1] == "0": return True
    # if the lacey variavle is an int then return true
    else:
        return True


def factors(const):
    user = int(const)
    output = [1]
    for x in range(1, round(user / 2 + 1)):
        st = user / x
        if is_int(st):
            output.append(int(st))
    return sorted(output)


def zero(factor, lead):
    opt = []
    for p in range(0,len(factor)):
        opt.append(str(factor[p]))
    # getting possible zero options by deviding leading factors by the constent
    for x in range(0, len(factor)):
        if not is_int(int(factor[x])/int(lead)):
            opt.append(str(factor[x])+"/"+str(lead))
        else: opt.append(int(int(factor[x]) / int(lead)))

    return opt


# front end
con = input("ENter Constent> ")
leading = input("Enter Leading> ")
print("plus or minus")
print(zero(factors(con),leading))
