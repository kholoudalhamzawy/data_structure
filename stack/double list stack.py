class stack:
    def __init__(self):
        self.arr=[]
        self.arr2=[]
        self.size=0

    def size_array(self,data):
            if (len(self.arr) > self.size):
                return
            self.size = data

    def push(self,data):
        if len(self.arr) < self.size:
            self.arr.append(data)
            print(data)
            return True
        print("stack is full")
        return False

    def popp(self):
        if len(self.arr) == 0:
            print("stack is empty")
            return None
        return self.arr.pop()
    def peek(self):
        print(self.arr[0])

    def pop_from_back(self):
        if len(self.arr) == 0:
            print("stack is empty")
            return None
        while len(self.arr) > 1:
            self.arr2.append(self.arr.pop())
        item = self.arr.pop()
        while len(self.arr2) >0:
            self.arr.append(self.arr2.pop())
        print(self.arr)
        return item


stack=stack()
stack.size_array(6)
stack.push(4)
stack.push(5)
stack.push(3)
stack.push(6)
stack.pop_from_back()