

class Node(object):
    """
    Node of the graph used for a search problem.
    """

    def __init__(self, state=None):
        self.__state = state
        self.__parent = None
        self.__g = 0
        self.__f = 0
        self.__move = None

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def move(self):
        return self.__move

    @move.setter
    def move(self, move):
        self.__move = move

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, cost):
        self.__g = cost

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, cost):
        self.__f = cost

    def __repr__(self):
        return str(self.__state)

    def __str__(self):
        return str(self.__state)

    def __eq__(self, node):
        return self.__state.tiles == node.state.tiles

    def __neq__(self, node):
        return self.__state.tiles != node.state.tiles

    def __lt__(self, node):
        return self.__f < node.f

    def __gt__(self, node):
        return self.__f > node.f

    def __le__(self, node):
        if self.__f == node.f:
            return self.__g > node.g
        else:
            return self.__f < node.f

    def __ge__(self, node):
        if self.__f == node.f:
            return self.__g < node.g
        else:
            return self.__f > node.f
    def __hash__(self):
        """
        Hash of the current configuration.
        """
        return hash(tuple(self.__state.tiles))
