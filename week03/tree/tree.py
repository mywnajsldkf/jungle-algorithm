from __future__ import annotations  # 상위 버전의 기능을 사용할 수 있다. https://teknology.tistory.com/5
from typing import Any, Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        """생성자(constructor)"""
        self.key = key  # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 포인터
        self.right = right  # 오른쪽 포인터

class BinarySearchTree:
    """이진 검색 트리"""
    # root에 None을 대입하여 노드가 하나도 없는 빈 상태의 이진 검색 트리를 만든다.
    def __init__(self):
        self.root = None    # 루트

    # 키값으로 노드를 검색한다.
    '''
    1. 루트(p)를 확인한다.
    2. p가 None이면 검색을 실패하고 종료한다.
    3. 검색하는 key와 주목 노드(p)를 비교한다.
        - key = p: 검색 성공 후 종료
        - key < p: 주목 노드를 왼쪽 자식으로 이동
        - key > p: 주목 노드를 오른쪽 자식으로 이동
    '''
    def search(self, key: Any) -> Any:
        p = self.root   # 루트 확인
        while True:
            if p is None:       # 더 이상 진행할 수 없으면
                return None     # 검색 실패
            if key == p.key:    # key와 노드 p의 키가 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key 쪽이 작으면
                p = p.left      # 왼쪽 서브트리에서 가져온다.
            elif key > p.key:   # key 쪽이 크면
                p = p.left      # 오른쪽 서브트리에서 가져온다.

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 노드를 삽입"""
        def add_node(node: Node, key: Any, value: Any):
            """node를 루트로 하는 서브트리에서 키가 key이고 값이 value인 노드를 삽입"""
            if key == node.key:
                return False    # key가 이진 검색 트리에 이미 존재한다.
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        """root가 None이면, 트리가 빈 상태이므로 루트만으로 구성된 트리를 만든다."""
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        # 트리는 비어있지 않다. -> add_node 함수를 호출하여 노드를 삽입한다.
        else:
            return add_node(self.root, key, value)

    '''
    노드를 삭제한다.
    - 자식 노드가 없는 노드를 삭제하는 경우
    => 해당 노드가 상위 노드의 왼쪽에 있다면, 상위 노드의 왼쪽 포인트가 해당 노드를 가리키지 않도록 업데이트한다.(왼쪽 포인터: None)
    - 자식 노드가 1개인 노드를 삭제하는 경우
    => 삭제할 노드가 부모 노드의 왼쪽 자식인 경우: 왼쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트한다.
    => 삭제할 노드가 부모 노드의 오른쪽 자식인 경우: 오른쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트한다.
    - 자식 노드가 2개인 노드를 삭제하는 경우
    1. 삭제할 노드의 왼쪽 서브트리에서 키값이 가장 큰 노드를 검색한다.
    2. 검색한 노드를 삭제 위치로 옮긴다. 검색한 노드의 데이터를 삭제할 노드 위치에 복사한다.
    3. 옮긴 노드를 삭제한다. 이때 자식 노드의 개수에 따라 다음이 수행된다.
    - 옮긴 노드에 자식 없음: '자식 노드가 없는 노드 삭제'
    - 옮긴 노드에 자식 1개 있음: '자식 노드가 1개인 노드 삭제'
    '''
    def remove(self, key: Any) -> bool:
        """키가 key인 노드 삭제"""
        p = self.root       # 스캔 중인 노드
        parent = None       # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인

        # A. 자식 노드가 없는 노드를 삭제하는 경우
        while True:
            if p is None:       # 더 이상 진행할 수 없으면
                return False    # 키는 존재하지 않는다.

            if key == p.key:    # key와 노드 p의 키가 같다.
                break           # 검색 성공
            else:
                parent = p                  # 가지 내려가기 전에 부모 설정
                if key < p.key:             # key가 더 작으면
                    is_left_child = True    # 왼쪽 자식
                    p = p.left              # 왼쪽 서브 트리에서 검색
                else:                       # key가 더 크면
                    is_left_child = False   # 오른쪽 자식 내려감
                    p = p.right             # 오른쪽 서브 트리에서 검색

        if p.left is None:
            # B. 자식 노드가 1개인 노드를 삭제하는 경우
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right   # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right  # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left    # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left   # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            # C. 자식 노드가 2개인 노드를 삭제하는 경우
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key        # left의 키를 p로 이동
            p.value = left.value    # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left # left 삭제
            else:
                parent.right = left.left    # left 삭제
        return True

    # 모든 노드를 오름차순으로 출력하는 dump() 함수
    def dump(self, reverse = False) -> None:
        """node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력"""
        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)            # 왼쪽 서브트리를 오름차순으로 출력
                print(f'{node.key} {node.value}')   # node를 출력
                print_subtree(node.right)           # 오른쪽 서브트리를 오름차순으로 출력

        def print_subtree_rev(node: Node):
            """node를 루트로 하는 서브트리의 노드를 키의 내림차순으로 출력"""
            if node is not None:
                print_subtree_rev(node.right)       # 오른쪽 서브트리를 내림차순으로 출력
                print(f'{node.key} {node.value}')   # node를 출력
                print_subtree_rev(node.left)        # 왼쪽 서브트리를 내림차순으로 출력

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    # 가장 작은 키/가장 큰 키를 반환한다. -> 맨 끝이 none을 만날 때까지 왼쪽 또는 오른쪽 자식을 따라간다.
    def min_key(self) -> Any:
        """가장 작은 키"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """가장 큰 키"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key