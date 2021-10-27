from typing import Any
from zad1 import LinkedList


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()


    def __repr__(self):
        output = []
        node = self._storage.head
        while node is not None:
            output.append(node.value)
            node = node.next
        return output

    def __len__(self):
        return self._storage.__len__()

    def __str__(self):
        str_out = map(str, self.__repr__())
        return ", ".join(str_out)


    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

queue = Queue()
assert len(queue) == 0
print(f'queue = {queue}\ntest: ok')

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
print(f'queue = {queue}\ntest: ok')

client_first = queue.dequeue()
assert client_first == 'klient1'
print(f'client_first = {client_first}\ntest: ok')

assert str(queue) == 'klient2, klient3'
print(f'queue = {queue}\ntest: ok')
assert len(queue) == 2
print(f'queue_len = {len(queue)}\ntest: ok')
print(queue.peek())