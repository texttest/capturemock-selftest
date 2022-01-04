from collections.abc import MutableMapping

class MyDict(MutableMapping):
    def __init__(self, **kwargs):
        self._dict = dict(kwargs)
    def __delitem__(self):
        del self._dict[key]
    def __getitem__(self, key):
        return self._dict[key]
    def __setitem__(self, key, val):
        self._dict[key] = val
    def __iter__(self):
        return iter(self._dict)
    def __len__(self):
        return len(self._dict)
