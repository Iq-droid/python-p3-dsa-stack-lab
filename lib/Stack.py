class Stack:
    def __init__(self, items = None, limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit
    pass

    def isEmpty(self):
        return len(self.items) == 0
    pass

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")
    pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")
    pass

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")
    pass
    
    def size(self):
        return len(self.items)
    pass

    def full(self):
        return len(self.items) == self.limit
    pass

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
    pass
