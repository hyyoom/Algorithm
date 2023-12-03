

def solution(expression):
    arr = ''
    op = {}
    print(tmp)
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '*' or expression[i] == '+':
            if expression[i] not in op:
                op[expression[i]] = 1
            arr+='.'
        else:
            arr+= expression[i]
    arr = arr.split('.')
    op = list(op.keys())
    
    # solve(0,len(arr),arr,op)
    


expression = "100-200*300-500+20"
solution(expression)