import funCombo
import math
print("1(single),2(range)")
ques = input("> ")
p = float(input("P> "))
q = float(input("Q> "))
n = int(input("N> "))


def single():
    x = int(input("X> "))
    a = funCombo.combo(n, x)
    b = math.pow(p, x)
    c = math.pow(q, n - x)
    print("c({0},{1})*{2}^{3}*{4}^{5}-{6}".format(x, n, p, x, q, n, x))
    print(a * b * c)


def ranges():
    x = []
    totalprob = 0
    print("Enter * to stop range")
    while True:
        temp = input("> ")
        if temp == "*":
            break
        x.append(int(temp))

    for w in range(0,len(x)):
        a = funCombo.combo(n, x[w])
        b = math.pow(p, x[w])
        c = math.pow(q, n - x[w])
        print("c({0},{1})*{2}^{3}*{4}^{5}-{6}".format(x[w], n, p, x[w], q, n, x[w]))
        print(a * b * c)
        totalprob = totalprob + (a * b * c)
    print("Total = {0}".format(totalprob))


if ques == "1":
    single()
elif ques == "2":
    ranges()
