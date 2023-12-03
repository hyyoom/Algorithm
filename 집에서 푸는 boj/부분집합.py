def solve(idx,N):
    if idx == N:
        print(tmp)
        print()
        return
    for i in range(N):
        if bit[i] == 0:
            bit[i] = 1
            tmp[idx] = arr[i]
            solve(idx+1, N)
            bit[i] = 0
            

# def perm(idx ,N):
# 	if idx == N:
# 		if permu[:N] not in pm:
# 			pm.append(permu[:N])
# 		return
# 	else:
# 		for i in range(N):
# 			if used[i] == 0:
# 				used[i] = 1
# 				permu[idx] = cal[i]
# 				perm(idx+1, N)
# 				used[i] = 0

tmp = [0,0,0]
arr = [1,2,3]
bit = [0,0,0]
solve(0,3)