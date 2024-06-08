def lineup(n, info):
    # 줄을 서는 순서를 저장할 리스트, 처음에는 모두 0으로 채운다.
    result = [0] * n
    
    # 키가 작은 사람부터 큰 사람까지 순서대로 배치
    for i in range(1, n + 1):
        count = info[i - 1]
        spaces = 0
        
        for j in range(n):
            if result[j] == 0:
                if spaces == count:
                    result[j] = i
                    break
                spaces += 1
    
    return result

# 입력 받기
N = int(input())
info = list(map(int, input().split()))

# 줄 세우기
result = lineup(N, info)

# 결과 출력
print(' '.join(map(str, result)))
