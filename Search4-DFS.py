#consider here, code of a binary search tree, where BFS will operate
#paste the below code as a method to a BST

def DFSInorder():
    return traverseInOrder(self.root,[])

def DFSPostorder():
    return traversePostOrder(self.root,[])

def DFSPreorder():
    return traversePreOrder(self.root,[])

def traverseInorder(node,lst):
    #we traverse left -->right
    if node.left!=None:
        #we traverse left as long as it doesn't hit an end
        traverseInorder(node.left,lst)
    list.append(node.data) #pushes the value of the node, after which nothing

    if node.right!=None:
        traverseInorder(node.right,lst)


#the only difference in the other two is op of list.push
def traversePreOrder(node,lst):
    list.append(node.data) #pushes the root node 1st
    #then goes on accessing children left-->right
    if node.left!=None:
        traversePreOrder(node.left,lst)
    if node.right!=None:
        traversePreOrder(node.right,lst)

def traversePostOrder(node,lst):
    #children accessed left-->right
    if node.left!=None:
        traversePostOrder(node.left,lst)
    if node.right!=None:
        traversePostOrder(node.right,lst)
    list.append(node.data)

#space complexity O(height of the tree)