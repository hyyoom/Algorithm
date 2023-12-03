import sys
sys.stdin = open("c:/Users/SSAFY/Desktop/Ss_practice/algorithm/boj/input.txt", "r")

N,M = map(int, input().split())

r,c,d = map(int, input().split())
maps = [list(map(int ,input().split())) for _ in range(N)]

i = r
j = c
cnt = 0
chk = 0
flag = 0
c = [0,0,0,0]
flag2 = 0

while True:
    flag2 = 0 
    if i < 0 or i >= M or j < 0 and j >= M :
        break

    if 0<=i<N and 0<=j<M:
        if maps[i][j] == 0:
            maps[i][j] = 1
            cnt += 1
    
    if 0<=i-1<N or 0<=i+1<N or 0<=j-1<M or 0<=j+1<M:
        if 0<=i-1<N and 0<=j<M:
            chk += 1
            if maps[i-1][j] :
                flag +=1
        if 0<=i+1<N and 0<=j<M:
            chk += 1
            if maps[i+1][j] == 1:
                flag +=1
        if 0<=i<N and 0<=j-1<M:
            chk += 1
            if maps[i][j-1] == 1:
                flag +=1
        if 0<=i<N and 0<=j+1<M:
            chk += 1
            if maps[i][j+1] == 1:
                flag +=1
        if chk == flag:
            flag2 = 1
            if d == 0:
                i += 1
            if d == 1:
                j -= 1
            if d == 2:
                i -= 1
            if d == 3:
                j += 1
            if i < 0 or i >= M or j<0 and j>=M :
                break
        flag = 0
        chk = 0
    
    if 0<=i-1<N or 0<=i+1<N or 0<=j-1<M or 0<=j+1<M and flag2 == 0:
        if d == 0:
            d = 3
        else:
            d -= 1
        
        if d == 0 and 0<=i-1<N and 0<=j<M:
            if maps[i-1][j] == 0:
                i-=1
                continue
        if d == 1 and 0<=i<N and 0<=j+1<M:
            if maps[i][j+1] == 0:
                j+=1
                continue

        if d == 2 and 0<=i+1<N and 0<=j<M:
            if maps[i+1][j] == 0:
                i+=1
                continue

        if d == 3 and 0<=i<N and 0<=j-1<M:
            if maps[i][j-1] == 0:
                j-=1
                continue
    flag2 = 0

print(cnt)
        
        
        
        
        