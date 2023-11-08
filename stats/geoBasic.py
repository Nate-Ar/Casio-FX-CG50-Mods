# Nate-Ar
# Nov 8 2023
# find mean variance and standard deviation of geo problems
import math

# loop
while True:
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
    # if user wants mean
    if ques == "1":
        print("1 / {0}".format(p))
        print("= {0}".format(1/p))
        print("--------")
    if ques == "2":
        print("1 - {0} / {0}^2".format(p, ))
        print("= {0}".format((1 - p) / math.pow(p, 2)))
        print("--------")
    if ques == "3":
        print("squrt(1 - {0} / {0}^2)".format(p))
        print("= {0}".format(math.sqrt((1-p)/math.pow(p,2))))
        print("--------")
