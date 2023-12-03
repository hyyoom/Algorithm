# N = int(input())

# grap = []
# grap.append("Don't_use")
# for _ in range(N):
#     grap.append(list(map(int, input().split())))

# tmp_sum = 0
# ret = []

# for i in range(1, N+1):
#     tmp_sum = 0
#     if i + grap[i][0] <= N + 1:
#         tmp_sum += grap[i][1]
#         while True:
#             i += grap[i][0]
#             if i > N:
#                 break
#             if i + grap[i][0] > N+1:
#                 break
#             tmp_sum += grap[i][1]
#         ret.append(tmp_sum)
# print(max(ret))

N = int(input())

t = []
p = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)


for i in range(N-1, -1, -1): # 뒤에서부터 거꾸로
    if t[i] + i > N: # 상담에 필요한 일수가 퇴사일을 넘어가면
        dp[i] = dp[i+1] # 다음날 값 그대로 가져옴
    
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i]) 
        # 뒷쪽이 상담을 할경우
        # 오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값

print(dp[0])