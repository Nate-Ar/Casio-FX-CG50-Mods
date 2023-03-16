# Nate-ar
# funtion to replace is_integer becusee microPython dose not use that
def is_int(lacey):
    # converts input to string so it can be indexed
    now_string = str(lacey)
    # makes sure the input is not int (checks non string variable)
    if not isinstance(lacey, int):
        # if the last index(-1) is = to the string 0 then you know its a whole number
        if now_string[-1] == "0": return True
    # if the lacey variavle is an int then return true
    else: return True


# asks the user to input a number they want factored
print("input Number")
ints = int(input("> "))
# four loop runs, so it can go throw every possible factor
#  also gets x witch is input number divided by 2 and rounded starting at 1
for x in range(1,round(ints / 2)+1):
    # divided input by x to get a possible factor
    contest = ints / x
    # checing to see if the possible factor is a whole-number
    if is_int(contest):
        # if it is a whole number then it check to see if its not a repeat
        if contest >= x:
            # if its not then it prints it out
            print(str(x)+"x"+str(int(contest)))




