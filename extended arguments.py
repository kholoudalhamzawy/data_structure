
#to take unlimited number of parameters we use astrisk
def volume(*lengths):
    #the iter() allow us to iterate through all parameters which is stored as a tuple
    i=iter(lengths)
    #the next() allow us to set v to the first parameter
    v=next(i)
    for length in i:
        v*= length
    return v

#honstly i donno i tried them without the iter and next and it worked 3adè

 #for more understandable error when not putting any parameters:
 #we put an original first parameter

def volume2(length,*lengths):
    v=length
    for item in lengths:
        v*= item
    return v

print(volume2(2))

# arg* and kwarg** should always be the last parameters



sun=[1,3,5,6,5]
mon=[9,8,7,6,2]
tue=[9,8,7,6,2]
for item in zip(sun,mon,tue):
    print (item)
#or instead of looping and writing all parameters:

#to pretty print list of lists
from pprint import pprint as pp
days=[sun,mon,tue]
pp(list(zip(*days)))




def seq(immutable):
    if immutable:
        cls=list
    else:
        cls=tuple
    return cls
#we can loose the cls part and return list/tuble right away

a=seq("hdh") #meaning true
b=seq("") #meaning false
print(a)
print(a("kkj"))
print(b)
print(b("kkj"))

# can be shortened
def seqq(immutable):
    return list if immutable else tuple
a=seqq("hdh") #meaning true
b=seqq("") #meaning false
print(a)
print(a("kkj"))
print(b)
print(b("kkj"))




class add_to_list:
    def __init__(self,list):
        self.list=list

    def __call__(self, *args, **kwargs):
        for item in args:
            self.list.append(item)
        return self.list

    def __str__(self):
        return str(self.list)

    def __iter__(self):
        return iter(self.list)

    def __len__(self):
        return len(self.list)

list=[2,3]
newlist=add_to_list(list)
newlist(3,2,4)
print(newlist)
for i in newlist:
    print(i)
print(f"the length is {len(newlist)}")
print('#'*44)
list=[9,2]
l=list.copy()
list.append(2)
print(l)
print('#'*44)

class zey:
    # def __init__(self):

    def lala(self):
        self.list=[2,3]
        return self.list

    def op(self):
        self.list.append(22)
        return self.list
    def p(self):
        self.list.append(10)
        return self.list

#not defining the self.list in the __init__ requiers the method to be called first

s=zey()
print(s.lala())
print(s.op())
print(s.p())
print(s.op())
print(s.lala())
print(s.p())
l=[9,8,7]
for last_index in range(3):
    print(l[0:last_index])
