"""
    This class contains logic for the following rule stated on problem:
    1. We have a 3 for 2 great deal on Nike Shoes. i.e. if you buy 3 Nike Shoes, you’ll just pay the price of 2.

    If I want something different, I need to change just this class :) (Y)
"""
from cargill_test.models.interfaces.PricingRule import PricingRule


class BuyMorePayLessRule(PricingRule):

    _items_to_buy = 3
    _items_to_pay = 2
    _discount_applied = False
    _discount_amount = 0.0

    def __init__(self):
        super().__init__()

    def apply_pricing_rule(self, item, shopping_list) -> float:
        if self._discount_applied:
            return 0.0

        item_count = shopping_list.count(item.item_id)
        times_to_discount = item_count / self._items_to_buy
        if times_to_discount >= 1:
            self._discount_amount = int(times_to_discount) * item.price
            self._discount_applied = True

        return self._discount_amount
