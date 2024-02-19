N, M = map(int, input().split())

alpha = list(input().split())
alphaha =  sorted(alpha)
v = [0] * (M+1)
chk = [x for x in range(ord('a')-1, ord('z'))]

chk1 = []
chk2 = []
for c in chk:
    if chr(c) in ['a','e','i','o','u']:
        chk1.append(chr(c))
    else:
        chk2.append(chr(c))

def check_alpha(chk_alpha):
    cnt1 = 0
    cnt2 = 0
    for i in chk_alpha:
        if i in chk1:
            cnt1 += 1
        else:
            cnt2 += 1
    if (cnt1 >= 1 and cnt2 >= 2):
        return True
    return False
    



def solve(idx, end, target, result):
    if len(result) == target:
        chk = check_alpha(result)
        if (chk):
            print(''.join(result))
        return

    if idx == end:
        if target == len(result):
            chk = check_alpha(result)
            if (chk):
                print(''.join(result))
        return
    solve(idx+1, end, target, result+[alphaha[idx]])
    solve(idx+1, end, target, result)

solve(0, M, N, [])