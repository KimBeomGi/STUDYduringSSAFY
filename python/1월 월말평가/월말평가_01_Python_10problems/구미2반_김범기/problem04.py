# [문제]
# 이싸피는영화정보를제공해주는서비스의개발팀에서데이터분석을담당하고있다. 
# The Movie Database API를이용하여데이터를수집하였다.
# 받아온영화샘플정보는dictionary 형태이다. 
# 영화데이터는다음과같이구성되어있다고할때아래의신규기능을추가하려고한다.

#제목이공백을포함하여몇글자인지반환하는함수title_length를완성하시오.
# (해당문제는python 내장함수len사용불가)

# [문제풀이]
# 1. 제목인 title key를 이용해야한다.
# 2. 공백을 포함해 몇 글자인지 반환. 그러나 len 사용불가



# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 len 사용 금지

def title_length(movie):
    i = 0
    for char in movie['title']: # i를 생성하여 각 문자열의 문자마다 +1 실시후 i 출력
        i += 1
    return i



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(title_length(movie))  # 6 (공백 포함 길이)