"""
    This class contains logic for the following rule stated on problem:
    3. We will add an additional Charger free of cost with every Central AC sold.

    If I want something different, I need to change just this class :) (Y)
"""
from typing import List

from cargill_test.models.interfaces.PricingRule import PricingRule
from cargill_test.models.pricing_rules.NoRule import NoRule
from cargill_test.models.Item import Item


class GiftingRule(PricingRule):

    _discount_amount = 0.0
    _gift_item = Item('mch', 'Charger', 30.00, NoRule())
    _discount_applied = False

    def __init__(self):
        super().__init__()

    def apply_pricing_rule(self, item, shopping_list) -> float:
        if self._discount_applied:
            return 0.0

        item_count = shopping_list.count(item.item_id)
        gift_count = shopping_list.count(self._gift_item.item_id)
        count = min(item_count, gift_count)
        self._discount_amount = count * self._gift_item.price
        self._discount_applied = True

        return self._discount_amount
