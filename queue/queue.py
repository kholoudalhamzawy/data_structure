
class node:
    def __init__(self,data):
        self.item=data
        self.ref=None
class listed_stack:
    def __init__(self):
        self.head=None
        self.tail=None

    def inqueue(self,data):
        newnode=node(data)
        if not self.head:
          self.head=newnode
          #self.head.ref=newnode
          self.tail=newnode
        else:
            newnode.ref=self.head
            self.head=newnode

    def dequeue(self):
        item = self.tail.item
        node=self.head
        while node.ref is not self.tail:
            node=node.ref
        self.tail=node
        return item

