from collections import deque
T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    node = [[] for _ in range(N+2)]
    v = [0] * (N+1)
    
    M_lst = list(map(int, input().split()))
    for i in range(0,M*2,2):
        node[M_lst[i]].append(M_lst[i+1])
        node[M_lst[i+1]].append(M_lst[i])
    
    
    cnt = 0
    for i in range(1,N+1):
        if not v[i]:
            q = deque()
            q.append(i)
            v[i] = 1
            cnt += 1
            while q:
                p = q.popleft()
                for nq in node[p]:
                    if not v[nq]:
                        v[nq] = 1
                        q.append(nq)
    print(f"#{tc} {cnt}")
        