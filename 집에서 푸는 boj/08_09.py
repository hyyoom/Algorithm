# 재귀로 조합? 만들기
arr = [1,2,3,4,5]
N = 5
M = 3 # 조합 요소의 갯수
selected = [0] * N # 조합에 포함 될건지 말건지


# idx번째 요소가 조합에 포함될건지 말건지 결정하는 함수
def comb(idx,cnt):
    if cnt == M:
        print(selected)
        return

    if idx == N: #마지막 인덱스 까지 확인했는데, 원하는 만큼 선택 못함
        return
    for i in range(2):
        selected[idx] = i
        comb(idx+1, cnt+1)
        selected[idx] = 0

    # 위와 같은 코드
    # selected[idx] = 0
    # comb(idx + 1, cnt)
    # selected[idx] = 1
    # comb(idx+1, cnt+1)
comb(0,0)