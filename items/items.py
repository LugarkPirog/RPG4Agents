import json
import os
import sys
import logging

if __name__ == '__main__':
    base_path = '.'
    sys.path.insert(0, os.path.abspath('.'))
else:
    base_path = '.'

from settings import DEBUG


if DEBUG:
    logging.basicConfig(level=logging.DEBUG)

ITEMS = os.path.abspath(base_path) + '/items/items.json'


class BaseItem(object):
    def __init__(self, *args, **kw):

        logging.debug('BaseItem init kw: ' + str(kw))

        def load(id):
            with open(ITEMS, 'r') as f:
                description = json.load(f).get(str(id)) or {}
                f.close()
            logging.debug('BaseItem init load descr: ' + str(description))
            return description

        self.description = load(kw.get('id'))


    # def __getattr__(self, item):
    #     return self.description.get(item)

    # def __getattribute__(self, item):
    #     return self.description.get(item)

    def __getitem__(self, item):
        return self.description.get(item)


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


if __name__ == '__main__':
    i = BaseItem(id='1')
    print(i['damage'])
