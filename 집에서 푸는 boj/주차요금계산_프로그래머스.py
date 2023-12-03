# 입차 보고 바로 출차 딕셔너리로.
# 공식 5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600 기본시간 이상이면 이 공식 활용
import math

def how_much(h_in, m_in, h_out, m_out):
    ret = 0
    
    if m_in > m_out:
        hour = h_out - h_in -1
        minute = (60 - m_in) + m_out
        if minute >= 60:
            hour += 1
            minute -= 60
    elif m_in < m_out:
        # 05:35 07:45
        hour = h_out - h_in
        minute = m_out - m_in
    else:
        hour = h_out - h_in
        minute = 0
    
    ret = (hour*60) + minute
    return ret

# def two_four(car, dic):
#     if car in dic:
#         h_in = int(dic[car][0][:2])
#         m_in = int(dic[car][0][3:])
#         tmp = how_much(h_in, m_in, 24, 59)
#         result.append(tmp)

result = []
def solution(fees, records):
    answer = []
    car_in_data = []
    
    dic = {}
    tmp = {}
    car_data = []
    for record in records:
        time, car_num, in_out = record.split()
        if in_out == "IN" and car_num not in car_in_data:
            car_in_data.append(car_num)
        
        if car_num not in car_data:
            car_data.append(car_num)
        if car_num not in dic:
            dic[car_num] = [time, in_out]
        elif car_num in dic:
            hour_in, minute_in = dic[car_num][0].split(":")
            hour_in = int(hour_in)
            minute_in = int(minute_in)
            hour_out = int(time[:2])
            minute_out = int(time[3:])
            # in과 out 시간 모두 구함.
            # 공식 5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600
            cal = how_much(hour_in,minute_in, hour_out,minute_out) # tmp == 분으로 환산한 시간
            if car_num not in tmp:
                tmp[car_num] = cal
            elif car_num in tmp:
                tmp[car_num] += cal
            del dic[car_num] # 출차했으면 없애주기
    
    for car in car_data:
        if car in dic:
            h_in = int(dic[car][0][:2])
            m_in = int(dic[car][0][3:])
            if tmp == {}:
                dont_out_car = how_much(h_in, m_in, 23, 59)
                tmp[car] = dont_out_car
            else:
                dont_out_car = how_much(h_in, m_in, 23, 59)
                if car in tmp:
                    tmp[car] += dont_out_car
                else:
                    tmp = dont_out_car
            

    car_in_data.sort()
    for car in car_in_data:
        if car in tmp:
            if tmp[car] <= fees[0]:
                result.append(fees[1])
            elif tmp[car] > fees[0]:
                ceils = math.ceil((tmp[car] - fees[0]) / fees[2])
                cal_how_much = (ceils * fees[3]) + fees[1]
                result.append(cal_how_much)
    
    return result

fees= [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))