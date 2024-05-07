from collections import deque
N, M = map(int, input().split())

# 3 3
# 101
# 010
# 101

maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ret = [[0]*M for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]


# 1. 0자리라면 함수를 만들어서 내 위 양옆의 0의 갯수를 모두 세도록 한다. 이때 bfs를 사용하는게 좋을듯
# 2. 이때 map의 원본을 2부터 시작해서 변경 시키고 dic에 몇개의 0이 있는지, 저장한다.
# 3. 1의 근처에 있는 dic[number]를 모두 센다. 이때 set을 이용해서 이미 센 친구는 배제한다.

dict_cnt = 2
dic = {}
dics = {}
v = [[0]*M for _ in range(N)]

def bfs(y,x):
    global dict_cnt
    global dic
    global v
    q = deque()
    q.append((y,x))
    v[y][x] = 1
    maps[y][x] = dict_cnt

    while q:
        y, x = q.popleft()
        if dict_cnt not in dic:
            dic[dict_cnt] = 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M:
                if not v[ny][nx] and maps[ny][nx] == 0:
                    v[ny][nx] = 1
                    maps[ny][nx] = dict_cnt
                    if dict_cnt not in dic:
                        dic[dict_cnt] = 1
                    else:
                        dic[dict_cnt] += 1
                    q.append((ny,nx))

def getSolve(y,x):
    global dic
    tmp = set()
    total_cnt = 1

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<=ny<N and 0<=nx<M:
            if maps[ny][nx] != 1:
                if maps[ny][nx] not in tmp:
                    tmp.add(maps[ny][nx])
                    total_cnt += dic[maps[ny][nx]]
    return total_cnt


for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            dict_cnt += 1
            bfs(i,j)

# for i in range(N):
#     for j in range(M):
#         tmp = maps[i][j]
#         if tmp != 1:
#             if tmp not in dic:
#                 dic[tmp] = 1
#             else:
#                 dic[tmp] = dic[tmp] + 1

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            cnt_zero = getSolve(i,j)
            ret[i][j] = cnt_zero % 10



# for i in range(N):
#     for j in range(M):
#         print(maps[i][j], end=" ")
#     print()
# print("=====================")
for i in range(N):
    for j in range(M):
        print(ret[i][j], end="")
    print()


