import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

tmp = arr[0]
cnt = 0
dp = [0] * (N)
for i in range(0, len(arr)-1):
    if arr[i] < arr[i+1]:
        dp[i] = max(dp[:i-1])
    # else:
    #     dp[i] = dp[i-1]

print(dp)
print(max(dp))