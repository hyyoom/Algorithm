# SWA_16910. 원 안의 점
T = int(input())

for tc in range(1, T+1):
    r = int(input())
    point = 0

    for i in range(1, r+1):            # 1개의 분면에 들어가는 격자점 수
        for j in range(1, r+1):
            if i**2 + j**2 <= r**2:
                point += 1
    point += r   # 한 축의 격자점 수

    point *= 4   # 4사분면 + 4개의 축 격자점 갯수
    point += 1   # 원점
    print(f'#{tc} {point}')