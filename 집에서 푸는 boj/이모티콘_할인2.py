


users = [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900],
]
emoticons = [1300, 1500, 1600, 4900]

sale = [10, 20, 30, 40]
N = 5
max_plus = 0
emoji = []
buy = []
# 일정 금액 이상이면 이모티콘구매
# 일정 비율 이상이면 구매

def solve(tmp,users,emo):
    global max_plus
    global emoji
    toto = 0
    buy_emoji = 0
    for user in users:
        total = 0
        for i in range(len(tmp)):
            if tmp[i] >= user[0]:
                price = (100-tmp[i]) * emo[i]
                price = price / 100
                price = int(price)
                total+=price
        if total >= user[1]:
            buy_emoji += 1
            total = 0
        else:
            toto+=total
    if max_plus <= buy_emoji:
        max_plus = buy_emoji
        emoji.append([max_plus,toto])

def perm(idx, emolen, tmp,users,emoticons):
    if idx == emolen:
        solve(tmp,users, emoticons)
        return
    for i in range(4):
        tmp[idx] += sale[i]
        perm(idx + 1, emolen, tmp,users,emoticons)
        tmp[idx] -= sale[i]


def solution(users, emoticons):
    perm(0, len(emoticons), [0] * len(emoticons),users,emoticons)
    result = sorted(emoji, key=lambda x:(x[0],x[1]))
    return(result[len(result)-1])

