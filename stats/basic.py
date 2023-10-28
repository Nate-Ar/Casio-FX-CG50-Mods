# Nate-ar
# Oct 28 2023
# to be used to fine mean,standard Division of binomial distribution problems
import math
# tell the user the options for this program
print("1(mean),2(Variance),3(Standard Division)")
# save there response
ques = input("> ")
# get the P value
p = float(input("P> "))
# get the N value
n = int(input("N> "))
# if user wants mean
if ques == "1":
    # print he mean
    print("{0}*{1} = {2}".format(n,p,n*p))
# if the user wants variance
elif ques == "2":
    # calculate the Q value
    q = 1 - p
    # print the Variance
    print("{0}*{1}*{2} = {3}".format(n,p,q,n*p*q))
# if the user wants standard variation
elif ques == "3":
    # get Q value
    q = 1 - p
    # print standard variation
    print("squrt({0}*{1}*{2}) = {3}".format(n, p, q, math.sqrt(n * p * q)))
