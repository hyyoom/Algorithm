
T = int(input())

# 재귀
# def solve(N):
#     if N == 20:
#         return 3
#     elif N == 10:
#         return 1
#     return solve(N-20)*2 + solve(N-10)

# def solve1(N):
#     N = N // 10
#     cnt = [0] * 31 # 300까지
#     cnt[1] = 1
#     cnt[2] = 3
#     for i in range(3, N+1):
#         cnt[i] = cnt[i-2]*2+cnt[i-1]
#     return cnt[N]

# 현재길이가 length인데 10짜리 붙여보고, 20짜리 두번 붙여보고
# 만약 현재길이가 목표하는 길이라면 하나 찾았다는 표시를 할거
# 20짜리 붙이다가 목표하는 길이를 넘어간다면 무시

def solve2(length, N): # 동작방식은 dfs로 동작함
    # 가능한거 다 해보기
    # 현재 길이가 목표하는 길이와 같다면 cnt += 1, 종이 붙이기 중단
    # 현재 길이가 찾는 길이보다 더 길다면 끝냄
    global cnt

    if length == N:
        cnt += 1
        return
    elif length > N:
        return
    else: # 아직은 작다
        solve2(length+10,N)
        solve2(length+20,N)
        solve2(length+20,N)


def solve2(length, N): # 동작방식은 dfs로 동작함
    # 가능한거 다 해보기
    # 현재 길이가 목표하는 길이와 같다면 cnt += 1, 종이 붙이기 중단
    # 현재 길이가 찾는 길이보다 더 길다면 끝냄
    # global cnt 글로벌 안쓴다면

    if length == N:
        # return
        return 1 # 하나 찾았다
    elif length > N:
        # return
        return 0 # 못찾았다
    else: # 아직은 작다
        return solve2(length+10,N) + solve2(length+20,N) * 2

        
    

for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    # ret = solve1(N)
    ret = solve2(0, N)
    # print(f"#{tc} {ret}")
    print(f"#{tc} {ret}")