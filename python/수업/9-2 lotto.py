# {"totSellamnt":108444724000,"returnValue":"success","drwNoDate":"2023-01-07","firstWinamnt":1727810100,"drwtNo6":37,"drwtNo4":20,"firstPrzwnerCo":15,"drwtNo5":21,"bnusNo":17,"firstAccumamnt":25917151500,"drwNo":1049,"drwtNo2":5,"drwtNo3":13,"drwtNo1":3}
# https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049

# 1049회 1등 번호를 가져와서
# 10회 랜덤한 로또번호 생성 후
# 등 수 출력하기


# 같은 작업을 10회 반복하기
# for e in range(10):
#     여기 코드 부분이 10회 반복
#     이 부분에서 랜덤한 로또 코드 뽑아서 당첨번호를 확인하면 됩니다.
#     출력까지 하면 됩니다.


# 1. 1049회 1등 번호를 가져와서
# 2. 랜덤한 로또번호 생성
# 3. 생성한 번호들 중 몇개가 당첨번호와 일치하는지 개수세기
#   3-1 생성한 번호들 중 첫 번재 요소가 당첨번호와 일치하는지 비교 후 같으면 숫자 올려주기
#   3-1 생성한 번호들 중 첫 번재 요소가 당첨번호와 일치하는지 비교
#   3-1 생성한 번호들 중 첫 번재 요소가 당첨번호와 일치하는지 비교
#   3-1 생성한 번호들 중 첫 번재 요소가 당첨번호와 일치하는지 비교
#   3-1 생성한 번호들 중 첫 번재 요소가 당첨번호와 일치하는지 비교
#   3-1 생성한 번호들 중 첫 번재 요소가 당첨번호와 일치하는지 비교
# 4. 개수에 따른 등수 출력하기
# 5. 2~4번까지 작업을 총 10회 반복한다.

# 1049회 1등 당첨번호 가져오기
import random
import json
import requests



lotto_json=requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').text
lotto_dict = json.loads(lotto_json)
# drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6,bnusNo
win_number = []
for i in range(1,7):
    win_number.append(lotto_dict[f'drwtNo{i}'])
print(win_number)
# 임의의 로또 번호 생성하기 *10
for _ in range(10):     #나는 뭐 변수는 사용안할거다 언더바 사용
    my_number=random.sample(range(1,46),6)
    #생성한 번호들 중 몇 개가 당첨번호와 일치하는지 개수세기
    cnt = 0 # 몇 개 맞았는지 개수를 세기 위한 변수 선언
    # my_number의 첫 번째 요소부터 마지막 요소까지 맞는지 검사하기
    is_bonus = False
    for e in my_number:
        #e가 당첨번호에 포함되어 있으면, 맞은 개수(cnt)를 증가.
        
        # for n in win_num:
        #     if e==n:
        #         cnt+=1
        if e in win_number: # in 이라는 연산자가 반복문을 대신 돌아줌
            cnt +=1
        else:
            if e== lotto_dict['bnusNo']:
                #보너스 맞았음!
                is_bonus = True

    # 랜덤하게 생성된 번호의 맞은 개수세기 종료
    print(f'맞은 개수: {cnt}',end = ' ')    # end =' '를 쓰면 넘어가야할게 한 줄로 나옴
    if cnt ==3:
        print('5등 당첨!')
    elif cnt ==4:
        print('4등 당첨!')
    elif cnt ==5:
        if is_bonus ==True:
            print('2등 당첨!')    
        else:
            print('3등 당첨!')

    elif cnt ==6:
        print('1등 당첨!')
    else:
        print('낙첨되었습니다.')