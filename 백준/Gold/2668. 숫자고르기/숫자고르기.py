N = int(input())
c2 = [[]]
for _ in range(N):
    c2.append(int(input().strip()))
c1 = [x for x in range(0,N+1)]


c1_tmp = []
c2_tmp = []
answer = []
def solve(i,v):
    global c1_tmp
    global c2_tmp
    global answer
    # if c2[i] == c1[i]:
    #     print(c2[i])
    #     return
    if v[i]:
        c1_tmp.sort()
        c2_tmp.sort()
        if len(c1_tmp) == len(c2_tmp):
            flag = 0
            for i in range(len(c1_tmp)):
                if c1_tmp[i] != c2_tmp[i]:
                    flag = 1
                    break
            if not flag:
                answer.append(c1_tmp)
        c1_tmp = []
        c2_tmp = []
        return
    v[i] = 1
    c2_tmp.append(c2[i])
    c1_tmp.append(c1[i])
    solve(c2[i],v)

for i in range(1,len(c1)):
    v = [0]*(N+1)
    solve(i,v)

anw = []

for a in answer:
    for s in a:
        if s not in anw:
            anw.append(s)
anw.sort()
print(len(anw))
for a in anw:
    print(a)