# Nate-ar
def factor(uin):
    uin = int(uin)
    # holds factors until output
    output = []
    # four loop runs, so it can go throw every possible factor
    #  also gets x witch is input number divided by 2 and rounded starting at 1
    for b in range(1, round(uin / 2)+1):
        # divided input by x to get a possible factor
        contest = uin / b
        # checing to see if the possible factor is a whole-number
        if contest.is_integer():
            # if it is a whole number then it check to see if its not a repeat
            if contest >= b:
                # adds both numbers to the output list if it passes all if statments
                output.append(int(b))
                output.append(int(contest))
    # returns the output list
    return list(dict.fromkeys(output))


print("Running")
# makes a place to hold the user inputs
inputs = []
# place to hold all factors
factors = []
# gets 2 inputs
for i in range(0, 2):
    inputs.append(input("> "))
# uses the factor function to get all factors
for x in range(0, (len(inputs))):
    # adds all factors to factor list witch is 3d a list of lists
    factors.append(factor(inputs[int(x)]))
# list to hold common factors
cf = []
print(factors)
# confusing for loopa to read the 3d list
for g in range(0, len(factors[0])):
    for k in range(1, len(factors)):
        for l in range(0, len(factors[k])):
            if factors[k][l] == factors[0][g]:
                cf.append(factors[0][g])
# sorts the list lest to greatest
cf.sort()
# prints the list of common factors
print(cf)
# prints the greatest common factor
print("GCF = " + str(cf[-1]))
