def is_valid(k):
    k.sort()
    for i in range(len(k)-1):
        if(k[i]==k[i+1]):
            return False
    return True

def get_combinations(number, boxes):
    def fl_append(fl, newL):
        fl[str(newL)] = newL

    def dict_to_list(d):
        l = []
        for key in d.keys():
            l.append(d[key])
        return l

    mid = int(number/2)
    if(mid*2 == number):
        mid -= 1
    final_l = {}
    for i in range(1, mid+1):
        if(i > 9):
            continue
        if(boxes == 2):
            if(number-i > 9):
                continue
            j = [i, number-i]
            if(is_valid(j)):
                fl_append(final_l, j)
        else:
            for comb in get_combinations(number-i, boxes-1):
                comb.append(i)
                if(is_valid(comb)):    
                    fl_append(final_l, comb)
    # print(number, boxes, "==>",dict_to_list(final_l),"\n")
    return dict_to_list(final_l)

def get_combinations2(number, boxes):
    def fl_append(fl, newL):
        fl[str(newL)] = newL

    def dict_to_list(d):
        l = []
        for key in d.keys():
            l.append(d[key])
        return l

    mid = int(number/2)
    if(mid*2 == number):
        mid -= 1
    final_l = {}
    for i in range(1, mid+1):
        if(i > 9):
            continue
        if(boxes == 2):
            if(number-i > 9):
                continue
            j = [i, number-i]
            if(is_valid(j)):
                fl_append(final_l, j)
        else:
            for comb in get_combinations(number-i, boxes-1):
                comb.append(i)
                if(is_valid(comb)):    
                    fl_append(final_l, comb)
    # print(number, boxes, "==>",dict_to_list(final_l),"\n")
    return dict_to_list(final_l)

from time import time

N = 100
start = time()
for i in range(N):
    c = get_combinations2(30,4)
print(((time()-start)/N)*1000, "ms")
# print(c)
# c = get_combinations(10,4)
# print(c)
