# 목표
# 파이썬 기초 문법 (print, 이스케이프 문자열, 입력과 출력 등)에 대해 이해한다.
# 파이썬 기본 자료형 (문자형, 수치형, 불린형)에 대해 이해한다.
# 파이썬 복합 자료형 (리스트, 딕셔너리, 튜플)에 대해 이해한다.

# 온라인 실습실의 Q&A게시판을 생성하려고 한다.게시글의 총 갯수와 한 페이지에 필요한 게시글 수를 입력으로 주었을 때, 생성되는 총 페이지의 수를 출력하는 프로그램을 작성하시오.

# 입력 예시게시글의 총 갯수를 입력하세요 : 30
# 한 페이지에 필요한 게시글 수를 입력하세요 : 6
# 출력 예시: 5
# 요구사항

post = 30   #게시글 갯수
page = 6    #한 페이지당 갯수
if post % page ==0:     #게시글갯수가 페이지당 갯수로 똑 떨어지면 해당 페이지만 쓰면 되니 그냥 나누기
    print(int(post/page))
else:
    print(int(post/page)+1) #페이지당 갯수로 나눠떨어지지 않으면 페이지 하나 더 먹어야하니  +1