T = int(input())

for tc in range(1, T+1):
    N = int(input())
    word = [list(input().strip()) for _ in range(N)]

    alpha = [[chr(i), 0] for i in range(ord("A"), ord("Z")+1)]
    nums = [0] * len(alpha)

    while word:
        tmp = word.pop(0)
        for i in range(len(alpha)):
            if alpha[i][0] == tmp[0]:
                alpha[i][1] = 1
    
    ret = 0
    for i in alpha:
        if i[1] == 1:
            ret+=1
        else:
            break
    print(f"#{tc} {ret}")














