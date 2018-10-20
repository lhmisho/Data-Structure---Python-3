class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__=="__main__":
    q = Queue()
    L = [1,2,3,4,5,6,7,8,9]
    for i in L:
        q.enqueue(i)

    while not q.is_empty():
        result = q.dequeue()
        print(result)

