from collections import deque

T = int(input())

dx = [1,-1,2,-10]

def bfs(start,end):
    q = deque()
    v = [0] * 2000001
    q.append([start,0])
    while q:
        x,cnt = q.popleft()
        if x == end:
            # print(v)
            return cnt
        for i in range(4):
            if i == 2:
                nx = x*2
                if 0<= nx <= 1000000 and not v[nx]:
                    v[nx] = 1
                    q.append([nx,cnt+1])
            else:
                nx = x+dx[i]
                if 0<= nx <= 1000000 and not v[nx]:
                    v[nx] = 1
                    q.append([nx,cnt+1])

 
for tc in range(1,T+1):
    N, K = map(int, input().split())

    print(f"#{tc} {bfs(N,K)}")