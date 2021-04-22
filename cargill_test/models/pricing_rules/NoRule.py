"""
    This is not a rule stated on problem but once some items don't have any rules,
    I personally think its better this than assign None.
"""

from cargill_test.models.interfaces.PricingRule import PricingRule


class NoRule(PricingRule):

    def __init__(self):
        super().__init__()

    def apply_pricing_rule(self, item, shopping_list) -> float:
        return 0.0

    def to_string(self) -> str:
        return "No Rule"
