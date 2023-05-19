import random

Men = ["개", "소", "말", "돼지", "닭", "오리" ]
Women = ["진달래꽃", "할미꽃", "개나리꽃", "민들레꽃"]
random.shuffle(Men)
random.shuffle(Women)

f = []

def ideal_type():
    if len(a)%2 == 0: #짝수명이면 부전승 없이
        loop = len(a) // 2
        for i in range(0, loop): #대결 팀 배정
            while True:
                if loop == 1:
                    print("<< 준결승 >>\n")
                else:
                    print("<< 제 %d 강 >>\n " %(2**loop))
                print("%s vs %s" %(a[i], a[i+1]))        
                print("앞사람이 맘에 들면 1번을, 뒷사람이 맘에들면 2번을 입력")
                print("\n 입력:", end = ' ')
                temp = int(input())
                print()
                if temp == 1:
                    a.remove(a[i+1])
                    break
                elif temp == 2:
                    a.remove(a[i])  
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print()

    elif len(a)%2 != 0: #홀수명이면 한 명 부전승
        workover = a[-1]  #부전승
        a.remove(a[-1])
        loop = len(a) // 2
        for i in range(0, loop): #대결 팀 배정
            while True:
                if loop == 1:
                    print("<< 준결승 >>\n")
                else:
                    print("<< 제 %d 강 >>\n " %(2**loop))
                print("%s vs %s" %(a[i], a[i+1]))
                print("앞사람이 맘에 들면 1번을, 뒷사람이 맘에들면 2번을 입력")
                print("\n 입력:", end = ' ')
                temp = int(input())
                print()
                if temp == 1:
                    a.remove(a[i+1])
                    break
                elif temp == 2:
                    a.remove(a[i]) 
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print()
        a.append(workover)



while True:
    print("남자라면 1번을, 여자라면 2번을 입력하세요.")
    print("\n 입력:", end = ' ')
    c = int(input())
    print()
    if c == 1:
        a = Women[:]
        break
    elif c == 2:
        a = Men[:]
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")



while len(a) != 1:
    ideal_type()

print("당신의 이상형은", a[0], "입니다")   
