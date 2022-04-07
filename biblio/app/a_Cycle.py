# https://stackoverflow.com/questions/44611890/itertools-previous-opposite-of-next-python

import itertools as it

class Cycle:
    """Wrap cycle."""
    def __init__(self, seq):
        self._container = it.cycle(seq)
        self._here = None
        self.prev = None

    def __iter__(self):
        return self._container

    def __next__(self):
        self.prev = self._here
        self._here = next(self._container)
        return self._here