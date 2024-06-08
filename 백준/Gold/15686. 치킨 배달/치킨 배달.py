import sys

input = sys.stdin.readline

N,M = map(int, input().split())

maps = []
tmp = []
minv = 0xffffff
house = []

for _ in range(N):
    maps.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            tmp.append((i,j))
        if maps[i][j] == 1:
            house.append((i,j))


def get_distance(chicken):
    tmp_dis = []
    anw = 0
    for h in house:
        tmp_dis=[]
        for c in chicken:
            chicken_distance = abs(h[0]-c[0]) + abs(h[1]-c[1])
            # print(h, c, chicken_distance)
            tmp_dis.append(chicken_distance)
        anw += min(tmp_dis)
    # print(anw)
    return anw
            

def solve(idx, target, result):
    global minv
    if idx == target:
        if len(result) == M:
            mm = get_distance(result)
            if mm < minv:
                minv = mm
        return
    solve(idx+1, target, result+[tmp[idx]])
    solve(idx+1, target, result)


solve(0, len(tmp), [])
print(minv)

