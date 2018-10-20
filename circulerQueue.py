class Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0,0,0

    def enqueue(self, item):
        if self.is_full():
            print("queue is full")
            return
        print("Inserting queue")
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head+1) % self.max_size
        self.size -= 1
        return item

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True

if __name__ == "__main__":
    q = Queue(3)
    q.enqueue("Misho")
    q.enqueue("Abrar")
    q.enqueue("Imran")
    q.enqueue("Nahid")

    while not q.is_empty():
        result = q.dequeue()
        print(result)