

"""
Eight puzzle problem.
"""

from Node import Node
from State import State


class EightPuzzleProblem(object):
    """
    Representations of:
        - 8-puzzle problem
        - successors function,
        - g(n)
        - h(n)
        - the function that returns the problem's solution (if it exists).
    """

    def __init__(self, start, goal):
        self._start = Node(start)
        self._goal = Node(goal)
    @property
    def start(self) :
        return self._start

    @property
    def goal(self) :
        return self._goal

    def get_coord(self, num):
	    return (num/3, num%3)

    def get_list_pos(self, x, y):
        '''
           Given the coordinates,
           it returns the respective position in a list of positions.
        '''
        pos = ((x * 3) + y )
        return pos

    def manhattan(self, n):
        """
            Manhattan distance
        """
        distance = 0
        values = n.state.tiles
        for v in values:
            x1, y1 = self.get_coord(values.index(v))
            x2, y2 = self.get_coord(v)
            d = abs(x1 - x2) + abs(y1 - y2)
            distance += d
        return distance

    def f(self, n):
        """
            f(n) = g(n) + h(n)
        """
        return (n.g + self.manhattan(n))

    # Path of the solution from start node
    def path(self, goal, start):
        new_goal = goal
        path = []
        while not new_goal == start:
            path = [new_goal.move] + path
            new_goal = new_goal.parent
        return path

    # child_nodes function defined for the context of the 8-puzzle game
    def child_nodes(self, node):
        nodes = []
        state = node.state
        empty = state.tiles.index(0)
        x, y = self.get_coord(empty)

        # up
        if x > 0:
            new_x = x - 1
            new_y = y
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.tiles[idx]
            new_state = State(state.tiles)
            new_state.tiles[idx] = 0
            new_state.tiles[empty] = swap_value
            n = Node(new_state)
            n.move = 'Up'
            nodes.append(n)

        # down
        if x < 2:
            new_x = x + 1
            new_y = y
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.tiles[idx]
            new_state = State(state.tiles)
            new_state.tiles[idx] = 0
            new_state.tiles[empty] = swap_value
            n = Node(new_state)
            n.move = 'Down'
            nodes.append(n)

        # left
        if y > 0:
            new_x = x
            new_y = y - 1
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.tiles[idx]
            new_state = State(state.tiles)
            new_state.tiles[idx] = 0
            new_state.tiles[empty] = swap_value
            n = Node(new_state)
            n.move = 'Left'
            nodes.append(n)

        # right
        if y < 2:
            new_x = x
            new_y = y+1
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.tiles[idx]
            new_state = State(state.tiles)
            new_state.tiles[idx] = 0
            new_state.tiles[empty] = swap_value
            n = Node(new_state)
            n.move = 'Right'
            nodes.append(n)

        #return child_nodes list generated according to the possibile moves
        return nodes
