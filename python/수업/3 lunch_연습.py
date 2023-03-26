'''
import random
menu=['한식','양식','중식','일식','베트남식','러시아식']

today_lunch1 = random.choice(menu)
today_lunch2 = random.sample(menu,2)
print(today_lunch1)
print(today_lunch2)

print(menu[4],menu[3])

print(len(menu))
'''
import random
room = ['1반', '2반', '3반', '4반', '5반', '6반', '7반', '8반', '9반', '10반', '11반']

today_clean1 = random.sample(room, 3)
t_c_toilet = random.choice(today_clean1)
t_c_dining = random.choice(today_clean1)
print(today_clean1)
print(t_c_toilet)
print(t_c_dining)

