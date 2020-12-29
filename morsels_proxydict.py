# https://www.pythonmorsels.com/exercises/75e70eca18624b3dbf815daae3d8d361/submit/1/
"""
Problem Statement
Hello!

This week I'd like you to create a ProxyDict class which offers an immutable dictionary-like
interface that wraps around a given dictionary.

>>> user_data = {'name': 'Trey Hunner', 'active': False}
>>> proxy_data = ProxyDict(user_data)
>>> proxy_data.keys()
dict_keys(['name', 'active'])
>>> proxy_data['name']
'Trey Hunner'
>>> proxy_data['active']
False
>>> proxy_data['active'] = False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ProxyDict' object does not support item assignment
The ProxyDict class should support key lookups and should have a keys method.

Note that if the original dictionary passed to ProxyDict changes,
our ProxyDict object should change as well. Put another way,
our ProxyDict instances shouldn't copy the dictionary given to them but should wrap around it,
"proxying" to it.

>>> user_data = {'name': 'Trey Hunner', 'active': False}
>>> proxy_data = ProxyDict(user_data)
>>> user_data['active'] = True
>>> proxy_data['active']
True
Bonus 1

For the first bonus, I'd like you to make your ProxyDict class
support for the built-in len function, and add items, values, and get methods (just like the ones that dictionaries have).

>>> user_data = {'name': 'Trey Hunner', 'active': False}
>>> proxy_data = ProxyDict(user_data)
>>> len(proxy_data)
2
>>> proxy_data.items()
dict_items([('name', 'Trey Hunner'), ('active', False)])
>>> proxy_data.values()
dict_values(['Trey Hunner', False])
>>> proxy_data.get('name')
'Trey Hunner'
>>> proxy_data.get('shoe_size', 0)
0
Bonus 2

For the second bonus, I'd like you to allow your ProxyDict
objects to be iterable and I'd like them to have a nice string representation.

>>> user_data = {'name': 'Trey Hunner', 'active': False}
>>> proxy_data = ProxyDict(user_data)
>>> for key in proxy_data:
...     print(key)
...
'name'
'active'
>>> proxy_data
ProxyDict({'name': 'Trey Hunner', 'active': False})
Bonus 3

For the third bonus, your ProxyDict objects should support
equality with other dictionaries and other ProxyDict instances:

>>> user_data = {'name': 'Trey Hunner', 'active': False}
>>> p1 = ProxyDict(user_data)
>>> p2 = ProxyDict(user_data.copy())
>>> p1 == p2
True
>>> p2 == user_data
True
"""


class ProxyDict:
    def __init__(self, data: dict):
        self._dict = data
        self._keys, self._values = self._dict.keys(), self._dict.values()
        self._len = len(self._dict)

    def __len__(self):
        return self._len

    def __getitem__(self, i):
        return self._dict[i]

    def __iter__(self):
        return iter(self._keys)

    def __eq__(self, other):
        if isinstance(other, ProxyDict):
            return self._dict == other._dict
        else:
            raise NotImplementedError()

    def __repr__(self):
        return f"ProxyDict({self._dict})"

    def keys(self) -> list:
        return [k for k in self._dict.keys()]

    def items(self) -> list:
        return [(i, v) for i, v in zip(self._dict.keys(), self._dict.values())]

    def values(self) -> list:
        return [v for v in self._dict.values()]

    def get(self, ky, val=None):
        self._key = ky
        self._value = val

        if self._key not in self._dict.keys():
            return self._value
        else:
            return self._dict[self._key]
