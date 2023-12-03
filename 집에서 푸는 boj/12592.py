T = int(input())

for tc in range(1, T+1):
    str1 = list(input().strip())
    str2 = list(input().strip())
    dic = {}
    dic2 = {}
    for i in str2:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    ret1 = []
    ret2 = []
    for i in str1:
        if i in dic:
            ret1.append(i)
            ret2.append(dic[i])
    ret_dic = dict(zip(ret1, ret2))
    lst = ret_dic.values()
    print(f"#{tc} {max(lst)}")
    