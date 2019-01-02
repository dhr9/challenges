from time import time

a = 123456
N = 13

def getPower(a,N):
    s = "{0:b}".format(N)
    print(s)

def getPowerTraditional(a,N):
    l = 1
    for _ in range(N):
        l *= a
    print(l)
    

# START = time()
# getPower(a,N)
# print(str(time()-START)

# START = time()
# getPowerTraditional(a,N)
# print(time()-START)

# START = time()
# b = a**N
# print(str(time()-START).split("-")[1])

def trim(n):
    if(n==0):
        print(0)
        return
    s = str(n)
    power = 0
    k = n
    if("-" in  s):
        k = s[0]
        power = -int(s.split("-")[1])
    if("+" in  s):
        k = s[0]
        power = int(s.split("+")[1])
    if(k==n):
        if(str(k).split(".")[0]=="0"):
            print("multiply by 10")
            j = str(k).split(".")[1]
            k = j[-1]
        else:
            print("divide by 10")
            j = str(k).split(".")[0]
        print(j, "======", len(j)-1)
    print(k, end="")
    print("^ ", end="")
    print(power)

trim(0.0001)
trim(3.0994415283203125e-26)
trim(1234)
trim(309944.15283203125)
trim(309.94415283203125e+36)