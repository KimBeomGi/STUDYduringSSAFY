# 문제
# “반갑다. 내 이름은 반고흐#31555! 조선 최고의 활잡이지. 오늘도 난 금강산 위에서 적들을 노리고 있지. 내 앞에 있는 적들이라면 누구도 놓치지 않아! 좋아, 이제 곧 월식이 시작되는군. 월식이 시작되면 용이 적들을 집어삼킬 것이다. 잘 봐두어라! 마장동 활잡이 반고흐#31555님의 실력을-!”

# 반고흐#31555는 자기 뒤쪽 봉우리에 덩기#3958이 있음을 전혀 모르고 있었다. 덩기#3958도 반고흐#31555와 마찬가지로 월식이 시작되면 용을 불러내어 눈앞에 있는 다른 활잡이들을 모두 처치할 생각이다. 사실, 반고흐#31555와 덩기#3958 뿐만 아니라 금강 산맥의 N개 봉우리에 있는 모든 활잡이들이 같은 생각을 가지고 있다.

# 반고흐#31555가 있는 금강 산맥에는 총 N개의 봉우리가 있고, 모든 봉우리마다 한 명의 활잡이가 서서 월식이 시작되기만을 기다리고 있다. 다만, 애석하게도, 천계에 맥도날드가 생겨 용들이 살이 찐 탓에 용들은 자신보다 낮은 봉우리에 서있는 적들만 처치할 수 있게 되었다. 또한 용들은 처음 출발한 봉우리보다 높은 봉우리를 만나면 그대로 공격을 포기하고 금강산자락에 드러누워 낮잠을 청한다고 한다. 봉우리의 높이는 모두 다르고 모든 용들은 오른쪽으로만 나아가며, 중간에 방향을 틀거나, 봉우리가 무너지거나 솟아나는 경우는 없다.

# “달에 마구니가 끼었구나.”

# 드디어 월식이 시작됐다! 과연 이들 활잡이 중 최고의 활잡이는 누구일까? 최고의 활잡이가 최대 몇 명의 적을 처치할 수 있는지 알아보자.

# 입력
# 첫째 줄에 봉우리의 수 겸 활잡이의 수 N이 주어진다. (1 ≤ N ≤ 30,000) 둘째 줄에 N개 봉우리의 높이가 왼쪽 봉우리부터 순서대로 주어진다. (1 ≤ 높이 ≤ 100,000) 각각 봉우리의 높이는 중복 없이 유일하다.

# 출력
# 최고의 활잡이가 처치할 수 있는 적의 최대 숫자를 출력한다.


# 입력값
# 7
# 6 4 10 2 5 7 11
# 출력값
# 3

import sys

N = int(sys.stdin.readline().strip())
hills = list(map(int, sys.stdin.readline().strip().split()))         # 언덕 입력받기
max_killcount = 0
for i in range(N-1):                            # 0~N-2에 해당하는 인덱스만 확인하면됨
    kill_count = 0
    for j in range(i+1,N):                      # i요소가 해치울수 있는 값이 몇개 있는지 확인하기 위함.
        if hills[i] >= hills[j]:                # i가 j보다 크면 kill_count +1 해주기
            kill_count += 1
        else:                                   # 그렇지 않으면 용이 드러누워서 일 안하니까 그만확인
            break
    if max_killcount < kill_count:              # 최대 킬 수가 현재 킬수보다 작으면
        max_killcount = kill_count              # 최대 킬 수를 현재 킬수로 바꿔줌
print(max_killcount)




import sys

N = int(sys.stdin.readline().strip())
hills = list(map(int,sys.stdin.readline().strip().split())) # 언덕 입력받기
high_location = 0                   # 궁 발사 위치
kill_count = 0                      # kil_count
kills = []                          # 죽인 횟수들을 모음
for i in range(N):                  # 각 언덕마다 하나씩 궁수가 위치해있으니 이를 이용
  if hills[i] > high_location:      # i번째 언덕이 high_location보다 높으면
    high_location = hills[i]        # i번째 언덕이 제일 높은 위치가 됨
    kill_count = 0                  # 그리고 kill_count는 0으로 고정
  else:                             # 아니라면???
    kill_count += 1                 # 더 낮거나 같은 언덕이니 kill_count +1해주기
    kills.append(kill_count)        # 그리고 kill_count를 kills array에 입력해주기
                                    # else에 입력 이유는 이렇게 안하면, 더 높은 위치가 안나오면 append를 안해줌;;;;
print(max(kills))                   # 가장 큰 kill값을 출력