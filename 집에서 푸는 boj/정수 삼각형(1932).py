N = int(input())

maps = [list(map(int ,input().split())) for _ in range(N)]
dp1 = [[0] * i for i in range(1,N+1)]

dp1[1][0] = maps[0][0] + maps[1][0]
dp1[1][1] = maps[1][1] + maps[0][0]

for i in range(2, N):
    for j in range(1, len(maps[i]) - 1):
        dp1[i][0] = dp1[i-1][0] + maps[i][0]


for i in range(2, N):
    for j in range(1,len(maps[i])-1):
        dp1[i][j] = max(dp1[i-1][j], dp1[i-1][j+1]) + maps[i][j]
print(dp1)
