T = int(input())

def solve(idx,N,target,sums,ret):
    if idx == N:
        tmp = sums-target
        if tmp >= 0:
            ret.append(tmp)
        return
    
    solve(idx+1,N,target,sums+numbers[idx],ret)
    solve(idx+1,N,target,sums,ret)



for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    ret = []
    solve(0,len(numbers), M, 0, ret)
    # print(ret)
    print(f"#{tc} {min(ret)}")