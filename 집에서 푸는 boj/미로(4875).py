T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y,x,maps):
    st = []
    st.append((y,x))
    v = [[0] * N for _ in range(N)]
    v[y][x] = 1
    while st:
        y, x = st.pop()
        if maps[y][x] == 3:
            return 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and maps[ny][nx] != 1 and v[ny][nx] == 0:
                v[ny][nx] = 1
                st.append((ny,nx))
    return 0

for tc in range(1, T+1):
    N = int(input())
    maps = [list(input().strip()) for _ in range(N)]
    check = 0

    for i in range(N):
        for j in range(N):
            maps[i][j] = int(maps[i][j])

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                check = dfs(i,j,maps)
                break
    print(f"#{tc} {check}")