def has_duplicates(s):
    a = sorted(s)
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return True


s = "asdfghjka"
print(has_duplicates(s))
