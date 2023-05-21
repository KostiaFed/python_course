a = {'a1': 1, 'b2': 2, 'a3': 3, 'c4': 4} 
cpy = a.copy()

for v in cpy.keys():
  if v[0] == 'a':
    del a[v]

print(a)