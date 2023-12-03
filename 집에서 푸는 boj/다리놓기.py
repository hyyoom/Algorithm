T = int(input())

ret = 0
def solve(idx,M,N):
    global ret
    if idx ==  N:
        ret += 1
        return
    for i in range(M):
        if bit[i] == 0:
            bit[i] = 1
            arr[idx] = 1
            solve(idx+1, M,N)
            bit[i] = 0
            


for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = [0]*M
    bit = [0]*M
    
    solve(0,M,N)
    print(ret)
    