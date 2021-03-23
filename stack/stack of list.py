
class node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class linked_list_stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        newnode=node(data)
        newnode.ref=self.head
        self.head = newnode

    def traverse(self):
        count = self.head
        if not count:
            print("stack is empty")
        else:
            print("the items of stack are")
        while count:
            print(count.item)
            count = count.ref


    def pop(self):
        if not self.head:
            print("stack is empty")
        else:
            item= self.head.item
            self.head = self.head.ref
            return item

    def peek(self):
        print("the first item is ",self.head.item)

stack=linked_list_stack()
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


