# 클래스 임포트
from queue import PriorityQueue

# 생성자를 이용해서 비어있는 우선순위 큐를 초기화한다.
queue = PriorityQueue()

# 우선순위 큐 기본 사이즈는 무한대이다.
# 크기를 지정하면 특정 크기를 가진 우선순위 큐를 생성할 수 있다.
size_queue = PriorityQueue(maxsize=10)

# 원소 추가
queue.put(2)
queue.put(6)
queue.put(10)
queue.put(1)

# 큐에서 원소 삭제 -> 크기 순서대로
print(queue.get())  # 1
print(queue.get())  # 2
print(queue.get())  # 6
print(queue.get())  # 10

# 졍렬 기준 변경 -> (우선순위, 값)의 튜플 형태로 데이터를 추가하고 제거한다.
queue.put((3, 'Apple'))
queue.put((1, 'Banana'))
queue.put((2, 'Cherry'))

print(queue.get()[1])   # Banana
print(queue.get()[1])   # Cherry
print(queue.get()[1])   # Apple