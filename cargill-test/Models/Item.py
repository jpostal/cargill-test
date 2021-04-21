

class Item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def to_string(self):
        print('Item_id: {id} -- Name: {n} -- Price: ${p}'.format(id=self.item_id, n=self.name, p=self.price))
