class Stack:
    def __init__(self):
        self.items = []

    # adding item in the stack
    def push(self,item):
        self.items.append(item)

    # removing item from the stack
    def pop(self):
        return self.items.pop()

    # checking weather the stack is empty or not
    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__=="__main__":
    s = Stack()
    L = [1,2,4,5,6,7,8]
    for i in L:
        s.push(i)

    while not s.is_empty():
        r = s.pop()
        print(r)

