# Nate-ar
# Oct 28 2023
# to be used to fine mean,standard Division of binomial distribution problems
import math

# loop
while True:
    # tell the user the options for this program
    print("1(mean),2(Variance)")
    print("3(Standard Division),4(quit)")
    # save there response
    ques = input("> ")
    # see if user wants to quit
    if ques == "4":
        quit()
    # get the P value
    p = float(input("P> "))
    # get the N value
    n = int(input("N> "))
    # if user wants mean
    if ques == "1":
        # print he mean
        print("{0} * {1}".format(n, p))
        print("= {0}".format(n * p))
        print("--------")
    # if the user wants variance
    elif ques == "2":
        # calculate the Q value
        q = 1 - p
        # print the Variance
        print("{0} * {1} * {2}".format(n, p, q))
        print("= {0}".format(n * p * q))
        print("--------")
    # if the user wants standard deviation
    elif ques == "3":
        # get Q value
        q = 1 - p
        # print standard variation
        print("squrt({0} * {1} * {2})".format(n, p, q))
        print("= {0}".format(math.sqrt(n*p*q)))
        print("--------")
