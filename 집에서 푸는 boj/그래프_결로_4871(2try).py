N = int(input())

def dfs(s, g):
    st = [s]
    visit = [0] * (v + 1)
    visit[s] = 1
    while st:
        cur = st.pop()  # s
        if cur == g:
            return 1
        for next in nodes[cur]:  # s start
            if not visit[next]:
                visit[next] = 1
                st.append(next)
    return 0


for tc in range(1, N + 1):
    v, e = map(int, input().split())

    nodes = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        nodes[a].append(b)
    s, g = map(int, input().split())
    ret = dfs(s, g)
    print(f"#{tc} {ret}")
