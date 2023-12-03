# 내 현재 위치에서 k만큼 더한 인덱스까지
# m이 위치해 있다면 충전. 대신 m중에 k의 끝 값과 가장 근접한 m을 충전
# 충전할때 cnt += 1
# 충전 했다면 idx를 m의 위치로 치환
# 충전했다면 flag = 1 아니면 0
# flag == 0 이면 print(0) break

T = int(input())
for tc in range(1,T+1):
    k, n, m = map(int,input().split())
    m_lst_tmp = list(map(int, input().split()))
    m_lst = [0] * (n+k+1)
    cnt = 0
    for i in range(len(m_lst_tmp)):
        m_lst[m_lst_tmp[i]] = 1

    i = 0
    j = 0
    point = 0
    tmp = 0
    while point < n:
        point = i+k
        tmp = point
        while tmp > i:
            if tmp >= n:
                point = 2000
                break
            if m_lst[tmp] == 1:
                cnt += 1
                i = tmp
                break
            elif tmp == i+1:
                cnt = 0
                point = 2000
                break
            tmp-=1

    print(f"#{tc} {cnt}")