from collections import deque

ret = set()

def make_q(q):
    i = 0
    make_three = []
    n = N//4
    while i < N:
        make_three.append(q[i:i+n])
        i+=n
    return make_three

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hex_n = input().strip()
    # hex_n = hex_n[N-1] + hex_n[0:N-1]
    tmp = []
    
    for _ in range(K+1):
        three = make_q(hex_n)
        hex_n = hex_n[N-1] + hex_n[0:N-1]
        tmp.append(three)
    
    sets = set()
    for i in tmp:
        for j in i:
            sets.update(i)
    
    ret = list(sets)
    for i in range(len(ret)):
        # ret[i] = "0x"+ret[i]
        ret[i] = int(ret[i],16)
    ret.sort(reverse=True)
    print(f"#{tc} {ret[K-1]}")
    