

class hash_table:
    def __init__(self):
        self.cap=100
        self.list = [[] for i in range(self.cap)]

    def hashing(self, key):

        if not isinstance(key,str):
            raise TypeError("key must be string")

        hashed_key = 0
        for char in key:
            hashed_key+=ord(char)

        return hashed_key % 100

                 # methods without the collision:

    # def __setitem__(self, key, value):
    #     hashed_key=self.hashing(key)
    #     self.list[hashed_key]=value


    # def __getitem__(self, key):
    #     hashed_key=self.hashing(key)
    #     return self.list[hashed_key]

    # def __delitem__(self,key):
    #     hashed_key=self.hashing(key)
    #     self.list[hashed_key]=None


                 # methods with linear probing

    # u can make a delete method and check if the capacity is full and the item is not found and raise errors and test them all but i have period cramps dude sorry, for any further explination visit the exe under the hash ved on codebasics

    def __setitem__(self, key, value):
        hashed_key = self.hashing(key)
        while self.list[hashed_key]:
            if (len(self.list[hashed_key]) > 0 and self.list[hashed_key][0] == key):
                self.list[hashed_key] = (key, value)
                return
            hashed_key += 1
            if hashed_key >= self.cap:
                hashed_key = 0
        self.list[hashed_key] = (key, value)

    def __getitem__(self, key):
        hashed_key = self.hashing(key)
        if self.list[hashed_key][0] == key:
            return self.list[hashed_key][1]

        while self.list[hashed_key]:
            hashed_key += 1
            if hashed_key >= self.cap:
                hashed_key = 0
            if self.list[hashed_key][0] == key:
                return self.list[hashed_key][1]




    # def __setitem__(self, key, value):
    #     hashed_key=self.hashing(key)
    #
    #     # to check if the key has value and if the key already existed so we just change the value of it
    #     # if u don't understand this loop, try printing it, sorry too meh to explain :(
    #
    #     # it's just so we dont make 2 loops, one to count the indeces and one to represent the pair, enumerate does that, i guess
    #
    #     for index, pair in enumerate(self.list[hashed_key]):
    #         if(len(pair)==2 and pair[0]==key):
    # #             becuse tuples are immutable, so u cant just do pair[1]=value, so we make a new tuple
    #             self.list[hashed_key][index]=(key,value)
    #             return
    #
    #     self.list[hashed_key].append((key,value))



    # def __getitem__(self, key):
    #     hashed_key=self.hashing(key)
    #     for pair in self.list[hashed_key]:
    #         if pair[0]==key:
    #             return pair[1]
    # # if it didnt find it and we returned nothing, it returns none by defult



    def __delitem__(self, key):
        hashed_key = self.hashing(key)
        for index,pair in enumerate(self.list[hashed_key]):
            if pair[0]==key:
                del self.list[hashed_key][index]

    def __repr__(self):
        return repr(self.list)

    def __str__(self):
        return str(self.list)













if __name__=='__main__':
    h=hash_table()
    h["march 16"]=60
    h["march 25"]=50
    print(h)