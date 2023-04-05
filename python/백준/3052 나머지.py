answer_set = set()
for _ in range(10):
    A = int(input())
    answer_set.add(A%42)
print(len(answer_set))