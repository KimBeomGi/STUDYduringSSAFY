arr = [1,5,8,17,20,25,35,44]
N = len(arr)

# key : 찾으려는 값, 있으면 True, 없으면 False 반환
def binary_search(key):
    start = 0
    end = N-1
    
    # while True:
    while start <= end:
        # if start > end:       # start와 end의 역전이면, 그러니까 못찾았으면!!
        #     break 또는 return False

        # 1. 검색범위 중간값 찾기
        # 보통 중간값은 인덱스 끝과 끝 여기서는 0과 7을 더해서 //2 한 값
        mid = (start + end)//2
        if arr[mid] == key:
            return True
        # 못 찾은 경우, Key가 mid보다 큰 경우, 작은 경우로 나뉨
        elif key > arr[mid]:        # key값이 중간값보다 더 큰 경우, 중간보다 작은 건 필요가 읎따!!!!
            start = mid+1
        # elif key < arr[mid]:        # key값이 중간값보다 더 작은 경우, 중간보다 큰 건 필욕 읎따!!!!!
        #     end = mid-1
        else:       # key < arr[mid] # key값이 중간값보다 더 작은 경우, 중간보다 큰 건 필욕 읎따!!!!!
            end = mid -1            # 종료점을 중간 이전 인덱스로 설정
    return False


for i in range(1,51):
    print(f'{i} {binary_search(i)}')


arr = [1,5,8,17,20,25,35,44]
N = len(arr)

def binary_search(key):
    start = 0
    end = N-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return True
        elif key > arr[mid]:
            start = mid+1
        else:
            end = mid -1
    return False
print(binary_search(5))


arr = [1,5,8,17,20,25,35,44]
N = len(arr)

def binary_search(key):
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return 'Find'
        elif arr[mid] > key:
            end = mid -1
        elif arr[mid] < key:
            start = mid +1
    return "Don't have"
print(binary_search(35))