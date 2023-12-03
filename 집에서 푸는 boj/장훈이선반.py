T = int(input())
maxv = 99999999


def solve(idx,N,K,result):
    global maxv
    if result >= K:
        if maxv > result-K:
            maxv = result-K
        return
    if idx==N:
        return
    solve(idx+1,N,K,result+arr[idx])
    solve(idx+1,N,K,result)

for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    solve(0,N,K,0)
    print(f"#{tc} {maxv}")
    maxv=9999999