from collections import deque

N,M = map(int,input().split())
v = [0] * 100001
check = [0] * 100001

def print_move(cnt,now):
    data = []
    tmp = now
    for i in range(cnt+1):
        data.append(tmp)
        tmp = check[tmp]
    print(' '.join(map(str, data[::-1])))


def bfs(start, end):
    global v
    
    q = deque()
    q.append([start,0])
    v[start] = 1
    while q:
        p, cnt = q.popleft()
        if p == end:
            print(cnt)
            print_move(cnt,p)
            return
        for nq in ((p-1),(p+1),(p*2)):
            if 0 <= nq <= 100000 and not v[nq]:
                v[nq] = 1
                check[nq] = p
                q.append([nq,cnt+1])
# bfs(N,M)
bfs(N,M)
# print(*bfs(N,M))

    
