# binary_search : key를 arr에서 찾으면, True, 아니면 False 반환
def binary_search(arr, key, s, e):
    # 정렬이 되어 있으니까...
    # 중간값 검사해서
    # 중간값이 key보다 작으면 뒤쪽 절반만 재검사
    # 중간값이 key보다 크면.. 앞쪽 절반만 재검사
    
    while s <= e:
        mid = (s+e)//2
        # 찾았다!
        if arr[mid] == key:
            return True
        #아닐 경우
        elif arr[mid] > key:    # 찾고자 하는 값이 중간값보다 작음! 뒤쪽 부분은 필요가 없음
            e = mid - 1
        else:                   # 찾고자 하는 값이 중간값보다 큼! 앞족 부분은 불필요
            s = mid + 1
    return False                # s와 e가 역전되어서 while문이 빠져나옴..key를 못찾음

arr = [2,4,7,9,11,19,23]

result = binary_search(arr,9,0,len(arr)-1)
print(result)