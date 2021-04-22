from cargill_test.models.interfaces.PricingRule import PricingRule


class BuyMorePayLessRule(PricingRule):

    def __init__(self):
        pass

    def apply_pricing_rule(self) -> str:
        return "BuyMorePayLessRule"
