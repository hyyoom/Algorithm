#  오른쪽 밑으로 왼쪽 위로 반복
#  반복 끝나는 조건 == num이 N*N이면 종료 

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maps = [[0] * N for _ in range(N)]

    num = 1
    idx_j = 0
    idx_i = 0
    idx_N = N
    j_st = 0
    cnt = 0
    while num <= N*N:
        for j in range(N):
            if 0 <= idx_i < N:
                if maps[idx_i][j] == 0:
                    maps[idx_i][j] = num
                    num+=1
        idx_i += 1
        for i in range(N):
            for j in range(N-1,-1,-1):
                if maps[i][j] == 0:
                    idx_j = j
                    break
        for i in range(N):
            if maps[i][idx_j] == 0:
                maps[i][idx_j] = num
                num+=1
        
        for j in range(N-1, -1, -1):
            if 0 <= idx_N-1 < N:
                if maps[idx_N-1][j] == 0:
                    maps[idx_N-1][j] = num
                    num+=1
        idx_N-=1

        for i in range(idx_N, 0, -1):
            if maps[i][j_st] == 0:
                maps[i][j_st] = num
                num+=1
        j_st += 1

    print(f"#{tc}")
    for i in maps:
        print(*i)
        
            
