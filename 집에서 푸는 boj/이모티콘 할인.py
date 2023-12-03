sales_tmp = [10,20,30,40]
selected = [0]*4

# def dfs(idx,N):
#     if idx == N:
#         for i in range(N):
#             print(sales_tmp[i], end=" ")
#         print()
#         return
#     selected[idx] = 1
#     dfs(idx+1,N)
#     selected[idx] = 0
#     dfs(idx+1,N)

# dfs(0,4)

perm_arr = [0]*4
arr=[1,2,3,4]
N = 4

def perm(tmp,idx,N):
    if idx == N:
        print(tmp)
        return
    for i in range(N):
        tmp[idx] = arr[i]
        perm(tmp,idx+1,N)

perm([0]*4, 0, 4)
# def solution(users, emoticons):
    