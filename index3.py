arr = [1, 2, 3, 4, 5, 6]
iter = 0
max = 0

while iter < len(arr):
    if arr[iter] > max:
      max = arr[iter]
    iter +=1

print(max)