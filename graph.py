
import single_linked_list
import simple_arr_snq

class graph(single_linked_list.linked_list):
    def __init__(self):
        self.list=[]
        self.visited = []
        self.index = 0

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return iter(self.list)

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        if not len(self.list):
            raise Exception("graph is empty :(")
        return repr(self.list)


    def insert(self,*values):
        self.index=single_linked_list.linked_list()
        for value in values:
            self.index.insert_at_end(value)
        self.list.append(self.index)

    def reach_at_index(self,index):
        if index>=len(self.list):
            raise IndexError ('index out of range >:(')
        return self.list[index].showw()


    def insert_at_index(self,index,data):
        self.list[index].insert_at_end(data)

    # these dunders can be used to reac indexes instead of the functions insert and reach

    def __setitem__(self, index, data):
        self.list[index] = data

    def __getitem__(self, index):
        return self.list[index]

    def traverse(self):
        for element in self.list:
            print(element)

    def traverse_at_index(self,index):
        for element in self.list[index]:
            print(element)

    def dfs(self,element1):
        pass


        # for element in self.list[self.index]:





class graf():
    def __init__(self,edges):
        self.edges=edges
        self.graph_dic={}
        for start,end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start]=[end]

    def get_paths(self,start,end,path=[]):
        path =path+[start]

        if start == end:
            return [path]

        if start not in self.graph_dic:
            return []

        paths=[]

        for node in self.graph_dic[start]:
            # checks that it's not visited before so we dont stuck in the recursion, y3ny mn dubai le newyork then mnnewyork le dubai w leffi bena ya donia
            if node not in path:
                # print(f"node {node}")
                new_paths=self.get_paths(node,end,path)
                # print(f"paths{new_paths}"
                for p in new_paths:
                    # print(p)
                    paths.append(p)
        return paths

    def shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dic:
            return []

        shortest_path=None
        for node in self.graph_dic[start]:
            if node not in path:
                sp=self.shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path







if __name__ == '__main__':
    routes =[("mumbai","paris"),
             ("mumbai","Dubai"),
             ("mumbai","newyork"),
             ("paris","mumbai"),
             ("paris","Dubai"),
             ("Dubai","mumbai"),
             ("Dubai","newyork"),
             ("Dubai","paris")
             ]
    rout=graf(routes)
    print(rout.get_paths("mumbai","newyork"))
    # {'mumbai': ['paris', 'Dubai', 'newyork'],
    # 'paris': ['mumbai', 'Dubai'],
    # 'Dubai': ['mumbai', 'newyork', 'paris']}

    # graf=graph()
    # graf.insert(1,2,3,4)
    # graff=[[9,2],[8,4]]
    # print(graf[0])
    # for j in enumerate(graff):
    #     print (j)


    # graf.traverse()
    # graf.traverse_at_index(0)