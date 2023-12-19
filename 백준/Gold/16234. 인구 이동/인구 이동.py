from collections import deque
import sys
input = sys.stdin.readline


def BFS(r, c):
    q.append([r, c])
    union = [[r, c]]
    sm = arr[r][c]
    v[r][c] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in move:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                if L <= abs(arr[ni][nj] - arr[ci][cj]) <= R:
                    v[ni][nj] = 1
                    union.append([ni, nj])
                    sm += arr[ni][nj]
                    q.append([ni, nj])

    if len(union) > 1:
        for x, y in union:
            arr[x][y] = sm // len(union)

    return sm


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()

union = []
cnt = 0

move = ((-1, 0), (1, 0), (0, -1), (0, 1))
flag = True
while flag:
    v = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                sm = BFS(i, j)
                if sm > arr[i][j]:
                    flag = True

    if not flag:
        break
    cnt += 1

print(cnt)