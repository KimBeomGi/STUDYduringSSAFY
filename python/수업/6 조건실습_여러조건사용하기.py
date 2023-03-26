'''
만약(미세먼지 농도가 150보다 크다)면
('매우나쁨'을 출력)해줘
그게 아니라(미세먼지 농도가 150이하 80초과라)면
('나쁨'을 출력)해줘
그게 아니라(미세먼지 농도가 80이하 30초과라)면
('보통'을 출력)해줘
모두 아니라면
('좋음'을 출력)해줘
'''

nongdo = 60

if nongdo > 150:
    print('매우나쁨')
elif 80 < nongdo <= 150:    #elif nongdo <= 150 and nongdo >80:
    print('나쁨')
elif 30 < nongdo <= 80:     #elif nongdo <=80 and nongdo >30:
    print('보통')
else:
    print('좋음')

nongdo = 180
if nongdo <30:
    print('좋음')
elif 30 < nongdo <= 80:
    print('보통')
elif 80 < nongdo <150:
    print('나쁨')
else:
    print('매우나쁨')

