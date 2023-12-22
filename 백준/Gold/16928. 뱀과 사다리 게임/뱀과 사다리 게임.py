from collections import deque

N, M = map(int,input().split())
nodes = [0]*101
v = [0]*101
v[1] = 1
ret = []
def bfs():
    global ret

    q = deque()
    q.append((0,1,[1]))
    v[1] = 1
    while q:
        cnt, p,chk = q.popleft()
        for i in range(1,7):
            nq = p+i
            if nq<=100 and nodes[nq]:
                v[nq] = 1
                nq=nodes[nq]
            if nq<=100 and not v[nq]:
                v[nq] = 1
                q.append((cnt+1,nq,chk+[nq]))
            if v[100]:
                # ret.append(cnt)
                # print(chk+[nq],end="aaa")
                print(len(chk))
                return
    # print(v)
    # print(ret)
    # print(nodes)
    

for i in range(N+M):
    a,b = map(int,input().split())
    nodes[a] = b

bfs()
# print(v)