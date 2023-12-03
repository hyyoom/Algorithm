T = int(input())

def find_max_value(nums):
    maxv = nums[0]
    for i in nums:
        if maxv < i:
            maxv = i
    return maxv

for tc in range(1, T+1):
    N = int(input())
    back = list(map(int, input().split()))
    sums = 0
    maxv = 0

    idx_i = 0
    cnt = 0
    ret = 0
    flag = 1
    i = 0
    while flag:
        maxv = find_max_value(back)
        i = len(back)
        for i in range(len(back)-1,-1,-1):
            if len(back) > i:
                if back[i] == maxv:
                    front = back[:i+1]
                    back = back[i+1:]
                    idx_i = i
            if len(back) == 0:
                flag = 0
        for j in range(idx_i):
            sums += front[j]
        ret += (maxv*idx_i) - sums
        sums = 0
        cnt = 0

    print(f"#{tc} {ret}")
        








