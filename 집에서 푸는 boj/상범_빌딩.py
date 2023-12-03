from collections import deque
dy = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dl = [0,0,0,0,-1,1]
find_exit = []


for tc in range(0x99999):
    L,N,M = map(int, input().split())
    if not L and not N and not M:
        break
    maps = [[] for _ in range(L)]

    i = 0
    j = 0
    while i < L:
        j = 0
        while j < N:
            data = list(input().strip())
            if data :
                maps[i].append(data)
                j+=1
        i+=1

    for i in range(L):
        for j in range(N):
            for k in range(M):
                if maps[i][j][k] == "S":
                    s_dir = [i,j,k]

    def bfs(s_dir):
        global find_exit
        v = [[[0] * M for _ in range(N)] for _ in range(L)]
        q = deque()
        l = s_dir[0]
        y = s_dir[1]
        x = s_dir[2]
        
        find_exit = []

        v[l][y][x] = 1
        q.append([l,y,x])
        while q:
            l,y,x = q.popleft()
            if maps[l][y][x] == "E":
                for i in range(L):
                    for j in range(N):
                        for k in range(M):
                            if maps[i][j][k] == "E" and v[i][j][k]:
                                find_exit.append(v[i][j][k]-1)
            for k in range(6):
                ny = dy[k] + y
                nx = dx[k] + x
                nl = dl[k] + l
                if 0<=ny<N and 0<=nx<M and 0<=nl<L and not v[nl][ny][nx] and maps[nl][ny][nx] != "#":
                    v[nl][ny][nx] = v[l][y][x]+1
                    q.append([nl,ny,nx])


    bfs(s_dir)
    if find_exit:
        print(f"#Escaped in {min(find_exit)} minute(s).")
    else:
        print("Trapped!")
    
    find_exit=[]
    last = input()
