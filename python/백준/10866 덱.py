# 문제
# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
import sys

N = int(sys.stdin.readline().strip())
deque = []
for _ in range(N):
    order = sys.stdin.readline().strip().split()
    o = order[0]
    if o == 'push_front':
        deque.insert(0, int(order[1]))
        pass
    elif o == 'push_back':
        deque.append(int(order[1]))
    elif o == 'pop_front':
        if not deque:                   # deque에 값이 없으면
            print(-1)                   # -1 출력
        else:                           # deque에 값이 있으면
            print(deque.pop(0))         # 가장 앞에 값 출력
    elif o == 'pop_back':
        if not deque:                   # deque에 값이 없으면
            print(-1)                   # -1 출력
        else:                           # deque에 값이 있으면
            print(deque.pop())          # 가장 뒤에 값 출력
    elif o == 'size':                   # deque에 들어있는 정수의 개수
        print(len(deque))               # len(deque)이용
    elif o == 'empty':
        if deque:                       # deque에 값이 있으면
            print(0)                    # 0을 출력
        else:                           # deque에 값이 없으면
            print(1)                    # 1을 출력
    elif o == 'front':
        if not deque:                   # deque에 값이 없으면
            print(-1)                   # -1을 출력
        else:                           # deque에 값이 있으면
            print(deque[0])             # deque의 가장 앞 값 출력
        
    elif o == 'back':
        if not deque:                   # deque에 값이 없으면
            print(-1)                   # -1을 출력
        else:                           # deque에 값이 있으면
            print(deque[-1])             # deque의 가장 뒷 값 출력



##################################
# 다른 사람이 푼 더 빠른 실행속도
import sys

deque = []

for i in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().strip()
    chk = x[:6:]

    if chk == 'push_f':
        deque = [x[11::]] + deque

    elif chk == 'push_b':
        deque.append(x[10::])

    elif x == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque = deque[1::]

    elif x == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif x == 'size':
        print(len(deque))

    elif x == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif x == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif x == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])