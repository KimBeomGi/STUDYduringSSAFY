A,B,C = map(int, input().split())
# K=0
# while A+(B*K) >= C*K:
#     K+=1
# print(K)
if C-B > 0:
    print(int(A/(C-B))+1)
elif C-B <= 0:
    print(-1)