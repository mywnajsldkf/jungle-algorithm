from enum import Enum
from stack_list import FixedStack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'search', 'dump', 'quit'])

def select_menu():
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='    ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)  # 크기를 64로 할당

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()    # 메뉴 선택

    if menu == Menu.push:   # 푸시
        x = int(input('데이터를 입력하세요.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')
    elif menu == Menu.pop:
        try:
            s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    elif menu == Menu.search:
        x = int(input('검색할 값을 입력하세요.:'))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')
    elif menu == Menu.dump:
        s.dump()
    else:
        break