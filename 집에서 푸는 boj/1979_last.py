# idea  1일때 카운트 증가 x 1이라면 1 2 3 4 처럼 하나씩 증가시키고 
# 0을 만나면 바로 전값을 확인한다

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    ret = 0
    for i in range(N):
        cnt_idx = 0
        for j in range(N):
            if maps[i][j] > 0:
                cnt_idx += 1
                maps[i][j] = cnt_idx
            if maps[i][j] == 0 and 1<=j<N:
                if maps[i][j-1] == M:
                    ret += 1
                cnt_idx = 0
            elif j == N-1:
                if maps[i][j-1] == M:
                    ret += 1
                cnt_idx = 0
        #열도 추가
            
    print(ret)