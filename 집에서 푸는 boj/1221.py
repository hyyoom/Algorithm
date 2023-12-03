
T = int(input())
for tc in range(1, T+1):
    T_s, N = map(str, input().split())
    
    str_nums = list(map(str, input().split()))
    nums = [i for i in range(10)]
    strs = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    dic1 = dict(zip(strs, nums))
    dic2 = dict(zip(nums, strs))

    
    ret_sort1 = []
    ret_sort2 = []
    for i in str_nums:
        ret_sort1.append(dic1[i])
    ret_sort1.sort()
    
    for i in ret_sort1:
        ret_sort2.append(dic2[i])
        
    print(f"#{tc}")
    print(" ".join(ret_sort2))