
class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class linked_list:
    def __init__(self):
        self.startnode=None
        self.counter=0
        self.linked_list=[]

    def __len__(self):
        return len(self.linked_list)

    def __iter__(self):
        return iter(self.linked_list)

    def __str__(self):
        return str(self.linked_list)

    def __repr__(self):
        if not len(self.linked_list):
            raise Exception("list is empty :(")
        return repr(self.linked_list)



    def traverse_list(self):
        if self.startnode is None:
            print("list is empty")
            return
        else:
            n=self.startnode
            while n is not None:
                print(n.item," ")
                n=n.ref
            print("the number of items is ",self.counter)

    def showw(self):
        return self.linked_list

    def insert_at_start(self,data):
        newnode=Node(data)
        newnode.ref=self.startnode
        self.startnode=newnode
        self.counter+=1
        self.linked_list.append(data)


    def insert_at_end(self,data):
        newnode=Node(data)
        self.linked_list.append(data)
        if self.startnode is None:
           self.startnode=newnode
           self.counter += 1

           return
        n=self.startnode
        while n.ref is not None:
            n=n.ref
        n.ref=newnode
        self.counter+=1



    def insert_after_item(self,x,data):
        n=self.startnode
        print(n.ref)
        while n is not None:
            if n.item==x:
                break
            n=n.ref
        if n is None:
            print("item is not in the list")
        else:
            newnode= Node(data)
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
            self.counter += 1

            return

        n=self.startnode
        print(n.ref)
        while n.ref is not None:
            if n.ref.item==x:
                break
            n=n.ref
        if n.ref is None:
            print("the item is not in the list")
        else:
            newnode=Node(data)
            newnode.ref = n.ref
            n.ref=newnode
            self.counter += 1

    def insert_before_index(self,index,data):
        if index==0:
            newnode=Node(data)
            newnode.ref=self.startnode
            self.startnode=newnode
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
            n=Node(int(input("inter new node")))
            n.ref=self.startnode
            self.startnode=n
            self.counter += 1

    def make_new_list(self):
        num=int(input("how many nodes will you add ? "))
        if num == 0:
            return
        for nums in range(num):
            value=int(input("inter ur new node "))
            self.insert_at_start(value)

    def delete_from_start(self):
        if self.startnode is None:
            print("the list is empty")
        else:
            self.startnode=self.startnode.ref
            self.counter -= 1

    def delete_from_end(self):
        if self.startnode is None:
            print("the  list is empty")
        else:
            n=self.startnode
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
            self.counter -= 1


    def delete_element_by_value(self,x):
        if self.startnode is None:
            print("the list is empty")
            return
        if self.startnode==x:
            self.startnode=self.startnode.ref
            self.counter -= 1

            return
        n=self.startnode
        while n.ref is not None:
            if n.ref.item==x:
                break
            n=n.ref
        if n.ref is None:
            print("item is not found")
        else:
            n.ref=n.ref.ref
            self.counter -= 1



if __name__ == '__main__':

    new_linked_list = linked_list()
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_start(20)
    new_linked_list.insert_after_item(10,12)
    new_linked_list.insert_before_item(12,4)
    new_linked_list.insert_before_index(3,4)
    new_linked_list.insert_input_at_start()
    new_linked_list.traverse_list()




