from collections import deque
import sys
input = sys.stdin.readline

dir = [(0,1), (1,0), (0,-1), (-1,0)]

N = int(input())

maps = [[0] * N for _ in range(N)]
apple_N = int(input())
apple_direction = [map(int,input().split()) for _ in range(apple_N)]

for i, j in apple_direction:
    maps[i][j] = 2

change_dir_N = int(input())
change_dir = [list(input().split()) for _ in range(change_dir_N)]

for i in change_dir:
    i[0] = int(i[0])
maps[0][0] = 1

for i in maps:
    print(i)
print()
def bfs():
    dir_i = 0
    snake = deque()
    snake.append([0,0])
    time = 0
    while snake:
        for cd in change_dir:
            if time in cd:
                if cd[1] == "D":
                    dir_i = (dir_i + 1) % 4
                elif cd[1] == "L":
                    dir_i = (dir_i - 1) % 4
        y,x = snake[0] # 꼬리 부분
        ny = dir[dir_i][0] + snake[len(snake)-1][0] # 머리 늘림
        nx = dir[dir_i][1] + snake[len(snake)-1][1] # 머리 늘림
        if 0<=ny<N and 0<=nx<N:
            if maps[ny][nx] == 1: #머리 늘렸는데 몸통이면
                return time+1
            snake.append([ny,nx]) # 늘린머리 붙임
            if maps[ny][nx] == 2: # 붙일때 그 자리에 사과가 있었다면
                maps[ny][nx] = 1 # 사과 부분에 머리 있다고 표시
                if 0<=dir[dir_i][0] + ny<N and 0<=dir[dir_i][0] + nx<N:
                    if maps[dir[dir_i][0] + ny][dir[dir_i][0] + nx] == 1:
                        return time -1
                    else:
                        maps[dir[dir_i][0] + ny][dir[dir_i][0] + nx] = 1

                # maps[y][x] = 1 # 꼬리 부분 그대로 둠
            else:
                maps[ny][nx] = 1 # 사과 부분에 머리 있다고 표시
                maps[y][x] = 0 # 꼬리 부분 다시 공백처리
                snake.popleft() # 꼬리 뗌
        else:
            return time+1
        time+=1
    return time
                
print(bfs())
for i in maps:
    print(i)























