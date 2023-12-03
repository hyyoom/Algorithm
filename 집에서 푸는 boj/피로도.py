k = 80	
dungeons = [[80,20],[50,40],[30,10]]
v = [0]*len(dungeons)
answer = []
maxv = -1


def perm(idx, target,result,dungeons,k):
    global maxv
    
    if idx == target:
        cnt = 0
        for i in range(len(result)):
            if k >= result[i][0]:
                k-= result[i][1]
                cnt += 1
            else:
                break
        if maxv < cnt:
            maxv = cnt
        return
    for i in range(target):
        if not v[i]:
            v[i] = 1
            perm(idx+1,target,result+[dungeons[i]],dungeons,k)
            v[i] = 0    
        
    

def solution(k, dungeons):
    answer = []
    # dungeons = [1,2,3]
    perm(0,len(dungeons),[],dungeons,k)
    
    return maxv

# solution(k, dungeons)
# print(answer)