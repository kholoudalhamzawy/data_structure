
class node:
    def __init__(self,value):
        self.value=value
        self.parent=None
        self.left=None
        self.right=None
        self.exist=False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

class binary_tree:
    def __init__(self):
        self.root=None
        self.count=0
        self.list=[]
        self.dub_list=self.list.copy()

    def __iter__(self):
        return iter(self.list)

    def __call__(self, *values):
        for value in values:
            self.list.append(value)
            self.count += 1
            if not self.root:
                self.root = node(value)
            else:
                self._add(self.root,value)

    def __len__(self):
        return len(self.list)

    #or
    def add(self,*values):
        for value in values:
            self.list.append(value)
            self.count += 1
            new_node=node(value)
            if not self.root:
                self.root= new_node
            else:
                self._add(self.root,value)


    def _add(self,current_node,value):
        new_node=node(value)
        if new_node.value<current_node.value:
            if not current_node.left:
                current_node.left= new_node
                new_node.parent=current_node

            else:
                self._add(current_node.left,value)
        else:
            if not current_node.right:
                current_node.right=new_node
                new_node.parent=current_node
            else:
                self._add(current_node.right,value)

    def __repr__(self):
        if not self.root:
            raise Exception("tree is empty :(")
        return repr(self.list)



    def __str__(self):
        if not self.root:
            raise Exception("tree is empty :(")
        return str(self.list)


    #or

    # to print a copy of the tree
    def ordered_tree(self):
        if not self.root:
            raise Exception("tree is empty :(")
        self.dub_list.clear()
        return self._pre_order_traverse(self.root)

    def _pre_order_traverse(self, node):
        if node:
            if __name__=='__main__':
                print(node.value)
            self.dub_list.append(node.value)
            self._pre_order_traverse(node.left)
            self._pre_order_traverse(node.right)
        return self.dub_list


    # to print a sorted copy of the tree
    def sorted_tree(self):
        if not self.root:
            raise Exception("tree is empty :(")
        self.dub_list.clear()
        return self._in_order_traverse(self.root)

    def _in_order_traverse(self, node):
        if node:
            self._in_order_traverse(node.left)
            if __name__ == '__main__':
                print(node.value)
            self.dub_list.append(node.value)
            self._in_order_traverse(node.right)
        return self.dub_list

    # if u want to delete the whole tree
    def delete_whole_tree(self):
        if not self.root:
            raise Exception("tree is already empty ;)")
        self._post_order_traverse(self.root)
        # or self.root=None


    def _post_order_traverse(self, node):
        if node:
            self._post_order_traverse(node.left)
            self._post_order_traverse(node.right)
            if node is self.root:
                self.list.remove(node.value)
                self.root=None
                self.count-=1
            elif node.value < node.parent.value:
                self.list.remove(node.value)
                node.parent.left = None
                self.count-=1
            else:
                self.list.remove(node.value)
                node.parent.right = None
                self.count-=1

    # def exist(self,value):
    #     if not self._exist(self.root,value):
    #         return False
    #     else:
    #         return self._exist(self.root,value)

    def exist(self,value):
        if not self.root:
            raise Exception("tree is empty :(")
        if self._exist(self.root,value) is True:
            return self._exist(self.root,value)
        else:
            return False

    def _exist(self,current_node,value):
        if current_node:
            if current_node.value==value:
                self.exist=True
                return self.exist
            if current_node.value>value and current_node.left:
                self._exist(current_node.left,value)
            elif current_node.value<=value and current_node.right:
                self._exist(current_node.right,value)
        return self.exist


    def delete_node(self,value):
        if not self.root:
            raise Exception ("tree is empty :(")
        if not self.exist(value) :
            raise Exception("node is not in the tree :(")
        self.list.remove(value)
        self.count-=1
        self._delete_node(self.root, value)

    # 'bool' object is not callable >>:(
    # def delete_node(self,*values):
    #     for value in values:
    #         x=value
    #         if self.exist(x) :
    #             self._delete_node(self.root, value)
    #         else:
    #             raise Exception("node is not in the tree :(")

    def _delete_node(self,current_node,value):
        if current_node.value == value:
            #no children
            if not current_node.left and not current_node.right:
                if current_node.value < current_node.parent.value:
                    current_node.parent.left = None
                else:
                    current_node.parent.right = None
            #one left child
            elif current_node.left and not current_node.right:
                current_node.left.parent=current_node.parent
                #to know which side was the node to its parent
                if current_node.left.value < current_node.parent.value:
                    current_node.parent.left=current_node.left
                else:
                    current_node.parent.right = current_node.left
            #one right child
            elif not current_node.left and current_node.right:
                current_node.right.parent=current_node.parent
                if current_node.right.value < current_node.parent.value:
                    current_node.parent.left=current_node.right
                else:
                    current_node.parent.right = current_node.right
            #two children
            elif current_node.left and current_node.right:
                node=current_node.right
                while node.left:
                    node=node.left
            #####print(node)
                #removing the new node from it's original place
                if node is not self.root:
                    if node.value>=node.parent.value :
                        if node.right:
                            node.right.parent=node.parent
                            node.parent.right=node.right
                        else:
                            node.parent.right=None
                    elif node.value<node.parent.value:
                        if node.right:
                            node.right.parent=node.parent
                            node.parent.left=node.right
                        else:
                            node.parent.left=None
                #replacing the old node with the new node

                #setting children

                if node.left != current_node.left:
                    node.left = current_node.left
                if current_node.left:
                    current_node.left.parent=node
                if  node.right!=current_node.right:
                    node.right=current_node.right
                if current_node.right:
                    current_node.right.parent=node

                #setting parent
                if current_node is self.root:
                    self.root=node
                    node.parent=None
                else:
                    node.parent=current_node.parent
                    if node.value<current_node.parent.value:
                        current_node.parent.left=node
                    else:
                        current_node.parent.right=node
            return

        if current_node.value>value and current_node.left:
            self._delete_node(current_node.left,value)
        elif current_node.value<=value and current_node.right:
            self._delete_node(current_node.right,value)




if __name__=='__main__':

    tree=binary_tree()
    tree(12,8,7,3,7,17,15,14,16,19,18,20)
    tree.ordered_tree()
    tree.sorted_tree()
    tree.delete_node(17)
    tree.ordered_tree()
    tree.delete_whole_tree()
