import math

print("1(mean),2(Variance),3(Standard Division)")
ques = input("> ")
p = float(input("P> "))
n = int(input("N> "))
if ques == "1":
    print("{0}*{1} = {2}".format(n,p,n*p))
elif ques == "2":
    q = float(input("Q> "))
    print("{0}*{1}*{2} = {3}".format(n,p,q,n*p*q))
elif ques == "3":
    q = float(input("Q> "))
    print("squrt({0}*{1}*{2}) = {3}".format(n, p, q, math.sqrt(n * p * q)))
