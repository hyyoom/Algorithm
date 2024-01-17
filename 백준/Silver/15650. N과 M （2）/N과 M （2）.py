N, M = map(int, input().split())

nums = [x for x in range(1, N+1)]


v = [0] * (N+1)
answer = []

def solve(idx, target, result):
    global v
    global nums
    global answer

    if idx == target:
        answer.append(result)
        return
    for i in range(N):
        if nums[i] not in result:
            v[idx] = 1
            solve(idx+1, target, result+[nums[i]])
            v[idx] = 0

solve(0,M,[])

for anw in answer:
    tmp = sorted(anw)
    if tmp == anw:
        for a in anw:
            print(a,end=" ")
        print()


