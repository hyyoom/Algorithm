
# def solve(S,G): # 시작에서 순회하다 G만나면 길찾기 성공
#     visited = [0] * V+1 # 방문 표시
#     st = [S]
#     visited[S] = 1
#     while st:
#         cur = st[-1]
#         if cur == G:
#             return 1
#         # cur 에서 갈수있는 경로 모두 살펴보기
#         for i in range(V+1):
#             # 현재노드에서 갈수 있는 길이 있고, 방문하지 않았다면 방문
#             if node[cur][i] and not visited[i]:
#                 st.append(i)
#                 visited[i] = 1
#                 break
#         else:   # 반복동안 break에 한번도 안걸렸으면(for else 구문)
#                 # 길 못찾았으면 이라는 뜻
#             st.pop() # 경로상에서 현재위치 제거
#         # 이 위치가 실행되는건 반복문 내에서 return이 안걸렸다는 뜻
#         # 그것의 의미는 목적지 가는 길을 못 찾은것
#             return 0


def solve(cur, visited): # 현재 위치를 인자로 받아서 그 위치에서 갈 수 있는 길을 다 찾아봄
    if cur == G:
        return 1 # 찾았다
    visited[cur] = 1
    for i in range(V+1):
        if node[cur][i] and not visited[i]:
            if solve(i, visited): #return 1을 받았다. 길이 있다
                return 1 # 나도 상위 노드에 길 있다고 알려줘야지
    return 0 


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # V 정점 갯수 E 개줄

    node = [[0] * (V+1) for _ in range(V+1)]
    # node = [set() * (V+1) for _ in range(V+1)]

    for _ in range(E):
        a,b = map(int,input().split())
        # node[a][b] = 1
        node[a].append(b)
    for i in node:
        print(i)
    S,G = map(int,input().split())
    
    # print(f"#{tc} {solve(S,G)}")
    print(f"#{tc} {solve(S,[0] * (V+1))}")