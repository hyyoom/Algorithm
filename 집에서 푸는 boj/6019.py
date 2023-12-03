T = int(input())

for tc in range(1, T+1):
    D,A,B,F = map(int, input().split())

    time = D/(A+B)

    Fly = F * time
    #
    # time_m_fly = F/60
    # time_m = (A+B)/60 # 기차가 1분에 서로 얼마나 다가오는지..
    # cnt_mini = 0
    # while D >= 0:
    #     D -= time_m
    #     cnt_mini += 1
    #
    # Fly += time_m_fly * cnt_mini
    print(f"#{tc} {Fly:.10f}")