n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ret = 0
total = []

def comb(idx,N,result):
    global ret
    global total
    if sum(result) == k:
        ret += 1
        return
    if sum(result) > k:
        return
    for i in arr:
        result[idx] += i
        comb(idx+1,N,result)
        result[idx] -= i

comb(0,100,[0]*100)
print(ret)