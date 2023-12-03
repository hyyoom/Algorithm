N, M, D = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
maps.append([2]*M)
tmp = [x for x in range(M)]
bow = []
bow_tmp = []
enermy_dir = []

def comb(i, N, k, target, result):
    if k == target:
        bow.append(result)
        return
    if i == N:
        return
    comb(i+1,N,k+1,target, result+[tmp[i]])
    comb(i+1,N,k,target, result)
comb(0,M,0,3,[])


for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            enermy_dir.append([i,j])


def attack(enermy_dir):
    minv = []
    i = len(maps)-1
    for j in range(len(bow)):
        min_val = 1000
        for index in range(len(enermy_dir)):
            idx_i = abs(i - enermy_dir[index][0])
            idx_j = abs(j - enermy_dir[index][1])
            # print(3- enermy_dir[index][1])
            far = idx_i+idx_j
            if far <= D:
                if far <= min_val:
                    min_val = far
                    minv.append([index, enermy_dir[index][0],enermy_dir[index][1]])
        # print(minv)
        if len(minv) >= 2:
            minv = sorted(minv, key=lambda x : x[2]) # 0번째만 쓰면됨
            enermy_dir[index][0] = minv[0][1]
            enermy_dir[index][1] = minv[0][2]
            if minv[0][1] >= N or minv[0][2] >= M:
                enermy_dir.pop(index)
        else:
            enermy_dir[index][0] = minv[1]
            enermy_dir[index][1] = minv[2]
        minv = []
        print(enermy_dir)

attack(enermy_dir)

print(maps)

