"""
    This class contains logic for the following rule stated on problem:
    2. Sony TV will have a Bulk discount, where the price will drop to $499.99 each, if someone buys more
    than 4.

    If I want something different, I need to change just this class :) (Y)
"""
from cargill_test.models.interfaces.PricingRule import PricingRule


class DiscountRule(PricingRule):

    _items_to_buy = 4
    _new_price = 499.99
    _discount_amount = 0.0
    _discount_applied = False

    def __init__(self):
        super().__init__()

    def apply_pricing_rule(self, item, shopping_list) -> float:
        if self._discount_applied:
            return 0.0

        item_count = shopping_list.count(item.item_id)
        if item_count > self._items_to_buy:
            self._discount_amount = item_count * (item.price - self._new_price)
            self._discount_applied = True
        return self._discount_amount

    def to_string(self) -> str:
        return "Discount Rule"
