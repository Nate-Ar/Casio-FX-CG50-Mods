# Nate-ar
# Oct 28 2023
# number combination funtion for micro python(dose not come native) and allowing user
# to get the combination for a number

# combination function for Micro Python
def combo(n, x):
    # total of factorial N
    facn = 1
    # total of factorial X
    facx = 1
    # total of factorial n-x
    facp = 1
    # use multiplication to get the total of the factorial for each var
    for w in range(0,n):
        facn = facn*(w+1)
    for q in range(0,x):
        facx = facx*(q+1)
    for i in range(0,n-x):
        facp = facp*(i+1)
    #      combination returned
    return facn / (facx*facp)
