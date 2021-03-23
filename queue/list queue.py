
class node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class listed_queue:
    def __init__(self):
        self.head=None

    def inqueue(self,data):
        newnode=node(data)
        newnode.ref=self.head
        self.head=newnode

    def dequeue(self):

        if self.head is None:
            print("queue is empty")

        elif self.head.ref is None:
                print(self.head.item)
                self.head=None
        else:
            node = self.head
            while node.ref.ref is not None:
                node = node.ref
            print(node.ref.item)
            node.ref= None



    def peek(self):
        if not self.head:
            print("queue is empty")
        else:
            node=self.head
            while node.ref:
                node=node.ref
            print(node.item)

queue=listed_queue()

terminate=1
while terminate:
    print( "To inqueue press '1', to dequeue press '2', to show first in queue press '3', press anything else to terminate.. ".title())
    command = input(" ")
    if command == '1':
        queue.inqueue(input("inter the new value ".title()))

    elif command == '2':
        queue.dequeue()

    elif command == '3':
        queue.peek()
    else:
        terminate = 0

