# T = int(input())

# for tc in range(1, T+1):
#     maps = list(input().split())
#     cal = ["+","/","-",".","*","%"]

#     for i in range(len(maps)):
#         try:
#             maps[i] = int(maps[i])
#         except ValueError:
#             pass
    
#     st = []
#     ret = 0
#     answer = 0
#     for i in maps:
#         if i in cal:
#             if i == "+":
#                 if len(st) > 2:
#                     ret = st[-1] + st[-2]
#                     st.pop()
#                     st.pop()
#                 else:
#                     answer = "error"
#             elif i == "-":
#                 if len(st) > 2:
#                     ret = st[-1] - st[-2]
#                     st.pop()
#                     st.pop()
#                 else:
#                     answer = "error"
#             elif i == "/":
#                 if len(st) > 2:
#                     ret = st[-1] // st[-2]
#                     st.pop()
#                     st.pop()
#                 else:
#                     answer = "error"                    
#             elif i == "*":
#                 if len(st) > 2:
#                     ret = st[-1] * st[-2]
#                     st.pop()
#                     st.pop()
#                 else:
#                     answer = "error"                    
#             elif i == ".":
#                 break
#             st.append(ret)
#             ret = 0
#         else:
#             st.append(i)
#     print(st)

# T = int(input())

# for tc in range(1, T+1):
#     st = [0] * 300
#     top = -1
#     nums = input().split()
#     for x in nums:
#         if x not in '+-*/.': # 피연산자면
#             top += 1
#             st[top] = int(x)
#         elif x in '+-*/.':
#             op2 = st[top]
#             top -= 1
#             op1 = st[top]
#             top -= 1
#             if x=='+': # op1 + op2
#                 top += 1
#                 st[top] = op1 + op2
#             elif x=="-":
#                 top += 1
#                 st[top] = op1 - op2
#             elif x=="/":
#                 top += 1
#                 st[top] = op1 // op2
#             elif x=="*":
#                 top += 1
#                 st[top] = op1 * op2
#             else:
#                 break
#     if st[0:3].count(0) > 0:
#         print(f"#{tc} error")
#     else:
#         print(f"#{tc} {st[0]}")

T = int(input())

for tc in range(1, T+1):
    st = []
    nums = input().split()
    cnt = 0
    flag = 0
    for x in nums:
        if x not in '+-*/.': # 피연산자면
            st.append(int(x))
        elif x in '+-*/.':
            if not st:
                cnt = 0
                flag = 1
                break
            cnt = 1
            if len(st) >= 2:
                op2 = st[-1]
                op1 = st[-2]
                st.pop()
                st.pop()
            if x=='+': # op1 + op2
                st.append(op1 + op2)
            elif x=="-":
                st.append(op1 - op2)
            elif x=="/":
                st.append(op1 // op2)
            elif x=="*":
                st.append(op1 * op2)
            else:
                break
    if not st or cnt == 0 or len(st) > 1:
        print(f"#{tc} error")
    elif st and cnt == 1:
        print(f"#{tc} {st[0]}")