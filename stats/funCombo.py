
def combo(n,x):
    facn = 1
    facx = 1
    facp = 1
    for w in range(0,n):
        facn = facn*(w+1)
    for q in range(0,x):
        facx = facx*(q+1)
    for i in range(0,n-x):
        facp = facp*(i+1)
    return facn / (facx*facp)
