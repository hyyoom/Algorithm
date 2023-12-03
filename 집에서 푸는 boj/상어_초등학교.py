import sys

# input = sys.stdin.readline
sys.stdin = open("./test.txt", "r")

N = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


students = []
stu_likes = []
for _ in range(N**2):
    tmp = list(map(int, input().split()))
    students.append(tmp.pop(0))
    stu_likes.append(tmp)

students_tmp = students[:]
stu_likes_tmp = stu_likes[:]

maps = [[0] * N for _ in range(N)]
tmp = students.pop(0)
maps[1][1] = tmp


stu_likes.pop(0)

for stu_like in stu_likes:
    directions = []
    directions_2 = []
    directions_3 = []
    tmp = students.pop(0)
    # 1번조건
    for r in range(N):
        for c in range(N):
            cnt = 0
            for k in range(4):
                nr = dy[k] + r
                nc = dx[k] + c
                if 0 <= nr < N and 0 <= nc < N:
                    if maps[nr][nc] in stu_like and not maps[r][c]:
                        cnt += 1
            if not maps[r][c]:
                directions.append([r,c,cnt])

    directions.sort(key=lambda x: (-x[2]))
    # if tmp in [6,7,9]:
    #     print(directions,"나 디렉션1", f"tmp=={tmp}")
    #     print(stu_like)
    #     for m in maps:
    #         print(m)
    #     print('-------------------')

    for i in range(1, len(directions)):
        if directions[0][2] == directions[i][2]:
            directions_2.append(directions[i])
        else:
            break
    directions_2.append(directions[0])
    # if tmp in [6,7,9]:
    #     print(f"{directions_2} 나 디렉션222 tmp===={tmp}")
    #     print(stu_like)
    #     for m in maps:
    #         print(m)
    #     print('-------------------')


    if len(directions_2) == 1:
        if not maps[directions_2[0][0]][directions_2[0][1]]:
            maps[directions_2[0][0]][directions_2[0][1]] = tmp
        continue

    # 두번째 조건
    for i in range(len(directions_2)):
        cnt = 0
        for k in range(4):
            nr = dy[k] + directions_2[i][0]
            nc = dx[k] + directions_2[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not maps[nr][nc]:  # 비었다면
                    cnt += 1
        directions_2[i][2] = cnt

    # 세번째 조건
    directions_3 = []

    directions_2.sort(key=lambda x: (-x[2]))
    for i in range(1, len(directions_2)):
        if directions_2[0][2] == directions_2[i][2]:
            directions_3.append(directions_2[i])
        else:
            break
    directions_3.append(directions_2[0])
    if len(directions_3) == 1:
        # if tmp == 3:
        #     print(tmp,"2")
        if not maps[directions_3[0][0]][directions_3[0][1]]:
            maps[directions_3[0][0]][directions_3[0][1]] = tmp
        directions_3 = []
        continue

    directions_3.sort(key=lambda x: (x[0], x[1]))

    maps[directions_3[0][0]][directions_3[0][1]] = tmp


ret = 0
for i in range(len(students_tmp)):
    for r in range(N):
        for c in range(N):
            if maps[r][c] == students_tmp[i]:
                cnt = 0
                for k in range(4):
                    nr = r + dy[k]
                    nc = c + dx[k]
                    if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] in stu_likes_tmp[i]:
                        cnt += 1
                if cnt == 0:
                    pass
                elif cnt == 1:
                    ret += 1
                else:
                    cnt -= 1
                    ret += 10**cnt
# print(maps)
# for m in maps:
#     print(m)

print(ret)
