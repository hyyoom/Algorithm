# 원래값에서 0으로 채워지지 않은 곳부터 시작 -> 그곳부터 다 1로 바꿈
# 1로 바꾼 뒤의 값부터 어느 부분이 원래의 값과 다른지 보기
# 원래의 값과 다르다면 반대로 바꿈
# 반복

T = int(input())
for tc in range(1, T+1):
    bit = list(map(int,input().strip()))
    lens_bit = len(bit)

    cnt = 0
    make_bit = [0] * lens_bit
    for i in range(len(make_bit)):
        if make_bit[i] != bit[i]:
            idx_first = i + 1
            for j in range(i,len(make_bit)):
                make_bit[j] = 1
            cnt = 1
            break

    for i in range(idx_first, len(make_bit)):
        if make_bit[i] != bit[i]:
            if bit[i] == 1:
                cnt += 1
                for j in range(i, len(make_bit)):
                    make_bit[j] = 1
            elif bit[i] == 0:
                cnt += 1
                for j in range(i, len(make_bit)):
                    make_bit[j] = 0
    print(f"#{tc} {cnt}")
    
    
    