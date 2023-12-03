from collections import deque

places = [  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"] ]
ret = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]


def bfs(y,x,place):
    q = deque()
    q.append([y,x,0])
    v = [[0]*5 for _ in range(5)]
    v[y][x] = 1
    while q:
        y,x,count = q.popleft()
        for k in range(4):
            ny = dy[k]+y
            nx = dx[k]+x
            if 0<=ny<5 and 0<=nx<5:
                if place[ny][nx] == '0' and count <= 2 and not v[ny][nx]:
                    v[ny][nx] = 1
                    q.append([ny,nx, count+1])
                elif place[ny][nx] == 'P':
                    return 0
    return 1

def solve(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                result = bfs(i,j,place)
                if result == 0:
                    return 0
    return 1


def solution(places):
    for place in places:
        result = solve(place)
        ret.append(result)
    return ret
        
print(solution(places))