class Node:
    def __init__(self, data):
        # 데이터를 저장할 변수
        # 다음요소를 가리키는 변수
        self.value = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        # 첫 번재 요소(노드)의 주소
        self.head = None
        self.size = 0
    def append(self, data):
        # 리스트에 데이터 추가...
        # 노드 만들어서 마지막에 추가, 첫요소라면 head에 참조시키기
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            # 마지막 요소 찾아서 걔한테 달아주기
            # node의 next가 None인 요소가 마지막 요소
            current = self.head
            while current.next:
                current = current.next
            # current의 next는 None
            current.next = new_node
        self.size += 1      # 노드를 새로 붙였으니 길이 증가
    
    def pop(self, idx=-1):  # idx=-1은 기본값이 -1임을 선언
        if idx == 0:
            # head를 현재 head의 next로 바꿔주기
            self.head = self.head.next
        elif idx == -1:     # 마지막 요소 삭제
            # 마지막 요소의 이전요소 next를 None으로 바꿔주기
            if self.size == 1:
                self.head = None
            else:
                current = self.head
                for i in range(self.size-2):
                    current = current.next
                current.next = None
        else:
            # 삭제하려는 요소의 이전 요소의 next를
            # 삭제하려는 요소의 next로 바꿔주면 됨.
            current = self.head
            prev = None
            for i in range(idx):
                prev = current
                current = current.next
            prev.next = current.next

        pass


    def __str__(self):      # 매직메서드 __str__
        # 현재 리스트가 어떻게 구성되어있는지 출력하기 위해서 작성
        result = '['
        current = self.head
        while current:      # current가 value를 가지고 있으면 계속 수행
            result += (str(current.value)+', ')
            current = current.next
        result += ']'
        return result


lst = MyLinkedList()
lst.append('A')
lst.append('B')
lst.append('C')
lst.append('D')
lst.append('E')
print(lst)
lst.pop(2)
print(lst)
# lst.pop()