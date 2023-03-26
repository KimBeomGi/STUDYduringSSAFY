# [문제]
# 김코딩은 용사가 되어 용을 잡으러 간다. 현재 skeleton을 실행하면 아래처럼 잡지 못하는 상황이다.
# 마법을 사용해서 용을 물리치려고 한다. 스켈레톤 파일을 참고하여, 용을 물리칠 수 있도록 Hero의 내장 함수의 set_magic_power를 완성하라.
# Hint: Hero, 그리고 Dragon이 상속한 Creature 객체의 attack_target 함수 작동 원리를 분석하라.
# Hint: set_magic_power 함수가 실행되는 위치를 파악하라

# [결과예시]
# Hero attack Dragon
# Dragon's hp: 500
# Dragon attack Hero
# Hero's hp: 140
# Hero attack Dragon
# Oh, Dragon is down! I repeat. Dragon is down!


class Creature:
    def __init__(self):
        self.hp = 0
        self.attack = 0
        self.deffence = 0

    def attack_target(self, target):
        print(f"{self} attack {target}")
        demage = self.attack - target.deffence
        target.hp -= demage if self.attack > target.deffence else 1
        if target.hp <= 0:
            print(f"Oh, {target} is down! I repeat. {target} is down!")
        else:
            print(f"{target}'s hp: {target.hp}")


class Hero(Creature):
    def __init__(self):
        super().__init__()
        self.hp = 150
        self.attack = 10
        self.deffence = 10

    def __str__(self):
        return "Hero"

    def set_magic_power(self):                          # 수정해야하는 set_magic_power 메소드
        # set the Hero Status(hp, attack, deffence)
        self.hp += 30                                   # hero의 체력을 30 증가시키거나 방어력을 30증가시키면 되는데 여기선 체력을 증가시켰다.
        self.attack += 590                              # hero의 공격력이 590증가되어야 출력되어야 할 값이 나온다.
        self.deffence += 0                              # hero의 체력을 30 증가시키거나 방어력을 30증가시키면 되는데 여기선 체력을 증가시켰다.


class Dragon(Creature):
    def __init__(self):
        super().__init__()
        self.hp = 1000
        self.attack = 50
        self.deffence = 100

    def __str__(self):
        return "Dragon"


hero = Hero()
hero.set_magic_power()
dragon = Dragon()
while (hero.hp > 0) and (dragon.hp > 0):
    hero.attack_target(dragon)
    if dragon.hp > 0:
        dragon.attack_target(hero)