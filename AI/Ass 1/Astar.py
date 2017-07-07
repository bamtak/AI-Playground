
import heapq
import psutil

def Astar(problem):
    start_mem = memmory()
    start = problem.start
    goal = problem.goal

    # Create a list to_explore that will be managed as an ordered heap according to f(n) = g(n) + h(n).

    to_explore = []
    explored = set()
    start.f = problem.manhattan(start)
    heapq.heappush(to_explore, start)
    max_fringe = 0
    max_depth = 0
    max_ram = 0

    while to_explore:
        n = heapq.heappop(to_explore)
        explored.add(n)
        if n == goal:
            path_to_goal = problem.path(n, start)
            cost_of_path = len(path_to_goal)
            return (path_to_goal, cost_of_path, len(explored)-1, len(to_explore),max_fringe,cost_of_path, max_depth, max_ram)

        child_nodes = problem.child_nodes(n)
        dist = n.g  # distance of node n from start node
        dist_child_node = dist+1  # distance of every child_node of n from start node

        if max_depth < dist_child_node:
            max_depth = dist_child_node

        for child_node in child_nodes:
            # for every child_node set the node n as parent node,
            # increment by 1 the distance from start and calculate f(n)
            child_node.parent = n
            child_node.g = dist_child_node
            child_node.f = problem.f(child_node)

            state = child_node.state

            if not child_node in to_explore and not child_node in explored:
                heapq.heappush(to_explore, child_node)
        if max_fringe < len(to_explore):
            max_fringe = len(to_explore)
        temp_mem = memmory() - start_mem
        if temp_mem > max_ram :
            max_ram = temp_mem

def memmory():
    p = psutil.Process()
    return p.memory_info().rss / 1048576.0
