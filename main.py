import json
import math
datae = json.load(open("tree.json"))
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)

    def preorder(self):
        print(self.data, end=" ")
        for i in range(len(self.children)):
            self.children[i].preorder()

    def postorder(self):

        for i in range(len(self.children)):
            self.children[i].postorder()
        print(self.data, end=" ")

    def inorder(self):
        counter = 0
        x = math.ceil(len(self.children) / 2)
        for i in range(math.ceil(len(self.children) / 2)):
            self.children[i].inorder()
        print(self.data, end=" ")
        for i in range(x, len(self.children)):
            self.children[i].inorder()

def buildtree(data):
    counter = 0
    if data != None:
        for k,v in data.items():
            if k != "data":
                k = Node(k)
                for j,l in v.items():
                    counter+=1
                    if j != "data":
                        k.add_child(buildtree({j:l}))
                    if len(v) == counter:
                        return k

if __name__ == '__main__':
    val = buildtree(datae)
    val.preorder()
    print()
    val.inorder()
    print()
    val.postorder()