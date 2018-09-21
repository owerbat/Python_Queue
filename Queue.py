class Queue:
    def __init__(self, original=None):
        if type(original) is Queue:
            self.elements = original.elements[:]
        else:
            self.elements = []
        self.size = len(self.elements)

    def push(self, element):
        self.elements.append(element)
        self.size += 1

    def head(self):
        try:
            return self.elements[0]
        except IndexError:
            print("The queue is empty")
            return None

    def tail(self):
        try:
            return self.elements[self.size-1]
        except IndexError:
            print("The queue is empty")
            return None

    def pop(self):
        try:
            self.elements.pop(0)
            self.size -= 1
        except IndexError:
            print("The queue is empty")

    def __str__(self):
        return "head -> " + str(self.elements) + " <- tail"
