from collections import deque
def bfs(start_node, goal_node):
    explored = set()
    to_explored = deque([])
    to_explored.append(start_node)
    while len(to_explored) > 0:
         currNode = to_explored.popleft()
         print currNode
         if currNode == goal_node:
             return 'Success'
         '''else :
             print 'Failure' '''
         child_nodes = currNode.child_nodes
         for child in child_nodes:
             if not child in explored:
	             to_explored.append(child)
         explored.add(currNode)
    return 'Failure'
	

class Node(object):
    """
    Node of the graph used for a search problem.
    """

    def __init__(self, state=None, first_child_nodes = None, second_child_nodes = None):
        self.__state = state
        self.first_child_nodes = first_child_nodes
        self.second_child_nodes = second_child_nodes

    @property
    def state(self):
        return self.__state

    @property
    def child_nodes(self):
        
        return [self.first_child_nodes, self.second_child_nodes] if self.first_child_nodes and self.second_child_nodes else []


    def __repr__(self):
        return str(self.__state)

    def __str__(self):
        return str(self.__state)

    def __eq__(self, node):
        return self.__state == node.state

    def __neq__(self, node):
        return self.__state != node.state

    def __lt__(self, node):
        return self.__state < node.state

    def __gt__(self, node):
        return self.__state > node.state

    def __le__(self, node):
        return self.__state >= node.state

    def __ge__(self, node):
        return self.__state >= node.state
    def __hash__(self):
        """
        Hash of the current configuration.
        """
        return hash(self.__state)
if __name__ == '__main__':
    nodeM = Node('M')
    nodeH = Node('H')
    nodeK = Node('K')
    nodeL = Node('L')
    nodeJ = Node('J')
    nodeF = Node('F')
    nodeG = Node('G')
    nodeE = Node('E')
    nodeI = Node('I', first_child_nodes = nodeK, second_child_nodes = nodeL)
    nodeD = Node('D', first_child_nodes = nodeI, second_child_nodes = nodeJ)
    nodeB = Node('B', first_child_nodes = nodeD, second_child_nodes = nodeE)
    nodeC = Node('C', first_child_nodes = nodeF, second_child_nodes = nodeG)
    nodeA = Node('A', first_child_nodes = nodeB, second_child_nodes = nodeC)
    '''print bfs(nodeA, nodeM)
    print bfs(nodeA, nodeA)
    print bfs(nodeA, nodeB)
    print bfs(nodeA, nodeC)'''
    print bfs(nodeA, nodeJ)
    '''print bfs(nodeA, nodeE)
    print bfs(nodeA, nodeF)
    print bfs(nodeA, nodeG)
    print bfs(nodeA, nodeH)'''
    
	