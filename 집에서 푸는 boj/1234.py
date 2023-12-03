for tc in range(1,11):
    N,arr = map(int, input().split())
    arr = list(str(arr))

    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr = arr[:i] + arr[i+2:]
            i = 0
        i+=1

    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr = arr[:i] + arr[i+2:]
            i = 0
        i+=1

    while True:
        if arr[0] == "0":
            arr.pop(0)
        else:
            break

    print(f"#{tc}", "".join(arr))