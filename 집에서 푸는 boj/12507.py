
def bina_A(end,key,binary,start):
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start+end) // 2
        if mid == key:
            return cnt
        elif mid < key:
            start = mid
        else:
            end = mid
    return 0

T = int(input())
for tc in range(1,T+1):
    
    end,A,B = map(int,input().split())
    binary = [i for i in range(1, end+1)]
    start = 1
    cnt_A = bina_A(end,A,binary,start)
    cnt_B = bina_A(end,B,binary,start)
    if cnt_A < cnt_B:
        print(f"#{tc} A")
    elif cnt_A > cnt_B:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")


