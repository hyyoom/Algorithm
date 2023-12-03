import sys
input = sys.stdin.readline

for tc in range(10):
	T, E = map(int, input().split())

	node = [[] for _ in range(100)]
	node_input = list(map(int, input().split()))
	for i in range(E):
		a,b = node_input[i * 2], node_input[i*2+1]
		node[a].append(b)
	st = [0]
	v = [0] * 100
	while st:
		now = st.pop()
		if v[now] == 0:
			v[now] = 1
			for i in node[now]:
				if v[i] == 0:
					st.append(i)
	ret = 1
	if v[99] == 0:
		ret = 0
	print(f"#{T} {ret}")
