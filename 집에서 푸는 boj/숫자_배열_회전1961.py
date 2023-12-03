# 90도 == i,j하는데 [j][i]에서 i가 거꾸로
# 180도 == i고정에 j만 거꾸로
# 270 ==  i,j하는데 j를 마지막부터

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    first = []
    second = []
    third = []

    first_tmp = [[] for _ in range(N)]
    second_tmp = [[] for _ in range(N)]
    third_tmp = [[] for _ in range(N)]


    # 90도
    for i in range(N):
        for j in range(N-1,-1,-1):
            first.append(maps[j][i])

    #180도
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            second.append(maps[i][j])

    #270도
    for i in range(N-1,-1,-1):
        for j in range(N):
            third.append(maps[j][i])
    
    tmp = 0
    for i in range(N):
        first_tmp[i] = first[tmp:tmp+N]
        second_tmp[i] = second[tmp:tmp+N]
        third_tmp[i] = third[tmp:tmp+N]
        tmp += N

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            first_tmp[i][j] = str(first_tmp[i][j])
            second_tmp[i][j] = str(second_tmp[i][j])
            third_tmp[i][j] = str(third_tmp[i][j])


    for i in range(N):
        print("".join(first_tmp[i]),end=" ")
        print("".join(second_tmp[i]),end=" ")
        print("".join(third_tmp[i]))