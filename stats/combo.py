import funCombo
n = int(input("N> "))
x = int(input("X> "))
print("{0}!".format(n))
print("--------")
print("{0}!({1}-{2})!".format(x, n, x))
print("Output = {0}".format(funCombo.combo(n, x)))