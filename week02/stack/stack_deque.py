from typing import Any
from collections import deque

class Stack:
    """고정 길이 스택 클래스(collections.deque 사용)"""

    def __init__(self, maxlen):
        """스택 초기화"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self):
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return len(self.__stk)

    def is_empty(self):
        """스택이 비어 있는지 판단"""
        return not self.__stk

    def is_full(self):
        """스택이 가득 차 있는지 판단"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value):
        """스택에 value 푸시"""
        self.__stk.append(value)

    def pop(self):
        """스택에서 데이터 팝"""
        return self.__stk.pop()

    def peek(self):
        """스택에서 데이터를 피크"""
        return self.__stk[-1]

    def clear(self):
        self.__stk.clear()

    def find(self, value):
        """스택에서 value를 찾아 인덱스를 반환(찾지 못하면 -1을 반환)"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value):
        """스택에 포함되어 있는 value의 개수를 반환"""
        return self.__stk.count(value)

    def __contains__(self, value):
        """스택에 value가 포함되어 있는지 판단"""
        return self.count(value)

    def dump(self):
        """스택 안에 있는 모든 데이터를 나열(바닥에서 꼭대기 순으로 출력한다.)"""
        print(list(self.__stk))