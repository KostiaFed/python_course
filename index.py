arr = [1, 2, 3, 4, 5, 6]
iter = 0

while iter < len(arr):
    if arr[iter] % 2 == 0:
        arr.pop(iter)
    else:
        iter += 1

print(arr)