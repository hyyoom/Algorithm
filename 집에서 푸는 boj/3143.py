T = int(input())

for tc in range(1, T+1):

    A, B = list(input().split())
    A = list(A)
    B = list(B)

    cnt = 0
    i = j = 0
    len_a = len(A)
    len_b = len(B)
    idx = 0
    tmp = ''

    while i < len_a:
        j = 0
        idx = 0
        if i+j < len_a and A[i] == B[j]:
            while j < len_b:
                if i + j < len_a and A[i+j] == B[j]:
                    idx += 1
                j+=1
            if idx == len_b:
                cnt+=1
                i += len_b
        if i < len_a:
            cnt+=1
        i+=1
    # print(tmp)
            
    
    print(f"#{tc} {cnt+len(tmp)}")