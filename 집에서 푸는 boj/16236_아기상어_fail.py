import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]


# 자신보다 큰 물고기 못지나감
# 자신보다 작은 물고기만 먹을수 있음
def find_min_fish_size_and_direction(v,dir):
    
    min_list = []
    for d in dir:
        min_list.append([v[d[0]][d[1]], d[0], d[1]])
    
    minv = 99999
    min_i = []
    for mins in min_list:
        if mins[0] <= minv:
            minv = mins[0]
            min_i.append(mins)
    print(min_i)
        

    # min_v = min_list[0][1]
    # min_i_list = []
    # for i in range(len(min_list)):
    #     if min_list[i][1] <= min_v:
    #         min_v = min_list[i][1]
    #         min_i_list.append(min_v)
    # print(min_i_list)
        
def chk_go_function(v):
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                return 0
    return 1

time = 0
def bfs(y,x,shark):
    global time
    direction_or_fish = []
    fish_cnt_of_shark_ate = 0
    # 물고기 찾으러 감 shark > maps[i][j]..
    # 물고기 찾았으면 shark 
    v = [[0]*N for _ in range(N)]
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and not v[ny][nx]\
                and shark >= maps[ny][nx]: # 먹이 찾으러 출발
                v[ny][nx] = v[y][x] + 1 # 먹이 찾으러갈때의 걸음 수
                q.append([ny,nx])
                if maps[ny][nx] < shark and maps[ny][nx] != 0: # 먹이 찾음
                    # 먹이 찾은 좌표 모두 저장
                    direction_or_fish.append((ny,nx)) # 위치 좌표와 v[ny][nx]의 크기
                    # 먹이 찾은 곳에서 가장 가까운 먹이 위치 및 걸음수 반환하는 함수
                    # if chk_go_function(v) == 1:
                    find_min_fish_size_and_direction(v,direction_or_fish)
                    
                    time += 0#걸음수 구해서 더해야함
                    # v = [[0]*N for _ in range(N)] # 먹이 찾았으니 초기화
                    fish_cnt_of_shark_ate += 1
                    if fish_cnt_of_shark_ate == shark: # 상어 크기만큼 먹었다면 크기 증가
                        shark +=1
                        fish_cnt_of_shark_ate = 0



for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            maps[i][j] = 2
            shark = 2
            bfs(i,j,shark)
            break

