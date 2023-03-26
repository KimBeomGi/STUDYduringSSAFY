# # 문제
# 다음과 같이 tuple을 저장한 list가 있다. 각 tuple의 첫 번째 요소는 해야할 일, 두번째 요소는 남은 일 수이다.
# 새로운 일정울 입력받아 list에 추가하고 출력하라.

# todo = [("Python Homework", 3), ("Assay",4), ("Vacation", 100)]
# - 해야 할 일, 그리고 남은 일수까지 총 두 번 입력받는다.
# - 입력받은 해야 할 일과 남은 일수는 tuple로 묶는다.
# - 남은 일수는 int형태로 저장한다.

# 입력예시
# Soccer Contest
# 10

# 출력예시
#[("Python Homework",3), ("Assay",4),("Vacation",100),("Soccer Contest",10)]


# todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

# [문제풀이]
# 1. 문자열을 받고, 숫자로 받고. 이렇게 2번을 받은 것을 튜플로 묶어준다.
# 2. 이러한 튜플을 리스트에 넣어야 하므로 1번 이전에 ~ = []의 빈 리스트를 만들어주고 거기에 넣는다.
# 3. 여기서는 어떻게 끝낼 것인지는 없기에, while문을 통해 내가 입력해서 끝내주도록 하자.

todo = []
while len(todo)>=0:
    what_todo1 = input('할일은 무엇인가요?:')                # 해야 할 일을 입력
    if what_todo1 != 'Done':                                # 해야 할 일이 없다면 작성을 끝내기 위함
        what_todo2 = int(input('남은 일수는 어떻게 되나요?:'))  # 해야 할 일의 남은 일 수를 작성
        todo.append((what_todo1, what_todo2))               # 해야할 일과, 남은 일 수를 ()안에 넣어 튜플로 만들고 리스트에 추가하기
    else:
        break
print(todo)