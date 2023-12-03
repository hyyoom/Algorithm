N = 10


arr = [6,5,3,7,1,4,2,5,6,2]

for i in range(N - 1):
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
print(arr)