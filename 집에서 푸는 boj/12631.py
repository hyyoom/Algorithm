T = int(input())

for tc in range(1,T+1):
    arr = list(input().strip())
    
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr = arr[:i] + arr[i+2:]
            i = 0
        i+=1
    print(f"#{tc} {len(arr)}")