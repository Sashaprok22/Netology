class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

closes = {
    "}": "{",
    "]": "[",
    ")": "(",
}

queue = input()
stack = Stack()

for s in queue:
    if s in "}])":
        if stack.is_empty() or closes.get(s) != stack.pop():
            print("Несбалансированно")
            break
    else:
        stack.push(s)
else:
    print("Сбалансированно")