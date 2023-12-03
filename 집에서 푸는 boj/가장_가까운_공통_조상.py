from collections import deque

T = int(input())

def bfs(start, v, nodes,chk):
    q = deque()
    q.append(start)
    v[start] = 1
    chk.append(nodes[start])
    while q:
        p = q.popleft()
        for np in nodes[p]:
            if not v[np]:
                v[np] = v[p]+1
                chk.append(nodes[np])
                q.append(np)


for tc in range(1, T+1):
    N = int(input())
    M = N - 1
    nodes = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        nodes[b].append(a)
    find_a, find_b = map(int, input().split())
    

    v1 = [0] * (N+1)
    v1chk = []
    bfs(find_a,v1,nodes,v1chk)
    v2chk = []
    v2 = [0] * (N+1)
    bfs(find_b,v2,nodes,v2chk)

    ret = []
    for i in range(len(v1)):
        if v1[i] != 0 and v2[i] != 0:
            ret.append(i)
    print(ret)
    print(nodes)
    print(v1chk, v2chk)

    