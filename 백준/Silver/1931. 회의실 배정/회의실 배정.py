import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)





# # 제일 먼저 greedy_fini의 첫 시작의 끝나는 시간을 greedy_fini_tmp에 저장함
# # 그 시작점을 가지고 greedy_start의 반복문을 돌면서 greedy_fini_tmp보다 greedy_start[i][0]이 더 크다면
# # 다시 시작 시간을 greedy_fini_tmp에 저장함
# # 저장한 후에 다시 해당 시점부터 greedy_start반복문을 돌면서 해당 [i][0]이 같을때 [i][1]이 작은걸로 대체함
# # 이때 대체하면서 greedy_fini_tmp에 greedy_start[i][0]을 넣음
# # 위의 과정이 끝나면 그 다음 반복문을 돈다.
# # 여기서 중요한건 그 다음 반복문의 [i][0]이 greedy_fini_tmp보다 커야함
# cnt = 0
# greedy_fini_tmp = greedy_fini[0][1]
# for i in range(len(greedy_fini)):
#     if greedy_fini[i][1] >= greedy_fini_tmp:
#         print(greedy_fini[i][1])
#         print(greedy_fini_tmp)
#         for j in range(len(greedy_start)):
#             if greedy_fini_tmp <= greedy_start[j][0]:
#                 greedy_fini_tmp = greedy_start[j][0]
#                 cnt += 1
#                 for k in range(j+1, len(greedy_start)):
#                     if greedy_fini_tmp != greedy_start[k][0]:
#                         break
#                     if greedy_fini_tmp == greedy_start[k][0]:
#                         if greedy_start[j][1] > greedy_start[k][1]:
#                             greed_fini_tmp = greedy_start[k][1]
#         print(greedy_fini[i])
# print(cnt)