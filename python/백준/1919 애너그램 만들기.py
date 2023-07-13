# 문제
# 두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 그러한 두 단어를 서로 애너그램 관계에 있다고 한다. 예를 들면 occurs 라는 영어 단어와 succor 는 서로 애너그램 관계에 있는데, occurs의 각 문자들의 순서를 잘 바꾸면 succor이 되기 때문이다.

# 한 편, dared와 bread는 서로 애너그램 관계에 있지 않다. 하지만 dared에서 맨 앞의 d를 제거하고, bread에서 제일 앞의 b를 제거하면, ared와 read라는 서로 애너그램 관계에 있는 단어가 남게 된다.

# 두 개의 영어 단어가 주어졌을 때, 두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오. 문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.

# 입력
# 첫째 줄과 둘째 줄에 영어 단어가 소문자로 주어진다. 각각의 길이는 1,000자를 넘지 않으며, 적어도 한 글자로 이루어진 단어가 주어진다.

# 출력
# 첫째 줄에 답을 출력한다.

# 입력값
# aabbcc
# xxyybb

# 출력값
# 8


A = list(input())
B = list(input())
count_v = 0
A_dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 
         'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0
        }
B_dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 
         'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0
        }

for i in range(len(A)):
    A_dic[A[i]] += 1
for i in range(len(B)):
    B_dic[B[i]] += 1
# print(A_dic)
# print(B_dic)

ALPHABET = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
for i in range(len(ALPHABET)):
    if A_dic[ALPHABET[i]] and B_dic[ALPHABET[i]]:
        if A_dic[ALPHABET[i]] > B_dic[ALPHABET[i]]:
            count_v += A_dic[ALPHABET[i]] - B_dic[ALPHABET[i]]
        elif A_dic[ALPHABET[i]] < B_dic[ALPHABET[i]]:
            count_v += B_dic[ALPHABET[i]] - A_dic[ALPHABET[i]]
    elif A_dic[ALPHABET[i]] and not B_dic[ALPHABET[i]]:
        count_v += A_dic[ALPHABET[i]]
        pass
    elif B_dic[ALPHABET[i]] and not A_dic[ALPHABET[i]]:
        count_v += B_dic[ALPHABET[i]]
        pass
print(count_v)