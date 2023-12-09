# T = int(input())
def make_result(pm):
    global answer
    tmp = ''
    tt = []
    for i in range(len(nums)-1):
        tmp += nums[i]
        tmp += pm[i]
    tmp+= nums[len(nums)-1]
    
    # print(tmp)
    if eval(tmp.replace(" ","")) == 0:
        answer.append(tmp)

def make_pm(idx, N, result, v):
    if idx == N-1:
        make_result(result)
        return
    make_pm(idx+1,N,result+[' '],v)
    make_pm(idx+1,N,result+['+'],v)
    make_pm(idx+1,N,result+['-'],v)

T = int(input())
for _ in range(T):
    answer = []
    N = int(input())
    tmp = ['+','-','']
    nums = [str(x) for x in range(1,N+1)]
    v = [0]*(N)
    make_pm(0,N,[],v)
    for a in answer:
        print(a)
    print()



