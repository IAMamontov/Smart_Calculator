class Stack():

    def __init__(self):
        self.st = []

    def push(self, item):
        return self.st.append(item)


    def pop(self):
        return self.st.pop()


    def peek(self):
        return self.st[len(self.st) - 1]


    def is_empty(self):
        return not bool(len(self.st))
