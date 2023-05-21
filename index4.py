a = {1: 1, 2: 2, 3: 3, 4: 4} 
vvs = []
iter = 1

for v in a:
  if a[iter] % 2 == 0:
    vvs.append(a[iter])
  iter+=1

print(vvs)