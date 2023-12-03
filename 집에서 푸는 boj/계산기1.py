def find(exp):
    post_exp = ''
    st = []

    isp = {"*":2 , "/":2, "+": 1, "-": 1, "(" : 0} 
    icp = {"*":2 , "/":2, "+": 1, "-": 1, "(" : 3} 

    for c in exp:
        if c in '+-*/()':
            if c == ")":
                while st[-1] != "(":
                    post_exp += st.pop()
                st.pop() # 여는 괄호 버리기
                continue # 다음 토큰 읽어오기
            if not st:
                st.append(c)
            elif isp[st[-1]] < icp[c]: # 지금 들어가는게 스택의 top의 우선순위보다 높으면
                st.append(c)
            else: 
                while st and isp[st[-1]] >= icp[c]:
                    post_exp += st.pop()
                st.append(c)
        else: # 피연산자
            post_exp += c
    while st: # 남은 연산자 출력
        post_exp += st.pop()
    return post_exp

for tc in range(1, 11):
    st = []
    N = int(input())
    nums = list(input().strip())
    flag = 0

    nums = find(nums)

    op1 = 0
    op2 = 0
    for x in nums:
        if x != '+': # 피연산자면
            st.append(int(x))

        elif x == '+':
            if len(st) >= 2:
                op1 = st[-1]
                op2 = st[-2]
                st.pop()
                st.pop()
            if x=='+': # op1 + op2
                st.append(op1 + op2)
    print(f"#{tc} {st[0]}")