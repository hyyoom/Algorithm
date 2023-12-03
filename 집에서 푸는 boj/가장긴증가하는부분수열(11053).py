# LIS알고리즘 (최장 증가 부분 수열)
# 1. 변수선언(DP)
# 2. 주어진 숫자의 배열에서 인덱스를 하나씩 늘려 LIS를 찾는다.
# 이때, 인덱스는 1~N 0번째 인덱스의 숫자는 길이가 무조건 1이기 때문!
# 3. 이중 반복문으로 길이를 찾으려는 순자의 이전값들과 비교하여 LIS배열값을 최신화

N = int(input())
nums = list(map(int,input().split()))
dp = [1] * N
for i in range(1,N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))