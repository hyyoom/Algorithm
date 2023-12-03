T = int(input())

dir = [[-1,0], [1,0], [0,-1], [0,1]]

def check_flag(data):
    for i in range(N):
        if not data[i][4]:
            return 0
    return 1


def move_dir(data):
    for i in range(N):
        if -2000 >= data[i][0] or 2000<data[i][0]\
            or -2000 >= data[i][1] or 2000 <data[i][1]:
                data[i][4] = 1
        if data[i][4] == 0:
            data[i][0] += dir[data[i][2]][0]
            data[i][1] += dir[data[i][2]][1]


def count_score(data):
    score = 0
    for i in range(N):
        for j in range(i+1,N):
            if data[i][0] == data[j][0]\
                and data[i][1] == data[j][1] and data[i][4] != 1 and data[j][4] != 1:
                    score += data[j][3] +data[i][3]
                    data[i][4] = 1
                    data[j][4] = 1
    return score



for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        data[i][0],data[i][1] = data[i][1],data[i][0]
        data[i].append(0)
        for j in range(2):
            data[i][j] = data[i][j]
    
    score = 0
    while True:
        if check_flag(data): # 모든 플래그가 1로 돼었다면
            break
        move_dir(data)
        score += count_score(data)
    print(f"#{tc} {score}")
    
        