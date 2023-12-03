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
flag = [3,-1]


def chk_flag(flag, y, x):
    if flag[0] == 3 and flag[1] == -1:
        x += 1
        return y,x
    else:
        if flag[0] == 0:
            if flag[1] == 0:
                x -= 1 # L
            else:
                x += 1
        elif flag[0] == 1:
            if flag[1] == 0:
                x += 1
            else:
                x -= 1
        elif flag[0] == 2:
            if flag[1] == 0:
                y += 1
            else:
                y -= 1
        elif flag[0] == 3:
            if flag[1] == 0:
                y -= 1
            elif flag[1] == 1:
                y += 1
            else:
                x += 1
        return y,x


tail_dir = [[0],[0]]
while True:
    y,x = chk_flag(flag,y,x)
    if (0<=y<N and 0<=x<N) or maps[y][x] == 1:
        break
    if maps[y][x] == 2:
        maps[y][x] = 1
    