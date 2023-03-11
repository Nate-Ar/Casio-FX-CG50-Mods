# Nate-ar
# asks the user to input a number they want factored
print("input Number")
ints = int(input("> "))
# four loop runs, so it can go throw every possible factor
#  also gets x witch is input number divided by 2 and rounded starting at 1
for x in range(1,round(ints / 2)+1):
    # divided input by x to get a possible factor
    contest = ints / x
    # checing to see if the possible factor is a whole-number
    if contest.is_integer():
        # if it is a whole number then it check to see if its not a repeat
        if contest >= x:
            # if its not then it prints it out
            print(str(x)+"x"+str(int(contest)))




