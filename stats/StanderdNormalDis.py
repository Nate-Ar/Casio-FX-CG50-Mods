# Nate-ar
# Nov 16 2023
# Standard Normal Distribution


# z form parsing
def zfoarm():
    # showing work so you can copy down easy
    print("z = (x-m)/sigma")
    print("z = ({0}-{1})/{2}".format(x, m, sigma))
    print("z = {0}".format((x - m) / sigma))
    # returning z
    return (x - m) / sigma


# deciding what rules to use for z chart conversion
def converson(z):
    # no conversion
    if sign == "1":
        print("straight to z cart")
        print("p(z<{0})".format(z))
    #     symmetry rule
    elif sign == "2":
        # explain symmetry rule
        print("use Symmetry Rule")
        print("flip sign drop the negative")
        # make negative positive double negative == positive
        z = -z
        # print awncer
        print("p(z<{0})".format(z))
    #     symmetry & complement Rule
    elif sign == "3":
        # expalin the rule
        print("use Symmetry & Complement Rule")
        print("drop negative and  1 - P")
        # make negative positive double negative == positive
        z = -z
        # print work
        print("1-p(z<{0})".format(z))
        print("= {0}".format(1 - z))
    #     complement Rule
    elif sign == "4":
        # explain rule
        print("use Complement Rule")
        print("flip sign and 1 - p")
        # print work
        print("1-p(z<{0})".format(z))
        print("= {0}".format(z))


# get mean or mue
m = float(input("Mean> "))
# get x value
x = float(input("X> "))
# get standard deviation also called sigma but not the greek version
sigma = float(input("Sigma> "))
# do the zform conversion so user can see what a will be
z = zfoarm()
# get the sign, so you know what conversion to do before looking at the z table
print("1(z<a), 2(z>-a), 3(z<-a)")
print("4(z>a)")
sign = input("Sign: ")
# make sign selection and print anwcer
converson(z)
