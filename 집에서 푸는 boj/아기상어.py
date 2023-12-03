from collections import deque
import sys
# sys.stdin = open('./test.txt', 'r')

dy = [-1,0,0,1]
dx = [0,-1,1,0]
shark_size = 2
shark_size_cnt = 0


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
ss = 0

def bfs(start):
    global shark
    global maps
    global shark_size
    global shark_size_cnt
    global ss

    q = deque()
    q.append(start)
    v = [[0]*N for _ in range(N)]
    v[start[0]][start[1]] = 0
    flag = 0
    v_value = 0
    answer = []
    
    while q:
        y,x = q.popleft()
        if 1<=maps[y][x]<=6 and shark_size > maps[y][x]:
            if not flag:
                flag=1
                v_value = v[y][x]
            if flag and v_value != v[y][x]:
                break
            answer.append((y,x))
            # print(f"{y,x}  상어크기{shark_size}")

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and not v[ny][nx]\
                and shark_size >= maps[ny][nx]:
                v[ny][nx] = v[y][x] + 1
                q.append((ny,nx))
    
    if len(answer) >= 1:
        answer.sort(key=lambda x:(x[0],x[1]))
        change = answer.pop(0)
        shark_size_cnt += 1
        if shark_size_cnt == shark_size:
            shark_size += 1 # 상어 키워주기
            shark_size_cnt = 0
        maps[change[0]][change[1]] = 9 # 물고기 상어로
        maps[shark[0]][shark[1]] = 0
        shark = (change[0],change[1])
        return v[change[0]][change[1]]
    else:
        return -1

for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            shark = (i,j)
ret = 0
while True:
    tmp = bfs(shark)
    if tmp == -1:
        break
    elif tmp:
        ret+=tmp

print(ret)