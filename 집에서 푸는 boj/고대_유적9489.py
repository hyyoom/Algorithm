T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    

    maps = [list(map(int, input().split())) for _ in range(N)]

    ret = []
    maxv = 0
    for i in range(N):
        cnt = 0
        maxv = 0
        for j in range(M):
            if maps[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if maxv < cnt:
                maxv = cnt
                ret.append(maxv)
 
    for i in range(M):
        cnt2 = 0
        maxv = 0
        for j in range(N):
            if maps[j][i] == 1:
                cnt2 += 1
            else:
                cnt2 = 0
            if maxv < cnt2:
                maxv = cnt2
                ret.append(maxv)

    print(f"#{tc} {max(ret)}")
