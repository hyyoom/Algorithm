for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
  
    max_number = 0
    max_lst = []
    for r in range(len(arr)):
        sum_r = 0
        sum_y = 0
        sum_x = 0
        sum_c = 0
        for c in range(len(arr[r])):
            sum_r += arr[r][c]
            max_lst.append(sum_r)
            sum_c += arr[c][r]
            max_lst.append(sum_c)
            if r == c:
                sum_x += arr[r][c]
                max_lst.append(sum_x)
            if r+c == 99:
                sum_y = arr[r][c]
                max_lst.append(sum_y)
  
    for i in max_lst:
        if i > max_number:
            max_number = i
    print(f'#{tc} {max_number}')