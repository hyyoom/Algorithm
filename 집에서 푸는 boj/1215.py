for tc in range(1,11):
    N = int(input())

    maps = []
    for _ in range(8):
        maps.append(list(input().strip()))

    cnt = 0
    flag = 0
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                if maps[i][j+k] != maps[i][N-k+j-1]:
                    break
                flag += 1
            if flag == N//2:
                cnt += 1
            flag = 0

    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                if maps[j+k][i] != maps[N-k+j-1][i]:
                    break
                flag += 1
            if flag == N//2:
                cnt += 1
            flag = 0

    print(f"#{tc} {cnt}")
