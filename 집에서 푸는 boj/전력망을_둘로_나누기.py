from collections import deque

n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
minv = 0xffffff
ret = []

def bfs(g,node):

    v = [0] * (n+1)
    q = deque()
    q.append(g[0]) # 시작 인덱스
    v[g[0]] = 1
    while q:
        p = q.popleft()
        for nq in node[p]:
            if nq in g:
                if not v[nq]:
                    v[nq] = 1
                    q.append(nq)
    # print(v)
    return v.count(1)

def power_set(i, n, v,node):
    global minv
    if i == n:
        g1 = []
        g2 = []
        for idx in range(1,n+1):
            if v[idx]:
                g1.append(idx)
            else:
                g2.append(idx)
        if g1 and g2:
            # print(g1, g2)
            g1_cnt = bfs(g1,node)
            g2_cnt = bfs(g2,node)
            if g1_cnt + g2_cnt == n:
                ret.append(abs(g1_cnt-g2_cnt))

        return

    v[i] = 1
    power_set(i + 1, n, v, node)
    v[i] = 0
    power_set(i + 1, n, v, node)


def solution(n, wires):
    v = [0] * (n+1)
    
    node = [[] for _ in range(n+1)]
    for i in range(len(wires)):
        node[wires[i][0]].append(wires[i][1])
        node[wires[i][1]].append(wires[i][0])
    
    # print(node)
    power_set(1, n, v,node)
    print(min(ret))


solution(n, wires)
