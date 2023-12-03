from collections import deque

N, K = map(int, input().split())
v = [0] * 200001

dq = [2,-1,1]

def bfs():
    q = deque()
    q.append([N, 0])
    v[N] = 1
    while q:
        p, cnt = q.popleft()
        if p == K:
            return cnt
        for i in range(3):
            if i == 0:
                nq = dq[i]*p
                if 0 <= nq <= 100000 and not v[nq]:
                    v[nq] = 1
                    q.append([nq, cnt])
            else:
                nq = p+dq[i]
                if not v[nq] and 0 <= nq <= 100000:
                    v[nq] = 1
                    q.append([nq, cnt + 1])

print(bfs())