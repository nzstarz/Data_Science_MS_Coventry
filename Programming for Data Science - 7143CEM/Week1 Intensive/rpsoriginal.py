import random
def rps():
    cd = 0
    cw = 0
    cl = 0
    for i in range(30):
        a = random.randint(0,3)
        b = random.randint(0,3)
        if (a==0):
            if (b==0):
                cd = cd+1
            elif (b==1):
                cl = cl+1
            else:
                cw = cw+1
        elif (a==1):
            if (b==0):
                cw = cw+1
            elif (b==1):
                cd = cd+1
            else:
                cl = cl+1
        else:
            if (b==0):
                cl = cl+1
            elif (b==1):
                cw = cw+1
            else:
                cd = cd+1
    return(cw,cd,cl)

print(rps())


