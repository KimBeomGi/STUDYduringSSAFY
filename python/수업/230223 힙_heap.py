# 완전이진트리 >>> 배열형태에 저장 가능
# 이번 건은 최소힙 만들기임.

heap = [0] * (2**4)     # 높이 3인 이진트리를 저장할 수 있음
# 삽입과 삭제: 마지막 자리를 알고 있어야합니다.(요소가 몇개냐?)
heapcount = 0   # 마지막 요소의 자리

def heap_push(data):            # heap에 요소 추가
    global heapcount
    # 마지막 요소의 뒤에 새로운 요소를 추가
    heapcount += 1
    heap[heapcount] = data
    # 새로 추가한 요소가 부모보다 작다면 교환(교환 후에 부모가 더 크다면 계속 반복하기, 루트까지)
    parent = heapcount//2
    current = heapcount
    while heap[parent] > heap[current]:            # 부모가 더 크다면 자리 교환
        heap[parent], heap[current] = heap[current] , heap[parent]
        current = parent
        parent = current//2

def heap_pop():                 # heap에서 최소값 반환 및 삭제
    global heapcount
    result = heap[1]
    # 1. 마지막 요소를 root에 옮기기 (왜 마지막 요소? >> heap의 모양을 최대한 유지하기 위해서...)
    # 2. 자식 중에서 작은 요소와 현재요소를 비교해서 자식 요소가 더 작다면 교환>> 반복. 자식이 없을 때 까지
    
    heap[1] = heap[heapcount]       # heapcount가 제일 마지막 요소의 번호임
    heap[heapcount] = 0        # 넣어도 되지만 굳이 필요없을 것 같아서 주석처리했다가 모양봐야되니까 다시 살림.
    heapcount -= 1
    # 자식 요소 중에서 작은 것 찾아야 함...
    parent = 1
    child = parent *2           # 일단 왼쪽 잡기.
    if child + 1 <= heapcount:  # 오른쪽 자식도 있다!!!
        if heap[child+1] < heap[child]: # 오른쪽 자식의 값이 왼쪽 자식의 값보다 작으면
            child += 1
    # child : 이 위치에서는 자식들 중에서 더 작은 값을 가지는 자식의 번호.
    while child <= heapcount and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parnet = child
        child = parent *2
        if child + 1 <= heapcount:  # 오른쪽 자식도 있다!!!
            if heap[child+1] < heap[child]: # 오른쪽 자식의 값이 왼쪽 자식의 값보다 작으면
                child += 1

    return result


heap_push(5)
print(heap)
heap_push(3)
print(heap)
heap_push(7)
print(heap)
heap_push(1)
print(heap)
heap_push(6)
print(heap)
heap_push(0)
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)