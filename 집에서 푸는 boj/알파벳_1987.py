import sys
sys.setrecursionlimit(10**7)
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 갔던 알파벳 저장 set
# 빽 트레킹.
al = [chr(i) for i in range(ord("A"), ord("Z")+1)]
zero = [0] * len(al)
alpha = dict(zip(al,zero))
ans = 0


def dfs(y, x, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < N and 0 <= nx < M\
            and not alpha[maps[ny][nx]]:
            alpha[maps[ny][nx]] = 1
            dfs(ny, nx, cnt + 1)
            alpha[maps[ny][nx]] = 0


alpha[maps[0][0]] = 1
dfs(0,0,1)
print(ans)

