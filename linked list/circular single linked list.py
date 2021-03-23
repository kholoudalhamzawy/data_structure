
class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class linked_list:
    def __init__(self):
        self.startnode=None
        self.tailnode=None
        self.counter=0


    def traverse_list(self):
        if self.startnode is None:
            print("list is empty")
            return
        else:
            n=self.startnode
            while n:
                print(n.item," ")
                n=n.ref
                if n == self.startnode:
                    break
            print("the number of items in the list is ",self.counter)

    def insert_at_start(self,data):
        newnode=Node(data)
        if self.startnode is None:
            self.startnode=newnode
            self.tailnode=newnode
            newnode.ref = self.startnode
            self.counter += 1
        else:
            newnode.ref = self.startnode
            self.tailnode.ref=newnode
            self.startnode = newnode
            self.counter += 1


    def insert_at_end(self,data):
        newnode=Node(data)
        if not self.startnode:
            self.tailnode=newnode
            self.startnode = newnode
            self.counter += 1
            return

        self.tailnode.ref=newnode
        self.tailnode=newnode
        newnode.ref=self.startnode
        self.counter+=1
        # return


    def insert_after_item(self,x,data):
        newnode = Node(data)
        if self.tailnode.item == x:
            self.tailnode.ref=newnode
            self.tailnode=newnode
            newnode.ref=self.startnode
            self.counter += 1
            return

        n=self.startnode
        while n.item !=x:
            n=n.ref
        newnode.ref=n.ref
        n.ref=newnode
        self.counter += 1

    def insert_before_item(self,x,data):
        if self.startnode is None:
            print("list is empty")
            return
        if x==self.startnode.item:
            newnode=Node(data)
            newnode.ref=self.startnode
            self.startnode=newnode
            self.tailnode.ref=newnode
            self.counter += 1
            return
        n=self.startnode
        while n.item !=x:
            n=n.ref
        newnode = Node(data)
        newnode.ref = n.ref
        n.ref = newnode
        self.counter += 1

    def insert_before_index(self,index,data):
        if index==0:
            newnode=Node(data)
            newnode.ref=self.startnode
            self.startnode=newnode
            self.tailnode.ref=newnode
            self.counter += 1
            return
        i=0
        n=self.startnode

        while i < index-1 and n is not None:
            i=i+1
            n=n.ref
        if n is None:
            print("index out of bound")
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode
            self.counter += 1

    def insert_input_at_start(self):
            n=Node(int(input("inter new node : ")))
            n.ref=self.startnode
            self.tailnode.ref=n
            self.startnode=n
            self.counter += 1

    def make_new_list(self):
        num=int(input("how many nodes will you add ? "))
        if num == 0:
            return
        for nums in range(num):
            value=int(input("inter ur new node : "))
            self.insert_at_end(value)

    def delete_from_start(self):
        if self.startnode is None:
            print("the list is empty")
        else:
            self.startnode=self.startnode.ref
            self.tailnode.ref=self.startnode
            self.counter -= 1

    def delete_from_end(self):
        if self.startnode is None:
            print("the  list is empty")
        else:
            n=self.startnode
            while n.ref is not self.tailnode:
                n=n.ref
            n.ref=self.startnode
            self.tailnode=n
            self.counter -= 1


    def delete_element_by_value(self,x):
        if self.startnode is None:
            print("the list is empty")
            return
        if self.startnode.item==x:
            self.startnode=self.startnode.ref
            self.tailnode.ref=self.startnode
            self.counter -= 1

            return
        n=self.startnode
        while n.ref.item != x:
            n=n.ref
        n.ref=n.ref.ref
        self.counter -= 1



new_linked_list = linked_list()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_start(20)
new_linked_list.insert_after_item(10,12)
new_linked_list.insert_before_item(12,4)
new_linked_list.insert_before_index(3,4)
new_linked_list.delete_from_start()
new_linked_list.delete_from_end()
new_linked_list.insert_input_at_start()
new_linked_list.delete_element_by_value(12)
new_linked_list.traverse_list()
new_linked_list.make_new_list()
new_linked_list.traverse_list()


