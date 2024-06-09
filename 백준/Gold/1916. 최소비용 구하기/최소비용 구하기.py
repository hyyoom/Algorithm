import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V = int(input())
E = int(input())

weights = [sys.maxsize]*(V+1)
nodes = [[] for _ in range(V+1)]

for _ in range(E):
    s,e,w = map(int, input().split())
    nodes[s].append((w, e))

start, end = map(int, input().split())

heap = []
weights[start] = 0
heappush(heap, (0, start))

while heap:
    w, v = heappop(heap)
    if weights[v] < w:
        continue
    for nw, nv in nodes[v]:
        new_weight = w+nw
        if new_weight < weights[nv]:
            weights[nv] = new_weight
            heappush(heap, (new_weight, nv))

print(weights[end]) 
    

