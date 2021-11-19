def cumsum(t):
    c = 0
    cs = [[], [], []]
    s = 0
    for i in t:
        l = 0
        for k in i:
            c += k
            cs[s].append(c)
            l += 1
            if l == 3:
                s += 1
    return cs


t = [[2, 4, 6], [1, 3, 5], [7, 8, 9]]
print(cumsum(t))
