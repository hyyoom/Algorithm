import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    for i in range(len(mbti)):
        mbti[i] = list(mbti[i])
    
    set1 = set()
    ret = []
    for i in range(len(mbti)-2):
        tmp = 0
        set1 = set()
        for j in range(4):
            set1.add(mbti[i][j])
            set1.add(mbti[i+1][j])
        tmp += len(set1)
        set1 = set()
        for k in range(4):
            set1.add(mbti[i+1][j])
            set1.add(mbti[i+2][j])
        tmp += len(set1)
        set1 = set()
        for l in range(4):
            set1.add(mbti[i][l])
            set1.add(mbti[i+2][l])
        tmp += len(set1)
        ret.append(tmp)
    
    print(ret)
        
