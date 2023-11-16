# Nate-ar
# Nov 16 2023
# solve standard distribution
import math


def mathpart():
    # print formaula
    print("(1 / sigma * squrt(2*pi)) * e^ (-(x-m)^2 / 2 * sigma ^ 2) ")
    # print current version
    print("(1/{0}*squrt(2*pi))*e^-({1}-{2})^2/2*{0}^2".format(sigma, x, m))
    print("= {0}".format((1 / sigma * math.sqrt(2 * pi)) * math.exp(-math.pow(x - m, 2) / 2 * math.pow(sigma, 2))))


# define pi
pi = math.pi
# get mean
m = float(input("Mean> "))
# get x
x = float(input("x> "))
# get standard divation or simga
sigma = float(input("Sigma> "))
mathpart()
