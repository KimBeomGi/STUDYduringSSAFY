N = int(input())
real_scores = list(map(int, input().split()))   # 원래 점수 3개
max_score = max(real_scores)                    # 최고점 찾기
lie_scores=[]
for i in range(N):
    lie_scores.append(real_scores[i]/max_score*100)
print(sum(lie_scores)/N)