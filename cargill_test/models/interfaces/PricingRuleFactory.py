from __future__ import annotations
from abc import ABC, abstractmethod
from cargill_test.models.interfaces.PricingRule import PricingRule


class PricingRuleFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_buy_more_pay_less_rule(self) -> PricingRule:
        pass

    @abstractmethod
    def create_discount_rule(self) -> PricingRule:
        pass

    @abstractmethod
    def create_gifting_rule(self) -> PricingRule:
        pass

    @abstractmethod
    def create_no_rule(self) -> PricingRule:
        pass
