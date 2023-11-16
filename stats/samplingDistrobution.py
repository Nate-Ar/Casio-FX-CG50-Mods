# Nate-ar
# Nov 16 2023
# for sample distribution problems
import math
import zchartConversion


def zform():
    # print formal
    print("a = (a - m)/(sigma/sqrt(n))")
    #     print current version
    print("a = ({0} - {1}/({2}/sqrt({3}))".format(a, m, sigma, n))
    #     print a value after math
    print("a = {0}".format((a - m) / (sigma / math.sqrt(n))))
    return (a - m) / (sigma / math.sqrt(n))


#  get mean
m = float(input("Mean> "))
# get a
a = float(input("a> "))
# get sigma or standard deviation
sigma = float(input("Sigma> "))
# get n or the sample space
n = float(input("n> "))
# get the sign, so you know what conversion to do before looking at the z table
z = zform()
print("1(z<a), 2(z>-a)")
print("3(z<-a) ,4(z>a)")
sign = input("Sign: ")
zchartConversion.converson(z, sign)
