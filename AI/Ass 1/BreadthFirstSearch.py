import psutil

def BreadthFirstSearch(problem):
    start_mem = memmory()
    start = problem.start
    goal = problem.goal
    to_explore = []
    explored_and_fringe = set()
    start.f = problem.manhattan(start)
    to_explore.append(start)
    explored_and_fringe.add(start)
    max_fringe = 0
    max_depth = 0
    max_ram = 0
    num_explored = 0

    while to_explore:
        n = to_explore.pop(0)
        if n == goal:
            path_to_goal = problem.path(n, start)
            cost_of_path = len(path_to_goal)
            return (path_to_goal, cost_of_path, num_explored, len(to_explore),max_fringe,cost_of_path, max_depth, max_ram)

        child_nodes = problem.child_nodes(n)
        dist = n.g  # distance of node n from start node
        dist_child_node = dist+1  # distance of every child_node of n from start node
        num_explored +=1

        if max_depth < dist_child_node:
            max_depth = dist_child_node

        for child_node in child_nodes:
            # for every child_node set the node n as parent node,
            # increment by 1 the distance from start and calculate f(n)
            child_node.parent = n
            child_node.g = dist_child_node

            if not child_node in explored_and_fringe:
                explored_and_fringe.add(child_node)
                to_explore.append(child_node)
        if max_fringe < len(to_explore):
            max_fringe = len(to_explore)
        temp_mem = memmory() - start_mem
        if temp_mem > max_ram :
            max_ram = temp_mem
def memmory():
    p = psutil.Process()
    return p.memory_info().rss / 1048576.0
