from collections import deque


class MyStack:
    def __init__(self):
        self.main = deque()

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        last_el = self.main.popleft()
        for _ in range(len(self.main)):
            self.main.append(last_el)
            last_el = self.main.popleft()
        return last_el

    def top(self) -> int:
        top_el = self.pop()
        self.main.append(top_el)
        return top_el

    def empty(self) -> bool:
        return not self.main
