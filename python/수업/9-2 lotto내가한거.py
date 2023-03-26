# {"totSellamnt":108444724000,"returnValue":"success","drwNoDate":"2023-01-07","firstWinamnt":1727810100,"drwtNo6":37,"drwtNo4":20,"firstPrzwnerCo":15,"drwtNo5":21,"bnusNo":17,"firstAccumamnt":25917151500,"drwNo":1049,"drwtNo2":5,"drwtNo3":13,"drwtNo1":3}
# 1049회 1등 번호를 가져와서
# 10회 랜덤한 로또번호 생성 후
# 등 수 출력하기


# 같은 작업을 10회 반복하기
# for e in range(10):
#     여기 코드 부분이 10회 반복
#     이 부분에서 랜덤한 로또 코드 뽑아서 당첨번호를 확인하면 됩니다.
#     출력까지 하면 됩니다.
'''
import random
e=random.sample(range(1,46),6)
for e in range(10):
    print(random.sample(range(1,46),6))
'''
# 1049회차 로또번호 확인
import json
import requests
get_num=requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').text
# print(get_num)
json_dict = json.loads(get_num)
win_num_bonus=[json_dict["drwtNo1"], json_dict["drwtNo2"], json_dict["drwtNo3"], json_dict["drwtNo4"], json_dict["drwtNo5"], json_dict["drwtNo6"], json_dict["bnusNo"]] #당첨번호(보너스)
win_num=[json_dict["drwtNo1"], json_dict["drwtNo2"], json_dict["drwtNo3"], json_dict["drwtNo4"], json_dict["drwtNo5"], json_dict["drwtNo6"]] #찐 당첨번호
print(win_num)
# print(json_dict)
print(f'당첨번호는 {json_dict["drwtNo1"]}, {json_dict["drwtNo2"]}, {json_dict["drwtNo3"]}, {json_dict["drwtNo4"]}, {json_dict["drwtNo5"]}, {json_dict["drwtNo6"]}, 보너스 번호는 {json_dict["bnusNo"]}입니다.')# 당첨번호 알랴줌
# # print(type(json_dict))

# 로또번호 생성 및 로또번호 비교
import random
for e in range(1, 11):
    my_num=random.sample(range(1,46),6) #로또 자동 생성기
    print(e,'번 생성기', my_num)
    my_num_set = set(my_num)
    win_num_set = set(win_num)
    win_num_bonus_set = set(win_num_bonus)
    win_intersection = my_num_set & win_num_set
    win_intersection_bonus = my_num_set & win_num_bonus_set
    if len(win_intersection) == 0:      # 어? 이게 되네????????
        print("하나도 못 맞췄습니다ㅠㅠ")
        print("-----")
        print("-----")
    else:
        print(sorted(list(win_intersection)))
        if len(win_intersection) == 1:
            print('1개라니.. 아쉽습니다.')
        if len(win_intersection) == 2:
            print('2개라니.. 한개 만 더 맞았으면ㅠㅠ 아쉽습니다.')
        if len(win_intersection) == 3:
            print('3개! 5등 축하합니다!')
        if len(win_intersection) == 4:
            print('4개! 4등 축하합니다!')
        if len(win_intersection) == 5:
            print('5개! 와우!!! 3등 축하합니다!')
        if len(win_intersection_bonus) == 6:
            if len(win_intersection) == 6:
                print('6개! 1등 100억원의 주인공은 당신!!! 축하합니다!!!')
            elif len(win_intersection_bonus) == 6:
                print('와우!!! 2등이라니! 정말 축하합니다!')
        if len(win_intersection) == 6:
            print('6개 실화냐? 1등 100억원의 주인공은 당신!!! 축하합니다!!!')
        print("-----")
        print("-----")