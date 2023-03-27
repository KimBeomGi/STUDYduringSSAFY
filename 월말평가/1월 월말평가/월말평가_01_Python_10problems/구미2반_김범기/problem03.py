# [문제]
# 이싸피는영화정보를제공해주는서비스의개발팀에서데이터분석을담당하고있다. 
# The Movie Database API를이용하여데이터를수집하였다.
# 받아온영화샘플정보는dictionary 형태이다. 
# 영화데이터는다음과같이구성되어있다고할때아래의신규기능을추가하려고한다.

# 평점이8점이상이라면True를반환하고, 8점미만이라면False를반환하는함수is_good_rate를완성하시오. 
# (반환되는값True와False는bool 자료형이다.)

# [문제풀이]
# 1. if문을 딕셔너리의 value를 이용해서 True와 False를 구분



# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_good_rate(movie):
    if movie['user_rating'] >= 8:       # user_rating의 값이 8이상이면  True
        return True
    else:
        return False



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(is_good_rate(movie))  # True