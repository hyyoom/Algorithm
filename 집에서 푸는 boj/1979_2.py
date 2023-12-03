T = int(input())

for text_case in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    for i in range(N):
        r_cnt = 0
        c_cnt = 0
        for j in range(N):

            if data[i][j] == 1:
                r_cnt += 1
                if j == N-1 and r_cnt == K:
                    #print(f'r {i, j}')
                    result += 1
                    r_cnt = 0
            elif data[i][j] == 0:
                if r_cnt == K:
                    #print(i, j)
                    result += 1
                r_cnt = 0
           

            if data[j][i] == 1:
                c_cnt += 1
                if j == N-1 and c_cnt == K:
                    result += 1
                    c_cnt = 0
            elif data[j][i] == 0:
                if c_cnt == K:
                    result += 1
                c_cnt = 0

    print(f'#{text_case} {result}')