# my_dict = {'apple': 5, 'banana': 2, 'cherry': 7, 'date': 5}

# # value 값을 기준으로 내림차순 정렬하고, value가 같은 경우 key 값을 기준으로 오름차순 정렬
# sorted_items = sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))

# # 정렬된 항목에서 key만 추출하여 리스트로 변환
# sorted_keys = [item[0] for item in sorted_items]

# print(sorted_keys)
import sys
input = sys.stdin.readline

N = int(input())

dic = {}
for _ in range(N):
    tmp = input().strip()
    z,x = tmp.split(".")
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

dic = sorted(dic.items(), key=lambda x:(x[0]))

for d in dic:
    print(d[0], end=" ")
    print(d[1])