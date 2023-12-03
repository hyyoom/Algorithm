T = int(input())

def delta(i,j,idx_cnt):
    plus = 0
    plus += maps[i][j]
    for k in range(1,idx_cnt+1):
        plus += maps[i][j+k]
        plus += maps[i][j-k]
    return plus

for tc in range(1,T+1):
    N = int(input())
    
    maps = [list(map(int, input().strip())) for _ in range(N)]
    if N == 1:
        print(f"#{tc} {maps[0][0]}")
        continue
    elif N == 3:
        ret = maps[0][1] + sum(maps[1]) + maps[2][1]
        print(f"#{tc} {ret}")
        continue


    # N//2 부터 시작. N//2-1을 계속 함. N//2-1이 1일때까지
    # 양쪽만 구하면 됨.
    # 세로 줄 돌면서 0~N//2까지
    ret = 0
    idx_cnt = 1
    ret += maps[0][N//2]
    for i in range(1,N//2+1):
        ret += delta(i, N//2, idx_cnt)
        idx_cnt += 1
    ret += maps[N-1][N//2]
    
    idx_cnt -= 2
    for i in range(N//2+1,N-1):
        ret += delta(i, N//2, idx_cnt)
        idx_cnt -= 1

    print(f"#{tc} {ret}")