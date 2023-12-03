# 가로 첫줄에 있는 1의 인덱스를 저장해서 출발점으로 저장함
# i만 +하면서 진행
# 2를 만난다면 return 해당 x위치
# 만약 진행 중 J+1 혹은 J-1에 1이 있다면 없을때까지 진행
# 진행후 continue를 통해 다음 반복문으로 진행
# import sys
# sys.stdin = open("c:/Users/SSAFY/Desktop/algorithm/swea/input.txt", "r")

def find_x(j,maps,ret):

    i = 0
    while i < 100:
        if j + 1 < 100 and maps[i][j+1] == 1:
            while True:
                if j+1<100 and maps[i][j+1] == 1:
                    j+=1
                else:
                    break
        elif j - 1 >= 0 and maps[i][j-1] == 1:
            while True:
                if j - 1 >= 0 and maps[i][j-1] == 1:
                    j-=1
                else:
                    break
        if maps[i][j] == 2:
            return ret
        i+=1
    return -1
            

for _ in range(10):
    T = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]
    x_start = []
    ret = 0
    for j in range(100):
        if maps[0][j] == 1:
            ret = find_x(j,maps,j)
            if ret != -1:
                print(f"#{T} {ret}")
    # print(find_x(0,maps,0))