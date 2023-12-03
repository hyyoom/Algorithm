# import sys
# # input = sys.stdin.readline
# sys.stdin = open('./test.txt', 'r')
ret = []
answer = 0

N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]

def solve(idx,target,N):
    global answer
    if target == N:
        answer += 1
        return
    if idx == N:
        return
    
    solve(idx+1,target+1,N)
    solve(idx+1,target,N)




for n,m in nums:
    solve(0,n,m)
    ret.append(answer)
    answer = 0

print(ret)



