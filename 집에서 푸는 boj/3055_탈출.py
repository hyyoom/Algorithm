from collections import deque

N,M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]
v = [[0]*M for _ in range(N)]

water = []
start = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]


for i in range(N):
    for j in range(M):
        if maps[i][j] == '*':
            water.append([i,j,"wa"]) #wa
        elif maps[i][j] == 'S':
            start.append([i,j,"st"]) #start

def bfs():
    q = deque()
    q = deque()
    for wa in water:
        q.append(wa)
        v[wa[0]][wa[1]] = -1
    v[start[0][0]][start[0][1]] = 1
    q.append(start.pop())
    
    while q:
        y,x,flag = q.popleft()
        if maps[y][x] == "D" and flag == "st":
            print(v[y][x]-1)
            exit()
        if flag == "wa":
            for k in range(4):
                ny = dy[k] + y
                nx = dx[k] + x
                if 0<=ny<N and 0<=nx<M and not v[ny][nx]\
                    and maps[ny][nx] == '.':
                        v[ny][nx] = -1
                        q.append([ny,nx,"wa"])
        else:
            for k in range(4):
                ny = dy[k] + y
                nx = dx[k] + x
                # if maps[ny][nx] == "S":
                #     return
                if 0<=ny<N and 0<=nx<M and v[ny][nx] == 0\
                    and (maps[ny][nx] == '.' or maps[ny][nx] == "D"):
                        if v[ny][nx] != -1 and v[ny][nx] == 0:
                            v[ny][nx] = v[y][x] + 1
                            q.append([ny,nx,"st"])
    print("KAKTUS")
    exit()
        
    


            
bfs()