# 1. target 위치 확인
# 2. 타깃에서 가장 가까운 홀 확인
# 3. 홀에서 target 각도 확인
# 4. target 공을 치기 위한 각도 확인

# import math

# start = (63,63)
# end = (0, 63)
# # (0,0) (127,127)
# a= abs(end[0]-start[0]) # x좌표 차이
# b= abs(end[1]-start[1]) # y좌표 차이

# # r은 거리 두 공 사이의 거리
# r = math.sqrt(a**2 + b**2)

# # 아크탄젠트는 math.atan함수를 이용하면 계산할 수 있음
# # math.atan의 결과는 radian으로 나옴(degree가 아님)
# radian = math.atan(b/a)

# # radian을 degree로 변경을 해야 실제 각도를 얻을 수 있음
# print(r, radian, math.degrees(radian))

# import math

# def get_num():
#     x1 = int(input())
#     y1 = int(input())
#     x2 = int(input())
#     y2 = int(input())
#     return[x1,y1,x2,y2]

# def cal_rad(arr):
#     rad = math.atan2(arr[3]-arr[1],arr[2]-arr[0])
#     return rad

# def radTodeg(rad):
#     PI = math.pi
#     deg = math.degrees(rad)
#     print("{0:0.2f}".format(deg))

# arr = get_num()
# rad = cal_rad(arr)
# radTodeg(rad)

import math

my_ball = (127,127)
target_ball = (154, 100)
goal = [(0,0),(254,0),(0,127),(254,127)]
goal_up_down = [(127,0),(127,127)]
diameter = 5.73
r = 5.73/2


