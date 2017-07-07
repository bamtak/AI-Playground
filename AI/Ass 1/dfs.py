from collections import deque
def dfs(start_node, goal_node, tree):
    explored = set()
    to_explored = []
    to_explored.append(start_node)
    while len(to_explored) > 0:
         currNode = to_explored.pop()
         print currNode
         if currNode == goal_node:
             return 'Success'
         else :
             print 'Failure' 
         if currNode in tree.keys():
             child_nodes = tree[currNode]
             for child in child_nodes[::-1]:
                 if not child in explored:
	                 to_explored.append(child)
         explored.add(currNode)
    return 'Failure'
	

if __name__ == '__main__':
    tree = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C':['F', 'G'], 'D':['H', 'I'], 'H': ['J', 'K']}
    print dfs('A', 'J', tree)
    #print bfs('A', 'G', tree)
    #print bfs('A', 'H', tree)
    #print bfs('A', 'Q', tree)
    #print bfs('A', 'Y', tree)
    
	