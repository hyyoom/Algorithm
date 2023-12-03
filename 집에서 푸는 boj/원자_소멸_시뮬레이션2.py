T = int(input())

dy = [1,-1,0,0]
dx = [0,0,-1,1]

for tc in range(1, T+1):
    N = int(input())
    bom = [list(map(int, input().split())) for _ in range(N)] 
    # for i in range(len(bom)):
    #     bom[i][0] = bom[i][0] * 2
    #     bom[i][1] = bom[i][1] * 2
    for b in bom:
        b[0] *= 2
        b[1] *= 2

    ret = 0    
    for i in range(4001):
        for j in range(len(bom)):
            bom[j][0] = bom[j][0] + dx[bom[j][2]]
            bom[j][1] = bom[j][1] + dy[bom[j][2]]
        
        v, ddel = set(), set()
        for b in range(len(bom)):
            # print(b)
            if (bom[b][0],bom[b][1]) in v:
                ddel.add((bom[b][0],bom[b][1]))
            else:
                v.add((bom[b][0],bom[b][1]))
        if ddel:
            print(ddel)
        
        for k in range(len(bom)-1,-1,-1):
            ci, cj = bom[k][0],bom[k][1]
            if (ci,cj) in ddel:
                ret += bom[k][3]
                bom.pop(k)
            elif abs(bom[k][0]) > 2000 or abs(bom[k][1]) > 2000:
                bom.pop(k)
    
    
    print(f"#{tc} {ret}")
    