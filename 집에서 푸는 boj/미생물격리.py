import copy

T = int(input())
 
dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]
 
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    teria = [list(map(int,input().split())) for _ in range(K)]
     
    while M:
        # 1 1 7 1  y, x, 미생물, 이동방향
        for ter in teria:
            ny = dy[ter[3]] + ter[0]
            nx = dx[ter[3]] + ter[1]
            ter[0] = ny
            ter[1] = nx
        for ter in teria:
            if ter[0] == 0 or ter[1] == 0:
                ter[2] //= 2
                if ter[3] == 1:
                    ter[3] = 2
                if ter[3] == 3:
                    ter[3] = 4
            if ter[0] == N-1 or ter[1] == N-1:
                ter[2] //=2
                if ter[3] == 2:
                    ter[3] = 1
                if ter[3] == 4:
                    ter[3] = 3
        teria = sorted(teria, key=lambda x: (x[0],x[1],x[2]), reverse=True)
        i = 1
        teria_tmp = []
        teria_tmp.append(teria.pop(0))
        while teria:
            tmp = teria.pop(0)
            if tmp[0] == teria_tmp[-1][0] and tmp[1] == teria_tmp[-1][1]:
                if tmp[2] < teria_tmp[-1][2]:
                    tmp[3] = teria_tmp[-1][3]
                tmp[2] = teria_tmp[-1][2] + tmp[2]
                teria_tmp.pop()
            teria_tmp.append(tmp)
        teria = teria_tmp
        M-=1
    ret = 0
    for ter in teria:
        ret += ter[2]
    print(f"#{tc} {ret}")