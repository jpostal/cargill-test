"""
    Item Model class.
"""


class Item:
    def __init__(self, item_id, name, price, pricing_rule):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.pricing_rule = pricing_rule

    def to_string(self):
        print('Item_id: {id} -- Name: {n} -- Price: ${p} -- Pricing Rule: {r}'.format(id=self.item_id, n=self.name,
                                                                                      p=self.price,
                                                                                      r=self.pricing_rule.to_string()))
