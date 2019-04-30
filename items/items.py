import json
import os


ITEMS = os.path.abspath('..') + '\\items\\items.json'


class BaseItem:
    def __init__(self, *args, **kw):
        self.id = kw.get('id')
        self.name = kw.get('name')
        self.description = {}
        self._load()

    def _load(self):
        with open(ITEMS, 'r') as f:
            self.description = json.load(f).get(str(self.id)) or {}
            f.close()

    def __getattr__(self, item):
        return self.description.get(item)

    #def __getattribute__(self, item):
    #    return self.description.get(item)


class Wearable(BaseItem):
    def __init__(self, type_, *args, **kw):
        super(Wearable, self).__init__(*args, **kw)
        self.type = type_


class Weapon(BaseItem):
    def __init__(self, damage, *args, **kw):
        super(Weapon, self).__init__(*args, **kw)
        self.damage = damage


class Empty(BaseItem):
    def __init__(self, *args, **kw):
        super(Empty, self).__init__(*args, **kw)
