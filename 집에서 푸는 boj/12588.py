T = int(input())

for tc in range(1, T+1):
    second = input()
    origin = input()


    start = second[0]

    i = 0
    j = 0
    k = 0
    chk = 0
    flag = 0
    if len(second) == 1 and len(origin) == 1 and second[0] == origin[0]:
        print(f"#{tc} 1")
        continue
    while i < len(origin)-len(second)+1:
        chk = 0
        if origin[i] == start:
            j = 0
            while j < len(second):
                if origin[i+j] == second[j]:
                    chk += 1
                j+=1
        if chk == len(second):
            flag = 1
            break
        i+=1
    
    print(f"#{tc} {flag}")
    