import sys
import copy
sys.stdin = open("c:/Users/SSAFY/Desktop/algorithm/swea/input.txt", "r")


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maps = list(map(int, input().split()))
    
    tmp_min = copy.deepcopy(maps)
    tmp_max = copy.deepcopy(maps)

    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if tmp_min[j] < tmp_min[min_idx]:
                min_idx = j
        tmp_min[i], tmp_min[min_idx] = tmp_min[min_idx], tmp_min[i]
    
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if tmp_max[j] > tmp_max[max_idx]:
                max_idx = j
        tmp_max[i], tmp_max[max_idx] = tmp_max[max_idx], tmp_max[i]

    ret = [0] * 10
    j = 0
    for i in range(10):
        if i % 2 == 0:
            ret[i] = tmp_max[j//2]
        elif i % 2 == 1:
            ret[i] = tmp_min[j//2]
        j+=1
        
    print(f"#{tc}",end=" ")
    print(*ret)