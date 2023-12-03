T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [set() for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        arr[s].add(e)
    visited = [0 for _ in range(V+1)]
    s, e = map(int, input().split())
    stack = [s]

    while stack and visited[e] == 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for v2 in arr[v]:
                if not visited[v2]:
                    stack.append(v2)

    if visited[e]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')