for i in range(4):
    # target_ball 좌상에 위치할 때
    if target_ball[0]<my_ball[0] and target_ball[1]<my_ball[1] and goal[i] == (0,0):
        x = abs(my_ball[0]-goal[i][0])
        y = abs(my_ball[1]-goal[i][1])
        x_t = abs(target_ball[0]-goal[i][1])
        y_t = abs(target_ball[0]-goal[i][1])
        m_tx = abs(my_ball[0]-target_ball[0])
        m_ty = abs(my_ball[1]-target_ball[1])
        a = math.sqrt(x**2 + y**2)                      # goal과 내 공의 거리
        b = math.sqrt(x_t**2 + y_t**2)                  # goal과 타겟의 거리
        c = math.sqrt(m_tx**2 + m_ty**2)                # 내 공과 타겟의 거리
        deg1 = math.atan2(y,x)                          # goal과 내 공의 각도(라디안 값)
        deg2 = math.acos((a**2 + b**2 - c**2)/2*a*b)    # 내 공, goal, 타겟의 각도(라디안 값)
        d = math.sqrt((a**2 * math.sin(deg2))**2 + (b+diameter) -(a*math.sin(deg2))**2) # 공을 치게 될 각도
        deg3 = math.acos((a**2 + d**2 - (b+diameter)**2)/2*a*d)                         # goal, 내 공, 타겟의 각도(라디안 값)
        find_deg = deg1 + deg3
        fianl_deg = math.degrees(find_deg)              # degree값으로 변환한 최종 각도
    
    # target_ball 우상에 위치할 때
    elif target_ball[0]>=my_ball[0] and target_ball[1]<=my_ball[1] and goal[i] == (254,0):
        x = abs(my_ball[0]-goal[i][0])
        y = abs(my_ball[1]-goal[i][1])
        x_t = abs(target_ball[0]-goal[i][1])
        y_t = abs(target_ball[0]-goal[i][1])
        m_tx = abs(my_ball[0]-target_ball[0])
        m_ty = abs(my_ball[1]-target_ball[1])
        a = round(math.sqrt(x**2 + y**2),2)                      # goal과 내 공의 거리
        b = round(math.sqrt(x_t**2 + y_t**2),2)                  # goal과 타겟의 거리
        c = round(math.sqrt(m_tx**2 + m_ty**2),2)                # 내 공과 타겟의 거리
        deg1 = math.atan2(y,x)                          # goal과 내 공의 각도(라디안 값)
        deg1_deg = math.degrees(deg1)
        k=(a**2 + b**2 - c**2)/(2*a*b)
        deg2 = math.acos(k)    # 내 공, goal, 타겟의 각도(라디안 값)
        print(deg2, math.degrees(deg2))
        # d = math.sqrt((a**2 * math.sin(deg2))**2 + (b+diameter) -(a*math.sin(deg2))**2) # 공을 치게 될 각도
        l = a**2 + (b+diameter)**2 - 2*a(b+diameter)*math.cos(deg2)
        d = math.sqrt(l) # 공을 치게 될 각도
        deg3 = math.acos((a**2 + d**2 - (b+diameter)**2)/2*a*d)                         # goal, 내 공, 타겟의 각도(라디안 값)
        find_deg = deg1 + deg3
        fianl_deg = math.degrees(find_deg)              # degree값으로 변환한 최종 각도

    # target_ball 좌하에 위치할 때
    elif target_ball[0]<my_ball[0] and target_ball[1]>my_ball[1] and goal[i] == (0,127):
        x = abs(my_ball[0]-goal[i][0])
        y = abs(my_ball[1]-goal[i][1])
        x_t = abs(target_ball[0]-goal[i][1])
        y_t = abs(target_ball[0]-goal[i][1])
        m_tx = abs(my_ball[0]-target_ball[0])
        m_ty = abs(my_ball[1]-target_ball[1])
        a = math.sqrt(x**2 + y**2)                      # goal과 내 공의 거리
        b = math.sqrt(x_t**2 + y_t**2)                  # goal과 타겟의 거리
        c = math.sqrt(m_tx**2 + m_ty**2)                # 내 공과 타겟의 거리
        deg1 = math.atan2(y,x)                          # goal과 내 공의 각도(라디안 값)
        deg2 = math.acos((a**2 + b**2 - c**2)/2*a*b)    # 내 공, goal, 타겟의 각도(라디안 값)
        d = math.sqrt((a**2 * math.sin(deg2))**2 + (b+diameter) -(a*math.sin(deg2))**2) # 공을 치게 될 각도
        deg3 = math.acos((a**2 + d**2 - (b+diameter)**2)/2*a*d)                         # goal, 내 공, 타겟의 각도(라디안 값)
        find_deg = deg1 + deg3
        fianl_deg = math.degrees(find_deg)              # degree값으로 변환한 최종 각도
    
    # target_ball 우하에 위치할 때
    elif target_ball[0]>my_ball[0] and target_ball[1]>my_ball[1] and goal[i] == (254,127):
        x = abs(my_ball[0]-goal[i][0])
        y = abs(my_ball[1]-goal[i][1])
        x_t = abs(target_ball[0]-goal[i][1])
        y_t = abs(target_ball[0]-goal[i][1])
        m_tx = abs(my_ball[0]-target_ball[0])
        m_ty = abs(my_ball[1]-target_ball[1])
        a = math.sqrt(x**2 + y**2)                      # goal과 내 공의 거리
        b = math.sqrt(x_t**2 + y_t**2)                  # goal과 타겟의 거리
        c = math.sqrt(m_tx**2 + m_ty**2)                # 내 공과 타겟의 거리
        deg1 = math.atan2(y,x)                          # goal과 내 공의 각도(라디안 값)
        deg2 = math.acos((a**2 + b**2 - c**2)/2*a*b)    # 내 공, goal, 타겟의 각도(라디안 값)
        d = math.sqrt((a**2 * math.sin(deg2))**2 + (b+diameter) -(a*math.sin(deg2))**2) # 공을 치게 될 각도
        deg3 = math.acos((a**2 + d**2 - (b+diameter)**2)/2*a*d)                         # goal, 내 공, 타겟의 각도(라디안 값)
        find_deg = deg1 + deg3
        fianl_deg = math.degrees(find_deg)              # degree값으로 변환한 최종 각도


# target_ball 바로 상에 위치할 때
if target_ball[0]==my_ball[0] and target_ball[1]<my_ball[1]:
    pass
# target_ball 바로 하에 위치할 때
if target_ball[0]==my_ball[0] and target_ball[1]>my_ball[1]:
    pass