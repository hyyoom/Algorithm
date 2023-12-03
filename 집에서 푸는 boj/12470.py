T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num = list(map(str,input().split()))
    num_lst = [0] * 10
    for i in num[0]:
        num_lst[int(i)] += 1
    max_v = 0
    max_v_idx = 0
    for i in range(0,10):
        if max_v <= num_lst[i]:
            max_v = num_lst[i]
            max_v_idx = i
    print(f"#{tc} {max_v_idx} {max_v}")
        
