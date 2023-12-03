

T = int(input())

for tc in range(1,T+1):
    maps = [[-1] * 11 for _ in range(11)]

    N = int(input())
    datas = []
    for i in range(N):
        datas.append(list(map(int, input().split())))

    for data in datas:
        for i in range(data[0], data[2]+1):
            for j in range(data[1], data[3]+1):
                maps[i][j] += data[4]

    ret = 0
    for i in maps:
        ret += i.count(2)

    print(f"#{tc} {ret}")