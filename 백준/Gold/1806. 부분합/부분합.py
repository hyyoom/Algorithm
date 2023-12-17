N, S = map(int, input().split())

nums = list(map(int, input().split()))

end = 0
sums = 0
minv = 0xfffff

for n in nums:
    if n >= S:
        print(1)
        exit(0)


for start in range(N):
    while end < N and sums < S:
        sums += nums[end]
        end += 1
    if sums >= S:
        minv = min(minv, end-start)
    sums -= nums[start]
if minv == 0xfffff:
    print(0)
else:
    print(minv)
    
    
    