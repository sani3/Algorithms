class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return
        else:
            data = self.queue[0]
            self.queue.pop(0)
            return data

    def is_empty(self):
        return self.queue == []


if __name__ == 'main':
    LQ = ListQueue()
    LQ.is_empty()
    LQ.enqueue(3)
    LQ.enqueue("Into the queue")
    LQ.is_empty()
    print(LQ.queue)
    LQ.enqueue(8)
    LQ.enqueue([2, 6, 4])
    print(LQ.queue)
    LQ.dequeue()
    LQ.dequeue()
    print(LQ.queue)
