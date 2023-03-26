# [문제]
# 게임캐릭터가움직일수있는범위가있으며, 이제한된구역을넘어가지않도록검사하는함수를만들려고한다.
# 캐릭터는2차원평면(N * N)에서이동하며, 사용자의키입력에따라위, 아래, 왼쪽, 오른쪽으로한칸씩움직일수있다.
# 2차원평면은list의내부요소가list인형태를의미한다.캐릭터의현재위치는튜플(x, y) 형태로주어지며, x와y는각각2차원평면에서의행과열을의미한다.
# (0 <= x < 100, 0 <= y < 100)최대범위는숫자N으로주어진다. 
# (0 < N <= 100)키입력은0부터3까지의숫자M으로주어지며, 각각위, 아래, 왼쪽, 오른쪽방향으로한칸이동을의미한다.
# 만약, 키입력의결과로2차원평면범위를벗어난다면False, 그렇지않으면True를반환하는함수is_position_safe를완성하시오. 
# (반환되는값True와False는bool 자료형이다.)

# [문제풀이]
# 1. 방향은 입력값 M 0,1,2,3으로 각 위 아래 왼 오에 대입된다.
# 2. 따라서 M을 0으로 받으면 (a,b)에서 (a-1,b)가 되도록하는 if문을 구성하면된다.
# 3. 현재 주어진 것에서 최대크기는 N 여기선 3. (0,0)~(2,2)로 구성되어있고 넘어가면 False가 나오게 한다.
# 4. position으로 현재 위치를 알려주므로 거기서 + - 를 이루어져 맞는지 틀린지 확인하면 된다.
# 4-1. position 은 (ㅁ,ㄴ)의 튜플이므로 position[0] position[1]로 x축과 y축을 사용할 수 있다.

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    position = list(position)  # 튜플로는 position부분이 행하려는 방법으로 제대로 처리가 되지 않아 list형으로 변환
    if M == 0:  #위
        position[0] = position[0]-1
    elif M == 1:    #아래
        position[0] = position[0]+1
    elif M == 2:    #왼쪽
        position[1] = position[1]-1
    elif M == 3:    #오른쪽
        position[1] = position[1]+1
    
    if 0 <= position[0] and position [1] <= N-1:    # 행렬을 넘어가지 않을시
        return True
    else:                                           # 행렬을 넘어갈 시
        return False




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
