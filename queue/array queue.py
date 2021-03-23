
class array_queue:
    def __init__(self):
        self.arr=[0]

    def array_size(self,number):
        self.size=number+1

    def inqueue(self,data):
            self.arr.insert(0, data)


    def valid(self):
        if len(self.arr) >= self.size:
            print("array is full")
            return False
        return True


    def dequeue(self):
        if len(self.arr) == 1:
            print("queue is empty ")
        else:
            print(self.arr[len(self.arr) - 2])
            item=(self.arr[len(self.arr) - 2])
            self.arr.pop(len(self.arr) - 2)
            return item

    def peek(self):
        if len(self.arr) == 1:
            print("queue is empty ")
        else:
            print(self.arr[len(self.arr)-2])


queue=array_queue()
terminate =1

queue.array_size(int(input("inter the number of your queue elements : ")))

while terminate:
    print("To inqueue press '1', to dequeue press '2', to show first in queue press '3', press anything else to terminate.. ".title())
    command = int(input(" "))
    if command == 1:
        if queue.valid():
            queue.inqueue(input("inter your new value : "))
    elif command == 2 :
        queue.dequeue()
    elif command == 3:
        queue.peek()
    else:
        terminate =0


