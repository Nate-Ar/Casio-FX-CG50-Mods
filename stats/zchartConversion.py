# deciding what rules to use for z chart conversion
def converson(z,sign):
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
        print("= 1 - zchar value of {0}".format(z))
    #     complement Rule
    elif sign == "4":
        # explain rule
        print("use Complement Rule")
        print("flip sign and 1 - p")
        # print work
        print("1-p(z<{0})".format(z))
        print("= 1 - zchar value {0}".format(z))