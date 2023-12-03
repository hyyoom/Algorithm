import sys
input = sys.stdin.readline

N = int(input())
score = [int(input().strip()) for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]

# if N == 1:
#     print(score)

for i in range(1,N + 1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + score[i-1]
    dp[i][2] = dp[i-1][1] + score[i-1]

print(max(dp[N]),end="")