import numpy as np
n = 100
l = np.ones(n) * -1

def toggle(i):
    l[i-1] *= -1

# Closed = -1
# Open = 1

print(l)
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j%i==0) :
            toggle(j)
print(l)

f = np.array(np.where(l==1))[0]+1
print(f)