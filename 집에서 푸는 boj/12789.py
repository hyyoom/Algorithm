from collections import deque

q = deque()
st = []

N = int(input())
data = list(map(int,input().split()))

first = min(data)

for i in data:
    q.append(i)


while q:
    next = q.popleft()
    if next == first:
        break
    else:
        st.append(next)
print(q, st)