from collections import deque

N, M = map(int, input().split())

grap = []
ret = []
cnt = 0
v = [[0] * M for _ in range(N)]
for _ in range(N):
    grap.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    v[y][x] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M:
                if v[ny][nx] == 0 and grap[ny][nx] != 0:
                    grap[ny][nx] = grap[y][x] + 1
                    v[ny][nx] = 1
                    q.append((ny,nx))

for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            v[i][j] = 1
            bfs(i, j)
            cnt = 0
print(grap[N-1][M-1],end="")