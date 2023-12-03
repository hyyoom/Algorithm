T = int(input())
minv = 99999999
maxv = -99999999

def solve(idx,target,result,op,v,nums,ret):
    global maxv
    global minv
    
    if idx == target:
        # print(result)
        value = nums[0]
        for i in range(target):
            if result[i] == '+':
                value+=nums[i+1]
            elif result[i] == '-':
                value-=nums[i+1]
            elif result[i] == '*':
                value*=nums[i+1]
            elif result[i] == '/':
                value/=nums[i+1]
                value = int(value)
        if value < minv:
            minv = value
        if value > maxv:
            maxv = value
        return
    else:
        for i in range(target):
            if not v[i]:
                v[i] = 1
                solve(idx+1,target,result+[op[i]],op,v,nums,ret)
                v[i] = 0


for tc in range(1, T+1):
    N = int(input())
    op_tmp = list(map(int,input().split()))
    
    op = []
    op += op_tmp[0]*['+']
    op += op_tmp[1]*['-']
    op += op_tmp[2]*['*']
    op += op_tmp[3]*['/']
    nums=list(map(int, input().split()))
    # print(nums)
    
    v = [0]*len(op)
    ret = []
    solve(0,len(op),[],op,v,nums,ret)
    # print(ret)
    print(f"#{tc} {maxv-minv}")
    maxv = -99999999
    minv = 99999999
