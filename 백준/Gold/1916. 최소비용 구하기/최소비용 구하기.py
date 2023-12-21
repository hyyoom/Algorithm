import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    bus[a].append((b,c))
start, end = map(int,input().split())

weight = [0xffffffff]*(N+1)
weight[start] = 0
q = []
heapq.heappush(q,(start,0))
while q:
    node, w = heapq.heappop(q)
    if weight[node] < w:
        continue
    for next_node, next_w in bus[node]:
        all_w = w + next_w
        if all_w < weight[next_node]:
            weight[next_node] = all_w
            heapq.heappush(q, (next_node, all_w))
print(weight[end])
