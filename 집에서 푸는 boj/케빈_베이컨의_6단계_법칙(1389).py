import sys
input = sys.stdin.readline

N,M = map(int, input().split())

def dfs(s):
	g=[2,3,4,5]
	v = [0] * (N+1)
	st = [1]
	print(node)
	cnt = 0
	ret = []
	v[s] = 1
	while st:
		cur = st.pop()
		for next in node[cur]:
			if not v[next]:
				cnt += 1
				v[next] = 1
				st.append(next)
			if 2 in node[next] or next==3:
				ret.append(v.count(1))
				break
	print(ret)
    

node = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

dfs(1)

# while s <= N:
#     g = 1
#     tmp = 0
#     while g<=N:
#         tmp = dfs(s,g)
#         g+=1
#     ret.append(tmp)
#     s+=1
