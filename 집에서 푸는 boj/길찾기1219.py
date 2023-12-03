
def solve(g): # dfs
    # 0번에서 99번 갈수있는길이 있으면 1 아니면 0반환
    st = [0]
    v = [0] * 100
    v[0] = 1
    while st:
        top = st[-1]
        if top == 99:
            return 1
        # g[top][0], g[top][1]
        for next in g[top]:
            if next != -1 and not v[next]:
                v[next] = 1
                st.append(next)
                break
        else: # 갈수있는 길이 없다
            st.pop()
    return 0

for _ in range(10):
    tc, E = map(int,input().split())
    edges = list(map(int, input().split()))

    g = [[-1] * 2 for _ in range(100)] #0으로 초기화하면 0번 노드와 무조건 이어지게 되므로

    for i in range(0,E*2,2):
        if g[edges[i]][0] == -1:   # g[edges[i]][0]과 [1]에 1 6, 1 7 이런식으로 
            #연결되는 값들이 들어오는데, -1로 초기화 했으니까 만약 0번째가 안찼으면 0번에 들어가고 아니면 1번에
            g[edges[i]][0] = edges[i+1] 
        else:
            g[edges[i]][1] = edges[i+1]
    
    result = solve(g)
    print(f"#{tc} {result}")