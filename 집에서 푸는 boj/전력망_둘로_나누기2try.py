from collections import deque

n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
minv = 0xffffff
ret = []

def bfs(g,node):

    v = [0] * (n+1)
    q = deque()
    q.append(g) # 시작 인덱스
    v[g] = 1
    cnt = 0
    while q:
        p = q.popleft()
        for nq in node[p]:
            if not v[nq]:
                v[nq] = 1
                q.append(nq)
                cnt += 1
    # print(v)
    return cnt


def solution(n, wires):
    v = [0] * (n+1)
    
    node = [[] for _ in range(n+1)]
    # node[0] += [0,0]
    cnt = len(wires)
    
    for i in range(len(wires)):
        node[wires[i][0]].append(wires[i][1])
        node[wires[i][1]].append(wires[i][0])
    
    print(node)
    ret = 0xffffff
    for a,b in wires:
        node[a].remove(b)
        node[b].remove(a)
        ret = min(ret,abs(bfs(a,node) - bfs(b,node)))
        node[a].append(b)
        node[b].append(a)
    print(ret)
          

solution(n, wires)
