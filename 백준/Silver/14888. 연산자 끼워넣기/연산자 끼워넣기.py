N = int(input())
nums = list(map(int,input().split()))
plus, minus, dup, moduel = map(int,input().split())

maxv = -9999999
minv = 0xffffffff
def comb(idx, n,p,m,d,mo,result):
    global maxv
    global minv
    if idx == n-1:
        if result > maxv:
            maxv = result
        if result < minv:
            minv = result
        return
    if p > 0:
        comb(idx+1,n,p-1,m,d,mo,result+nums[idx+1])
    if m > 0:
        comb(idx+1,n,p,m-1,d,mo,result-nums[idx+1])
    if d > 0:
        comb(idx+1,n,p,m,d-1,mo,result*nums[idx+1])
    if mo > 0:
        comb(idx+1,n,p,m,d,mo-1,int(result/nums[idx+1]))
comb(0,N,plus,minus,dup,moduel,nums[0])
print(maxv, minv)