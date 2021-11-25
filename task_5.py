def Is_sorted(t) :
    x = sorted(t)
    if x == sorted(t) :
        t=bool(1)
    else : t = bool(0)
    print (t)

t=[3,1,7,4,5,2,6,78,8,67]
Is_sorted(t)
