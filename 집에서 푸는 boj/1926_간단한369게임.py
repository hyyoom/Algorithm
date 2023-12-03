N = int(input())

nums = [i for i in range(1,N+1)]

pr = ''
for i in range(N):
    pr = ''
    if "3" in str(nums[i]) or "6" in str(nums[i]) or "9" in str(nums[i]):
        tmp = str(nums[i])
        for i in tmp:
            if i == "3" or i == "6" or i == "9":
                pr += '-'
        print(f"{pr}", end=" ")
    else:
        print(f"{nums[i]}",end=" ")