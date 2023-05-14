arr = [1, 2, 3, 4, 5, 6]
iter = 0

while iter < len(arr):
    arr[iter] = arr[iter]**2
    iter += 1

print(arr)