T = int(input())

for tc in range(1,T+1):
    N = int(input())

    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0
    if N % 2 == 0:
        while N%2 == 0:
            N//=2
            cnt_2 += 1
    if N % 3 == 0:
        while N%3 == 0:
            N//=3
            cnt_3 += 1
    if N % 5 == 0:
        while N%5 == 0:
            N//=5
            cnt_5 += 1
    if N % 7 == 0:
        while N%7 == 0:
            N//=7
            cnt_7 += 1
    if N % 11 == 0:
        while N%11 == 0:
            N//=11
            cnt_11 += 1
    print(f"#{tc} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}")