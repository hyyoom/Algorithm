record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]



def solution(record):
    dic = {}
    for re in record:
        if re[0] == "E" or re[0] == "C":
            status, user_id, name = re.split()
        elif re[0] == "L":
            status, user_id = re.split()
        if status == "Enter":
            dic[user_id] = name
        elif status == "Change":
            dic[user_id] = name
        # else:
        #     if status == "Change":
        #         dic[user_id] = name
    
    # for re in record:
    #     status, user_id, name = re.split()

    result = []

    for re in record:
        if re[0] == "E" or re[0] == "C":
            status, user_id, name = re.split()
        elif re[0] == "L":
            status, user_id = re.split()
        if status == "Enter":
            tmp = dic[user_id] + "님이 들어왔습니다."
            result.append(tmp)
        if status == "Leave":
            tmp = dic[user_id] + "님이 나갔습니다."
            result.append(tmp)
    return result

print(solution(record))

    