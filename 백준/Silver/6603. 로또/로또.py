
def solve(idx, target, result, k):
    if idx >= k:
        if len(result) == target:
            for r in result:
                print(r, end=" ")
            print()
            return
        return
    solve(idx+1, target, result+[nums[idx]], k)
    solve(idx+1, target, result, k)


while True:
    nums = list(map(int, input().split()))
    if (nums == [0]):
        
        break 
    tmp = nums.pop(0)
    
    solve(0,6,[], tmp)
    print()