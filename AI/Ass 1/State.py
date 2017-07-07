
class State(object):
    """
    Representation of a problem's state.
    """

    def __init__(self, tiles=None):
        self._tiles = []
        self._tiles.extend(tiles)

    @property
    def tiles(self):
        return self._tiles

    def __str__(self):
        return str(self._tiles)

    def __repr__(self):
        return str(self._tiles)

    def __eq__(self, other):
        return self._tiles == other.tiles
