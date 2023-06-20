# 정규식 기본1


# 주민등록번호
# 901201-111111

# 이메일 주소
# nadocoding@gmail.com
# nudocoding@gmail@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1
# 1000.2000.3000.4000



import re
# abcd, book, desk
# ca?e
# caae, cabe, cace, cade, ...

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자 > care, cafe, case와 같은 것은 됨 | caffe는 안됨
# ^ (^de) : 문자열의 시작 > desk, destination와 같은 것음 됨 | fake는 안됨
# $ (se$) : 문자열의 끝 > case, base와 같은 것은 됨 | face는 안됨

# m = p.match("case")
# print(m.group())    # 매치되지 않으면 에러가 발생
# m = p.match("caffe")  # 이러면 에러 발생
# print(m.group())    # 매치되지 않으면 에러가 발생

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")
    
m = p.match("careless")     # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)