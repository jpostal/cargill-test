from cargill_test.models.interfaces.PricingRuleFactory import PricingRuleFactory
from cargill_test.models.interfaces.PricingRule import PricingRule
from cargill_test.models.pricing_rules.BuyMorePayLessRule import BuyMorePayLessRule
from cargill_test.models.pricing_rules.DiscountRule import DiscountRule
from cargill_test.models.pricing_rules.GiftingRule import GiftingRule


class StorePricingRuleFactory(PricingRuleFactory):

    def __init__(self):
        pass

    def create_buy_more_pay_less_rule(self) -> PricingRule:
        return BuyMorePayLessRule()

    def create_discount_rule(self) -> PricingRule:
        return DiscountRule()

    def create_gifting_rule(self) -> PricingRule:
        return GiftingRule()
