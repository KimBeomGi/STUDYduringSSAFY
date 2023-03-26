resistance = {'black':0, 'brown':1, 'red':2, 'orange':3,
              'yellow':4, 'green':5, 'blue':6, 'violet':7, 
              'grey':8, 'white':9}
multify = {'black':1, 'brown':10, 'red':100, 'orange':1000,
              'yellow':10**4, 'green':10**5, 'blue':10**6, 'violet':10**7, 
              'grey':10**8, 'white':10**9}

A= resistance[input()]
B= resistance[input()]
C= multify[input()]
print((10*A+B)*C)