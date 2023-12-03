# st = [0] * 100
# top = -1
# nums = '6528-*2/+'
# for x in nums:
#     if x not in '+-*/': # 피연산자면
#         top += 1
#         st[top] = int(x)
#     else:
#         op2 = st[top]
#         top -= 1
#         op1 = st[top]
#         top -= 1
#         if x=='+': # op1 + op2
#             top += 1
#             st[top] = op1 + op2
#         elif x=="-":
#             top += 1
#             st[top] = op1 - op2
#         elif x=="/":
#             top += 1
#             st[top] = op1 // op2
#         elif x=="*":
#             top += 1
#             st[top] = op1 * op2
# print(st[top])

stack = [0]*100
top = -1
icp = {'(':3, "*":2, "/":2, "+":1, "-":1}
isp = {'(':0, "*":2, "/":2, "+":1, "-":1}
fx="(6+5*(2-8)/2)"
susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')':
        while stack[top] != '(':
            susik += stack[top]
            top -= 1
        top -= 1 # '('버림. pop
        
    else:
        if top == -1 or isp[stack[top]] < icp[x]: #토큰의 우선순위가 더 높으면
            top += 1 #push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top +=1
            stack[top] = x

print(susik)




