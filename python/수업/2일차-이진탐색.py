# Binary search 이용

# 1~400 페이지에서 200페이지 찾기
# 문제에서는 200 페이지를 포함하고 있다.  고로 201~400이 아닌 200~ 400이 되도록!
# 이거 때문에 무한루프가 도는 경우도 있다.
# 무한루프가 돈다하면 인풋이 잘못되었거나 우리가 잘못만들었음

# [문제]
# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
# 예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
# A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.


#                     A                   B

# 첫 번째 탐색 l=1, r=400, c=200      l=1, r=400, c=200

# 두 번째 탐색 l=200, r=400, c=300    l=1, r=200, c=100

# 세 번째 탐색                        l=1, r=100, c=50

# 책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.


# [문제풀이]
# 0. 주어지는 입력값은 각각 책의 페이지 수, A가 찾아야하는 페이지, B가 찾아야하는 페이지 이다.
# 0-1. 문제는 누가 먼저 탐색을 끝내는지를 알아내야하므로, 탐색을 몇번 했는지를 알아낸다면 서로 비교해서 적은 쪽이 이긴다.
# 1. 23년 2월7일 오늘 배운 이진탐색을 이용해서 탐색을 해보고, 각 탐색마다 count += 1을 할 수 있게 작성해보자.
# 1-1. 중간페이지는 c= int((l+r)/2) 즉 c = int((start+end)/2)로 계산한다. c는 헷갈리니 middle로 명명해야지.
# 1-2. 책은 0쪽이 아닌 1쪽부터 시작하므로 항상 start = 1이 된다.
# 2. 예시를 보면 페이지는 동잃 중간값을 -1 Ehsms +1하지 않고 그대로 가져오는 것을 확인
# 2-1. while문을 탈출하는 것도 생각 필요

T = int(input())
for testcase in range(1,T+1):
    pages, A_page, B_page = map(int, input().split())               # 책의 총 페이지, A가 찾을 페이지, B가 찾을 페이지
    start = 1                                                       # 책은 1쪽부터 시작하므로
    end = pages                                                     # 리스트가 아니므로 페이지 끝이 end
    A_count = 0
    B_count = 0
    
    def cout_binary_search(start, end, page):
        count = 0
        while start <= end:                                         # 시작이 끝을 넘기지 않는다면
            middle = int((start+end)/2)                             # 예로 401/2는 200.5인데 200으로 출력하겠음을 의미
            count += 1
            if middle == page:                                      # 중간값이 찾으려는 A_page와 같다면
                return count                                        # 이제 그만 찾아도 좋다.
            elif middle > page:                                     # 중간값이 찾으려는 A_page보다 크다면
                end = middle                                        # 뒤의 값은 필요없으니 중간값 이전을 찾아보자.
            elif middle < page:                                     # 중간값이 찾으려는 A_page보다 작다면
                start = middle                                      # 앞의 값은 필요없으니 중간값 이후를 찾아보자.
        return count

    A_count = cout_binary_search(start, end, A_page)                # A_count를 구하는 함수
    B_count = cout_binary_search(start, end, B_page)                # B_count를 구하는 함수
    # print(A_count, B_count)   # 이건 몇번 검사했는지 확인용도
    # A가 시도한 횟수와 B가 시도한 횟수를 비교해서 각 값에따라출력하기 위함
    if A_count < B_count:                                           # B가 검색 횟수가 많으면 A가 이김
        print(f'#{testcase} A')
    elif A_count > B_count:                                         # A가 검색 횟수가 많으면 B가 이김
        print(f'#{testcase} B')
    elif A_count == B_count:                                        # A가 검색 횟수가 B랑 같으면 비김
        print(f'#{testcase} 0')