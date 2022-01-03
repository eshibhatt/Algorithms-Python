#consider here, code of a binary search tree, where BFS will operate
#paste the below code as a method to a BST

#bfs by iteration
def bfs(self):
    currentNode=self.root
    lst=[] #holds the result of BFS
    que=[] #keeps track of the current level, so we can access the children

    que.append(currentNode) #initial in que is the currentNode

    while(que.length>0):
        currentNode=que[0]
        que.popleft()
        #uncomment below to see the hierarchy
        #print(currentNode.value)
        lst.append(currentNode.data)
        
        #checking child nodes
        if currentNode.left :
            que.append(currentNode.left)
        if currentNode.right :
            que.append(currentNode.right)

#bfs by recursion

def breadthFirstSearch(self,que,lst):
    #we will take que & lst as input in recur
    #initialising will reset the value, everytime it recurs
    if len(que)==0:
        return lst
    currentNode=self.que
    lst.append(currentNode.data)
    if currentNode.left :
            que.append(currentNode.left)
    if currentNode.right :
        que.append(currentNode.right)
    return self.breadthFirstSearch(que,lst)