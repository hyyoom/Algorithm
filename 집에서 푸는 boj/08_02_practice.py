N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
abs_ret = 0

for i in range(N):
    for j in range(N):
        for k in range(4):
            ny = dy[k] + i
            nx = dx[k] + j
            if 0<=ny<N and 0<=nx<N:
                abs_ret += abs(maps[ny][nx] - maps[i][j])
print(abs_ret)