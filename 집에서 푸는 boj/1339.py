import sys
input = sys.stdin.readline

N = int(input())

maps=[]
for _ in range(N):
    maps.append(input().strip())

idx = 0
dic = {}
for i in range(len(maps)):
    idx = 0
    for j in range(len(maps[i])-1, -1,-1):
        if maps[i][idx] not in dic:
            dic[maps[i][idx]] = 10 ** j
        else:
            dic[maps[i][idx]] += 10 ** j
        idx+=1

val = list(dic.values())
val.sort(reverse=True)

nums = [i for i in range(9, 9-len(val),-1)]
j = 0
for i in range(len(val)):
    nums[j] = val[i]*nums[j]
    j+=1
print(sum(nums))



