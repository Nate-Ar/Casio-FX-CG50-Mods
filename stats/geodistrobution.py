# Nate-ar
# Oct 31 2023
# to solve geo distribution problems
import math


# this function let the user get the geo distribution for a single x value
def single():
    # get the single x value
    x = int(input("X> "))
    # first step raise q to the power of x - 1
    step1 = math.pow(q, x - 1)
    # print the work so it can be easily writen down
    print("({0})({1})^{2}-1".format(p, q, x))
    print(step1 * p)
    # finally print the step witch is step1 * p to get the final
    print("Total = {0}%".format(round((step1 * p) * 100, 2)))


# this funtion let user do geo distribution problems with a range of x values at once
def ranges():
    # define the x array
    x = []
    # holds all the total probability added up
    total = 0
    # tell user how to quit
    print("Enter * to exit")
    # gets all the x values from user
    while True:
        # get input
        temp = input("X> ")
        # see if user wants to quit
        if temp == "*":
            break
        # if not the add input into array
        else:
            x.append(int(temp))
    # do the calculation for each x value
    for w in range(0, len(x)):
        # first step raise q to the power of x - 1
        step1 = math.pow(q, x[w] - 1)
        # then add step1*p to the total count
        total = total + step1 * p
        # print the work for each x value
        print("({0})({1})^{2}-1".format(p, q, x))
        print("{0}".format((step1 * p)))
    print("----------")
    # print the total
    print(total)
    # print the total in %
    print("Total = {0}%".format(round(total * 100, 2)))


# loop
while True:
    # ask if x is a single number or a range
    print("1(single),2(range),3(quit)")
    # hole the response
    ques = input("> ")
    # see if user wants to quit
    if ques == "3":
        quit()
    # get the p value
    p = float(input("P> "))
    # calculate p = 1-p
    q = 1 - p

    if ques == "1":
        single()
    elif ques == "2":
        ranges()
