T = int(input())
for testcase in range(1, T+1):
    checked = input()
    
    total_count = 0
    count = 0
    for i in range(len(checked)):
        if checked[i] == 'O':
            count += 1
            total_count += count
        elif checked[i] =='X':
            count = 0
    print(total_count)