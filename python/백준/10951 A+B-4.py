A, B = map(int, input().split())
while A and B:
    print(A+B)
    try : A, B = map(int, input().split())
    except: break