T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(N)]

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    ret = []
    tmp = 0
    for i in range(N):
        for j in range(M):
            tmp = maps[i][j]
            for k in range(4):
                ni = di[k] + i
                nj = dj[k] + j
                if 0<=ni<N and 0<=nj<M:
                    tmp += maps[ni][nj]
            ret.append(tmp)
    print(f"#{tc} {max(ret)}")
