class stack_of_array:
    def __init__(self):
        self.arr=[]

    def traverse(self):
        for i in range (0,len(self.arr)):
            print(self.arr[i])

    def push(self,data):
        index=1
        while index:
            if self.arr[index-1] ==0:
             self.arr[index-1]=data
             self.arr.insert(index,0)
             return
            index+=1

    def pop(self):
        item= self.arr[len(self.arr)-2]
        self.arr.pop(len(self.arr)-2)
        return item

    def peek(self):
        print(self.arr[len(self.arr) - 2])

stack=stack_of_array()

terminate=1
while terminate:
    print( "To push press '1', to pop press '2', to peek press '3', press anything else to terminate.. ".title())
    command = input(" ")
    if command == '1':
        stack.push(input("inter the new value ".title()))

    elif command == '2':
        stack.pop()

    elif command == '3':
        stack.peek()
    else:
        terminate = 0
