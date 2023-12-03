T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(N)]
    tmp = 0
    ret = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(i, i+M):
                for l in range(j, j+M):
                    tmp += maps[k][l]
            ret.append(tmp)
            tmp = 0
    print(f"#{tc} {max(ret)}")

