N, M = map(int,input().split())


dic = {}
for _ in range(N):
    a, b = input().split()
    dic[a] = b

# print(dic)

answer = []
for _ in range(M):
    a = input().strip()
    answer.append(dic[a])

for a in answer:
    print(a)