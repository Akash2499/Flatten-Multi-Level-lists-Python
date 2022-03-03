def flatten(L):
    c = 1
    while c == 1:
        c = 0
        L1 = []
        for i in L:
            if isinstance(i,list):
                c = 1
                for a in i:
                    L1 += [a]
            else:
                L1 += [i]
        L = L1
    return L
