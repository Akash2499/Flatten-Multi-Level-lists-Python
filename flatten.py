def flatten(L):
    L1 = []
    s = []
    c = 0
    for i in L:
        while isinstance(i,list):
            if i == []:
                break
            for a in i:
                c = 0
                if s != [] and a == s[0]:
                    s = s[1:]
                if isinstance(a,list):
                    i = a
                    c = 1
                    s = a[1:] + s
                    break
                L1+= [a]
            if c == 1:
                continue
            while len(s) > 0:
                i = s[0]
                if isinstance(i,list):
                    c = 1
                    s = s[1:]
                    break
                L1+= [i]
                s = s[1:]
                
                
            if c != 1:
                i = None
        
        if i != None:
            L1 += [i]
    return L1
            

print("Akash Patel")

print(flatten([1,2,[3,4],5,[6,[7,[[[8,15,[16,17],18,[19],20],9],10],11]],25]))
print(flatten([1,2,[3,4],5,[6,[7,8]]]))
