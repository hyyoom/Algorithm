import math

def calculate_shot(ball_position, target_position, pocket_positions, ball_radius, pocket_radius):
    x1, y1 = ball_position
    x2, y2 = target_position

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    angle = math.atan2(y2 - y1, x2 - x1)
    min_force = distance - ball_radius - pocket_radius

    if min_force < 0:
        min_force = 0  # 이미 포켓 안에 들어간 경우 세기를 0으로 설정합니다.

    # 포켓 구멍 위치를 기반으로 목적구를 넣을 수 있는지 확인합니다.
    for pocket_x, pocket_y in pocket_positions:
        pocket_distance = math.sqrt((pocket_x - x2)**2 + (pocket_y - y2)**2)
        if pocket_distance <= pocket_radius:
            return math.degrees(angle), min_force, (pocket_x, pocket_y)  # 목적구를 넣을 포켓 구멍의 좌표를 반환합니다.

    return None  # 넣을 수 있는 포켓을 찾지 못한 경우


ball_radius = 2.5  # 수구의 반지름
pocket_radius = 6.0  # 포켓 구멍의 반지름
ball_position = (10, 10)  # 수구의 위치 (x, y)
target_position = (20, 20)  # 목적구의 위치 (x, y)
pocket_positions = [(0, 0), (20, 0), (0, 20), (20, 20), (10, 0), (10, 20)]  # 포켓 구멍의 위치 리스트 [(x, y), ...]


# 수구로 목적구를 포켓에 넣을 수 있는 각도와 세기를 계산합니다.
result = calculate_shot(ball_position, target_position, pocket_positions, ball_radius, pocket_radius)

if result is not None:
    angle, force, pocket_position = result
    print(f"목적구를 {angle}도 각도로 최소 {force} 세기로 {pocket_position} 포켓에 넣으세요.")
else:
    print("목적구를 넣을 수 있는 포켓을 찾을 수 없습니다.")
