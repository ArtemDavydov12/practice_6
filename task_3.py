def middle(t):
  t.pop(0)
  t.reverse()
  t.pop(0)
  t.reverse()
  return t

t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(middle(t))
