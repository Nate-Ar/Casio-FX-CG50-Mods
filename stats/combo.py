# Nate-ar
# Oct 28 2023
# the allow the user to use the combination funtion directly
import funCombo
while True:
    # get the N value form the user
    n = int(input("N> "))
    # get the X value from the user
    x = int(input("X> "))
    # prin the work so it's easy to copy onto paper
    print("{0}!".format(n))
    print("--------")
    print("{0}!({1}-{2})!".format(x, n, x))
    # print output
    print("Output = {0}".format(funCombo.combo(n, x)))