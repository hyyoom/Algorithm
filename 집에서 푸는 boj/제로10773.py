N = int(input())

st = []

for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        if st:
            st.pop()
    else:
        st.append(tmp)
print(sum(st))