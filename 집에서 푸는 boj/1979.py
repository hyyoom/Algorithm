# N만큼 p를 N까지 보내면서 범위를 넘지 않았고, 흰색이라면 cnt += 1
# 돌고나서 각자 cnt가 k와 같다면 ret += 1
# return ret

T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for tc in range(1, T+1):
    N, K = map(int,input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    ret = []
    tmp_ny = 0
    tmp_nx = 0
    tmp = []
    for i in range(N):
        n = 0
        for j in range(N):
            if maps[i][j] == 1:
                for a in range(4):
                    for p in range(0,K):
                        ny = dy[a] * p + i #한쪽만 보는것
                        nx = dx[a] * p + j
                        if 0<=ny<N and 0<=nx<N and maps[ny][nx] == 1:
                            tmp.append([ny,nx])
                            cnt += 1
                            nny = ny + dy[a]
                            nnx = nx + dx[a]
                            if 0<=nny<N and 0<=nnx<N and p != K-1 and maps[nny][nnx] == 0:
                                break
                        if cnt == 3:
                            ret.append(cnt)
                            while n < len(tmp):
                                maps[tmp[n][0]][tmp[n][1]] = 0
                                n+=1
                    tmp = []
                    cnt = 1
    for i in maps:
        print(i)
    print(len(ret))




