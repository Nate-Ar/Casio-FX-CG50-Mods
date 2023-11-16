# Nate-ar
# Nov 16 2023
# Standard Normal Distribution
import zchartConversion

# z form parsing
def zfoarm():
    # showing work so you can copy down easy
    print("z = (x-m)/sigma")
    print("z = ({0}-{1})/{2}".format(x, m, sigma))
    print("z = {0}".format((x - m) / sigma))
    # returning z
    return (x - m) / sigma


# get mean or mue
m = float(input("Mean> "))
# get x value
x = float(input("X> "))
# get standard deviation also called sigma
sigma = float(input("Sigma> "))
# do the zform conversion so user can see what a will be
z = zfoarm()
# get the sign, so you know what conversion to do before looking at the z table
print("1(z<a), 2(z>-a),")
print("3(z<-a), 4(z>a)")
sign = input("Sign: ")
# make sign selection and print anwcer
zchartConversion.converson(z, sign)