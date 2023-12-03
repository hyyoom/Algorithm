
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
 
    ans = ''
    for i in range(N):
        for j in range(N-M+1):
            check = 1
            for k in range(M//2):
                if lst[i][j+k] != lst[i][j+M-k-1]:
                    check = 0
            if check == 1:
                for k in range(M):
                    ans += lst[i][j+k]
 
    for j in range(N):
        for i in range(N - M + 1):
            check = 1
            for k in range(M // 2):
                if lst[i+k][j] != lst[i+M-k-1][j]:
                    check = 0
            if check == 1:
                for k in range(M):
                    ans += lst[i + k][j]
 
    print(f'#{tc} {ans}')