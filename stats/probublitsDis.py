# Nate-ar
# Oct 28 2023
# this program dose and shows to work for probability distribution
import funCombo
import math
# ask if user is using range of x value
print("1(single),2(range)")
# store response
ques = input("> ")
# get P value
p = float(input("P> "))
# calculate q value
q = 1 - p
# making sure it's a binomial problem q + p should always be 1
if q+p != 1:
    print("Not binomial problem")
# get N value
n = int(input("N> "))


# single X value
def single():
    # get the single X value
    x = int(input("X> "))
    # calculate the combination for the problem using the custom funtion
    a = funCombo.combo(n, x)
    # calculate p to the power of x
    b = math.pow(p, x)
    # calculate q to the power of n-x
    c = math.pow(q, n - x)
    # print the work, so it's easy to show work on paper
    print("c({0},{1})*{2}^{3}*{4}^{5}-{6}".format(x, n, p, x, q, n, x))
    print(a * b * c)


# range of X values
def ranges():
    # make the X array
    x = []
    # total probability var
    totalprob = 0
    # tell user how to stop the while loop
    print("Enter * to stop range")
    while True:
        # get each x value
        temp = input("> ")
        # see if user wants to spot
        if temp == "*":
            break
        # add value if it's not = *
        x.append(int(temp))
    # to probability distribution
    for w in range(0,len(x)):
        # calculate the combination for the problem using the custom funtion
        a = funCombo.combo(n, x[w])
        # calculate p to the power of x
        b = math.pow(p, x[w])
        # calculate q to the power of n-x
        c = math.pow(q, n - x[w])
        # print the work, so it's easy to show work on paper
        print("c({0},{1})*{2}^{3}*{4}^{5}-{6}".format(x[w], n, p, x[w], q, n, x[w]))
        # print the probability for that x in the range
        print(a * b * c)
        # add each probability to the total
        totalprob = totalprob + (a * b * c)
    # print the total of the probability distribution
    print("Total = {0}".format(totalprob))


# code to run the correct funtion based on the first question asked the user
if ques == "1":
    single()
elif ques == "2":
    ranges()
