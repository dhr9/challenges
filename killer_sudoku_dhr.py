def get_combinations(number, boxes, l=[], start=1):
    def fl_append(fl, newL):
        # newL.sort()
        fl[str(newL)] = newL

    def dict_to_list(d):
        l = []
        for key in d.keys():
            l.append(d[key])
        return l
    
    def check_if_in_l(l, n):
        return n in l

    mid = int(number/2)
    if(mid*2 == number):
        mid -= 1
    final_l = {}
    # print(number, boxes, l,"--",list(range(start, mid+1)))
    for i in range(start, mid+1):
        if(i > 9 or check_if_in_l(l,i)):
            continue
        if(boxes == 2):
            if(number-i > 9 or check_if_in_l(l, number-i)):
                continue
            j = l.copy()
            j.append(i)
            j.append(number-i)
            fl_append(final_l, j)
        else:
            j = l.copy()
            j.append(i)
            for comb in get_combinations(number-i, boxes-1, j, i+1):
                # comb.append(i)
                fl_append(final_l, comb)
    # print(number, boxes, "==>",dict_to_list(final_l),"\n")
    return dict_to_list(final_l)



def time_it(N = 10000):
    from time import time

    start = time()
    for i in range(N):
        c = get_combinations(20,4)
    print(((time()-start)/N)*1000, "ms")

time_it()