import sys
input = sys.stdin.readline
from collections import deque
# sys.stdin = open('./test.txt', 'r')

minv = 0xfffffff
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(chicken):
    global minv
    
    q = deque()
    v = [[0]*N for _ in range(N)]
    ret = 0
    for ch in chicken:
        q.append(ch)
        v[ch[0]][ch[1]] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and not v[ny][nx]:
                v[ny][nx] = v[y][x] + 1
                if maps[ny][nx] == 1:
                    ret+=v[ny][nx]-1
                    if ret > minv:
                        return 0xfffff
                q.append((ny,nx))
    return ret


def solve(idx,re,result):
    global minv
    if len(result) == M:
        tmp = bfs(result)
        if tmp < minv:
            minv = tmp
        return
    if idx == re:
        return
    solve(idx+1,re,result+[chikens[idx]])
    solve(idx+1,re,result)


N,M = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

#치킨 좌표
chikens = []
house = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chikens.append((i,j))
        elif maps[i][j] == 1:
            house.append((i,j))

solve(0,len(chikens),[])

print(minv)