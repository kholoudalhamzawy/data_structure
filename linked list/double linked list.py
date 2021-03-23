
class Node:
    def __init__(self,data):
        self.item=data
        self.nref=None
        self.pref=None


class double_list:
    def __init__(self):
        self.startnode=None

    def insert_at_start(self,data):
        newnode = Node(data)

        if self.startnode is None:
            self.startnode=newnode
        else:
            newnode.nref=self.startnode
            self.startnode.pref=newnode
            self.startnode=newnode

    def insert_at_end(self,data):
        newnode=Node(data)
        if self.startnode is None:
            self.startnode=newnode
        else:
            n=self.startnode
            while n.nref is not None:
                n=n.nref
            n.nref=newnode
            newnode.pref=n


    def insert_before_item(self,x,data):
        newnode=Node(data)
        if self.startnode is None:
            self.startnode=newnode
        else:
            n=self.startnode
            while n is not None:
                if n.item == x:
                    break
                n=n.nref
            if n is None:
                print("index not found")
            else:
                newnode.pref = n.pref
                newnode.nref=n
                if n.pref is not None:
                    n.pref.nref = newnode
                n.pref = newnode

    def traverse_list(self):
        n=self.startnode
        while n is not None:
            print(n.item," ")
            n=n.nref

    def delete_from_start(self):
        n=self.startnode
        if n is None:
            print("no items to delete !!")
        elif n.nref is None:
            self.startnode=None
        else:
            self.startnode=n.nref
            self.startnode.pref=None

    def delete_from_end(self):
        if self.startnode is None:
            print("no items to delete!!!")
        elif self.startnode.nref is None:
            self.startnode = None
        else:
            n= self.startnode
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None


    def delete_by_item(self,x):
        n = self.startnode
        if n is None:
            print("no items to delete!!!")
        elif n.item == x:
            self.startnode = None
        else:
            while n is not None:
              if n.item == x:
                break
              n=n.nref
            if n is None:
              print("item is not found")
            else :
                n.pref.nref = n.nref
                n.nref.pref = n.pref

linked_list=double_list()
linked_list.insert_at_start(3)
linked_list.insert_at_end(4)
linked_list.insert_before_item(4,5)
linked_list.insert_at_start(6)
linked_list.delete_by_item(5)
linked_list.delete_from_end()
linked_list.delete_from_start()
linked_list.traverse_list()








