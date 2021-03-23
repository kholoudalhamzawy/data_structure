
class new_stack:
    def __init__(self):
        self.size_arr=0
        self.arr=[]

    def size(self,data):
        if data < self.size_arr:
            return None
        self.size_arr=data

    def push(self,data):
        if self.size_arr ==len(self.arr):
            return None
        self.arr.append(data)

    def peek(self):
        if len(self.arr)==0:
            return None
        return self.arr[0]

    def pop(self):
        if len(self.arr)==0:
            return None
        return self.arr.pop()

    def pop_from_back(self):
        if len(self.arr) == 0:
            return None
        return self.arr.pop(0)


#so that stack could be iterable, instead of doing it en every new stack:
    def __iter__(self):
        return iter(self.arr)

#so that stack could be printed out as a string:
    def __str__(self):
        return str(self.arr)

    def __repr__(self):
        return repr(self.arr)

#so that stack could have length:
    def __len__(self):
        return len(self.arr)

#u could have avoided all this by just returning the self.arr instead of queue/stack in the problems


x=new_stack()
x.size(4)
x.push(6)
x.push(2)
x.push(4)
x.push(8)


#4.1
def postfix_evaluation(set):
    stack=new_stack()
    stack.size(len(set))
    for char in set:
        if (char=='+'):
           stack.push( stack.pop()+stack.pop() )
        elif(char=='-'):
            stack.push(stack.pop() - stack.pop())
        elif  (char=='*'):
            stack.push(stack.pop() * stack.pop())
        elif (char=='/'):
            stack.push(stack.pop() / stack.pop())
        else:
            stack.push(char)
    return stack.pop()



#4.2
def static_stack_split(stack,int):
    stack1,stack2=new_stack(),new_stack()
    stack1.size(len(stack))
    stack2.size(len(stack))
    for value in stack:
        if not value:
            break
        elif value <= int:
            stack1.push(value)
        else:
            stack2.push(value)
    return stack1.arr,stack2.arr



#4.4
def palindrome(string):
    string=string.replace(" ","").lower()
    stack1=new_stack()
    stack1.size(len(string))
    stack2=new_stack()
    stack2.size(int(len(string)/2))
    for index in string:
        stack1.push(index)
    for index in range(int(len(string)/2)):
        stack2.push(stack1.pop())
    if len(stack1)>len(stack2):
        stack1.pop()
    for index in range(len(stack1)):
        if stack1.pop()!=stack2.pop():
            return False
    return True


#4.5
char =new_stack()
char.size(4)
char.push('a')
char.push('b')
count= new_stack()
count.size(4)
count.push(1)
count.push(2)
def dublicate(stack1,stack2):
    stack=new_stack()
    stack.size(200)
    for element1 in stack1:
        element2=stack2.pop_from_back()
        if(not element2):
            break
        for int in range(element2):
            stack.push(element1)
    return stack.arr

#4.6
def average(stack):
    sum=0
    for element in stack:
        sum+=element
    return sum/len(stack)




##########################################################
##########################################################

#5.1
#deque is what have queue and stack prefrences (pronounced deck LOL)

class new_queue:
    def __init__(self):
        self.size_arr=0
        self.arr=[]

    def size(self,data):
        if data < self.size_arr:
            return None
        self.size_arr=data

    def enqueue(self,data):
        if self.size_arr ==len(self.arr):
            return None
        self.arr.append(data)

    def peek(self):
        if len(self.arr)==0:
            return None
        return self.arr[0]

    def front_enqueue(self,data):
        if self.size_arr ==len(self.arr):
            return None
        self.arr.insert(0,data)

    def dequeue(self):
        if len(self.arr)==0:
            return None
        return self.arr.pop(0)

    def rear_dequeu(self):
        if len(self.arr)==0:
            return None
        return self.arr.pop()

    def __iter__(self):
        return iter(self.arr)

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        return repr(self.arr)


q=new_queue()
q.size(12)
q.enqueue(4)
q.enqueue(3)
q.enqueue(0)
q.enqueue(2)
q.enqueue(0)
q.front_enqueue(5)
q.front_enqueue(77)
q.enqueue(q.dequeue())
q.enqueue(1)
q.rear_dequeu()
#print(q)
#qlq=new_queue()
qlq=q
qlq.enqueue(4)
#print("ddf",qlq)
#print(q)
q.enqueue(9)
#print("ddf",qlq)

#note

# when u make to queues/stacks equal, they become pretty much the same, when modifying one of them, u'r actuelly modifing both of them.

# len(queue/stack)changes when u modify the queue/stack, so maybe tro to put it in a variable first

# u can't assign an existing stack/queue to ur stack/queue class, won't work ;)


#5.2
def mirror(queue):
    rev=new_stack()
    rev.size(len(queue))
    queue.size(len(queue)*2)

  # to iterate through queue if didn't use def iteration in the class def
    for item in range(len(queue)):
        rev.push(queue.peek())
        queue.enqueue(queue.dequeue())

    for item in range(len(rev)):
        queue.enqueue(rev.pop())
 # return the stack/queue .arr for easier everything
    return queue.arr

#print(q)


#5.3
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    stack,queue=new_stack(),new_queue()
    stack.size(int(len(string)/2))
    queue.size(int(len(string)/2))
    for index in string:
        if len(stack)!=int(len(string)/2):
            stack.push(index)
        elif (len(string)/2)==(int(len(string)/2)):
            queue.enqueue(index)
        else:
            string=string.replace(index,"",1)
    for integer in range(len(stack)):
        if stack.pop()!=queue.dequeue():
            return False
    return True


#5.4
def shift_the_zero(queue):
    dub=new_queue()
    dub.size(len(queue))
    for element in queue:
            if element !=0:
                dub.enqueue(element)
    for int in range(len(queue)-len(dub)):
        dub.enqueue(0)
    queue=dub
    return queue.arr
#print(q)


#5.5
def anagrams(string1,string2):
    if len(string1)!=len(string2):
        return False
    queue1,queue2=new_queue(),new_queue()
    queue1.size(len(string1))
    queue2.size(len(string2))
    for char1 in list(string1):
        queue1.enqueue(char1)
    for char2 in list(string2):
        queue2.enqueue(char2)

    #sol1
    for element1 in range(len(queue2)):
        anagram=False
        head1=queue1.dequeue()
        for element2 in range(len(queue2)):
            head2 = queue2.dequeue()
            if head1==head2:
                anagram=True
                break
            else:
                queue2.enqueue(head2)
        if not anagram:
            return False
    return True

   #sol2
    # for element1 in range(len(queue2)):
    #     head1=queue1.dequeue()
    #     head2 = queue2.dequeue()
    #     c2=head2
    #     while(head1!=head2):
    #         queue2.enqueue(head2)
    #         head2=queue2.dequeue()
    #         if head2==c2:
    #             return False
    # return True


if __name__=='__main__':
    print(postfix_evaluation((1, 2, "+", 3, 5, "*", 4, 3)))
    print(static_stack_split(x, 6))
    print(palindrome("masd Am "))
    print(dublicate(char, count))
    print(shift_the_zero(q))
    print(is_palindrome("ma A aM"))
    print(mirror(q))
    print(average(x))
    print(anagrams("post", "stop"))

