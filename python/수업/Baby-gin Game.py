#122313
# 모든 순서 다 바꾸기
# 앞 절반 뒤 절반 run, triplet 검사하기
# 순서는 어떻게 바꾸지???
# 세 개 짜리로 한 번 바꿔 봅시다.
# 0 1 2가 있다고 가정 첫번째 위치 0 두번째 위치에도 0 세번째 위치에도 0이 가능
# 1과 2도 그럼
# 첫 번째 자리에 들어갈 수 있는 수
'''
for i in range(3): # 0,1,2 i: 첫번째 자리
    for j in range(3): # j: 두번째 자리
        if i == j:
            continue        # 나를 포함하고 있는 반복문의 다음 회차로 넘어감
        for k in range(3): # k: 세번째 자리
            if i == j or i == k or j == k :
                continue
            print(i, j, k)

arr = [5, 7, 6]
for i in range(3): # 0,1,2 i: 첫번째 자리
    for j in range(3): # j: 두번째 자리
        if i == j:
            continue        # 나를 포함하고 있는 반복문의 다음 회차로 넘어감
        for k in range(3): # k: 세번째 자리
            if i == j or i == k or j == k :
                continue
            print(arr[i], arr[j], arr[k])

arr = [5, 7, 6]
for i in range(3): # 0,1,2 i: 첫번째 자리
    for j in range(3): # j: 두번째 자리
        if i == j:
            continue        # 나를 포함하고 있는 반복문의 다음 회차로 넘어감
        for k in range(3): # k: 세번째 자리
            if i == j or i == k or j == k :
                continue
            print(arr[i], arr[j], arr[k], end='')
            if arr[i] == arr[j]-1 and arr[i] == arr[k]-2:
                print('run!')
            else:
                print()

arr = [6, 6, 6]
for i in range(3): # 0,1,2 i: 첫번째 자리
    for j in range(3): # j: 두번째 자리
        if i == j:
            continue        # 나를 포함하고 있는 반복문의 다음 회차로 넘어감
        for k in range(3): # k: 세번째 자리
            if i == j or i == k or j == k :
                continue
            print(arr[i], arr[j], arr[k], end='')
            if arr[i] == arr[j] and arr[i] == arr[k]:
                print('triplet')
            else:
                print()

'''
'''
arr = [2, 1, 3, 6, 5, 4]
for i in range(6): # 0,1,2 i: 첫번째 자리
    for j in range(6): # j: 두번째 자리
        if i == j:
            continue        # 나를 포함하고 있는 반복문의 다음 회차로 넘어감
        for k in range(6): # k: 세번째 자리
            if i == k or j == k :
                continue
            for a in range(6):
                if a == i or a == j or a == k:
                    continue
                for b in range(6):
                    if b == i or b == j or b == k or b ==a:
                        continue
                    for c in range(6):
                        if c == i or c == j or c == k or c == a or c ==b:
                            continue
                        # print(i,j,k,a,b,c)
                        # 앞쪽이 run/triplet이냐, 뒤쪽이 run/triplet이냐 확인하는 변수
                        run_cnt=0
                        triplet_cnt=0

                        if arr[i] == arr[j] - 1 and arr[i] == arr[k] - 2:
                            print('run!')
                            run_cnt += 1
                        elif arr[i] == arr[j] and arr[i] == arr[k]:
                            print('triplet!')
                            triplet_cnt += 1
                        # else:
                        #     print()

                        if arr[a] == arr[b] - 1 and arr[a] == arr[c] - 2:
                            print('run!')
                            run_cnt += 1
                        elif arr[a] == arr[b] and arr[a] == arr[c]:
                            print('triplet!')
                            triplet_cnt += 1
                        # else:
                        #     print()

                        if triplet_cnt + run_cnt == 2:
                            print('Baby-Gin!')
                            print(arr[i],arr[j],arr[k],arr[a],arr[b],arr[c])
'''

'''
arr = [9, 3, 4, 5, 9, 9]
# babygin을 찾으면 true 못찾으면 False
def check_babygin():
    for i in range(6): # 0,1,2 i: 첫번째 자리
        for j in range(6): # j: 두번째 자리
            if i == j:
                continue        # 나를 포함하고 있는 반복문의 다음 회차로 넘어감
            for k in range(6): # k: 세번째 자리
                if i == k or j == k :
                    continue
                for a in range(6):
                    if a == i or a == j or a == k:
                        continue
                    for b in range(6):
                        if b == i or b == j or b == k or b ==a:
                            continue
                        for c in range(6):
                            if c == i or c == j or c == k or c == a or c ==b:
                                continue
                            # print(i,j,k,a,b,c)
                            # 앞쪽이 run/triplet이냐, 뒤쪽이 run/triplet이냐 확인하는 변수
                            run_cnt=0
                            triplet_cnt=0
                            if arr[i] == arr[j] - 1 and arr[i] == arr[k] - 2:
                                # print('run!')
                                run_cnt += 1
                            elif arr[i] == arr[j] and arr[i] == arr[k]:
                                # print('triplet!')
                                triplet_cnt += 1
                            # else:
                            #     print()
                            if arr[a] == arr[b] - 1 and arr[a] == arr[c] - 2:
                                # print('run!')
                                run_cnt += 1
                            elif arr[a] == arr[b] and arr[a] == arr[c]:
                                # print('triplet!')
                                triplet_cnt += 1
                            # else:
                            #     print()
                            if triplet_cnt + run_cnt == 2:
                                print('Baby-Gin!')
                                print(arr[i],arr[j],arr[k],arr[a],arr[b],arr[c])
                                return True
    return False    # 첫번째 반복문이 끝나고 나면 False 이유는 중간에 찾으면 return True이니까

result = check_babygin()
if result:
    print('찾았다.')
else:
    print('없네?')
'''

# 숫자는 0~9니까
arr = [9,8,9,3,1,2]
count = [0] * 10
for i in range(len(arr)):
    count[arr[i]] += 1          # arr의 각 요소가 몇 개 있는지 확인

# 앞에서부터 보면서 run, triplet 검사하기
run_cnt = 0
tri_cnt = 0
i =0
while i < len(count):
# for i in range(len(count)):
    if count[i] >=3:            # triplet 임
        tri_cnt += 1
        count[i] -= 3
        i -= 1                  # 원래자리 한 번 더 검사하려고 뺌
    elif count[i] > 0:
        # if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
        # if count[i+1] > 0 and count[i+2] > 0:
        # ↓↓↓↓ 단축평가
        if i <= 7 and count[i+1] and count[i+2]:           # 자동으로 참 거짓이 나오기 때문 숫자가 있으면 Treu, 없으면 False
            run_cnt += 1
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            i -= 1
    i += 1

if run_cnt + tri_cnt == 2:
    print('baby gin!!!')
else:
    print('사쿠라네 사쿠라여!!!!')