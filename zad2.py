from typing import Any
from zad1 import LinkedList, Node


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return self._storage.__len__()

    def __repr__(self):
        output = []
        node = self._storage.head
        while node is not None:
            output.insert(0, node.value)
            node = node.next
        output = map(str, output)
        output_ = "\n".join(output)
        return output_

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()

stack = Stack()
assert len(stack) == 0
print(f'stack = \n{stack}\ntest: ok')

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print(f'stack = \n{stack}\ntest: ok')

top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2
print(f'stack = \n{stack}\ntest: ok')
