
class stack:
    def __init__(self):
        self.arr=[]

    def size(self,data):
        self.num=data

    def valid(self):
        pass
    def push(self,data):
        # if len(self.arr) >= self.num:
        #     raise Exception ("stack is full")
        # else:
        self.arr.append(data)

    def pop(self):
        if len(self.arr) == 0:
            raise Exception("stack is empty")
            return None
        return self.arr.pop()

    def __str__(self):
        return str(self.arr)

class queue:

    def __init__(self):
        self.arr = []

    def size(self, data):
        self.num = data

    def enqueue(self,data):
        if len(self.arr) >= self.num:
            print("queue is full")
        else:
            self.arr.append(data)

    def dequeue(self):
        if len(self.arr) == 0:
            print("stack is empty")
            return None
        return self.arr.pop(0)

    def __str__(self):
        return str(self.arr)

if __name__=='__main__':

    x=stack()
    x.size(3)

    x.push(4)
    x.push(3)
    x.pop()
    print(x)

    q=queue()
    queue.size(q,3)
    queue.enqueue(q,4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    print(q)