T = int(input())

for tc in range(1,11):
    maps = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    chk_set1 = set()
    chk_set2 = set()

    set1 = set()

    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(3):
                for l in range(3):
                    set1.add(maps[k+i][l+j])
            if len(set1) != 9:
                flag = -100
                break
        set1 = set()


    for i in range(0,9):
        for j in range(0,9):
            chk_set1.add(maps[i][j])
            chk_set2.add(maps[j][i])
        if len(chk_set1) != 9 or len(chk_set2) != 9:
            flag = -100
            break
        chk_set1 = set()
        chk_set2 = set()

    if flag == 0:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")







