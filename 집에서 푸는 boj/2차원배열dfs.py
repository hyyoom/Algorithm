arr = [ # 0,0에서 시작해서 2로 나갈수 있냐 없냐..
    [1,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,1,1],
    [0,0,0,0,2],
]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N = 5

# def dfs():
#     # 방문 표시 배열
#     # (0, 0) 노드 시작점으로
#     st = [(0,0)]
#     v = [[0] * N for _ in range(N)]
#     v[0][0] = 1
#     # 현재 위치에서 갈 수 있는길 찾아보기 >> 반복
#     while st:
#         y, x = st[-1]
#         # 갈수 있는 경로 모두 탐색해보기
#         if arr[y][x] == 2:
#             return 1
#         for i in range(4):
#             ny = dy[i] + y
#             nx = dx[i] + x
#             if 0<=ny<N and 0<=nx<N and not v[ny][nx] and arr[ny][nx] != 0:
#                 st.append((ny,nx))
#                 v[ny][nx] = 1
#                 break
#         else: # 네군대 중 아무곳도 길이 없다면.
#             st.pop()
#     return 0

def dfs():
    # 방문 표시 배열
    # (0, 0) 노드 시작점으로
    st = [(0,0)]
    v = [[0] * N for _ in range(N)]
    v[0][0] = 1
    # 현재 위치에서 갈 수 있는길 찾아보기 >> 반복
    while st:
        y, x = st.pop()
        # 갈수 있는 경로 모두 탐색해보기
        if arr[y][x] == 2:
            return 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and not v[ny][nx] and arr[ny][nx] != 0:
                st.append((ny,nx))
                v[ny][nx] = 1
    return 0


print(dfs())