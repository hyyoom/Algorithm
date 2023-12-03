T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pado = [0]*110
    pado[0] = 1
    pado[1] = 1
    pado[2] = 1
    i = 0
    while i < 101:
        pado[i+3]=pado[i]+pado[i+1]
        i+=1
    print(pado[N-1])