from collections import deque
import sys
input = sys.stdin.readline


T = int(input())
nx = [2,-1,10,10]
v = [0]*20001


def bfs(start,end):
    q = deque()
    v[start] = 1
    # codes = ''
    q.append([start,''])
    while q:
        x,codes = q.popleft()
        if x == end:
            print(codes)
            return
        for i in range(4):
            if i == 0:
                nx = x*2
                if 0<=nx<10000:
                    q.append([nx,codes+'D'])
                elif nx > 9999:
                    nx %= 10000
                    q.append([nx,codes+'D'])
            if i == 1:
                if x == 0:
                    nx = 9999
                    if not v[nx]:
                        v[nx] = v[x]+1
                        q.append([nx,codes+'S'])
                elif 0<x:
                    nx = x-1
                    if not v[nx]:
                        v[nx] = 1
                        q.append([nx,codes+'S'])
            if i == 2:
                tmp = x
                while tmp>9:
                    tmp //= 10
                tmp_str = str(tmp)
                tmp_x = str(x)
                tmp_x = tmp_x[1:]+tmp_str
                nx = int(tmp_x)
                if not v[nx]:
                    v[nx] = 1
                    q.append([nx,codes+'L'])
            if i == 3:
                tmp = x
                while tmp >9:
                    tmp %= 10
                tmp_str = str(tmp)
                tmp_x = str(x)
                tmp_x = tmp_str + tmp_x[:-1]
                nx = int(x)
                if not v[nx]:
                    v[nx] = 1
                    q.append([nx,codes+'R'])


for tc in range(1, T+1):
    N,M = map(int, input().split())
    bfs(N,M)
