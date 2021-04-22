from __future__ import annotations
from abc import ABC, abstractmethod


class PricingRule(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def apply_pricing_rule(self, item, shopping_list) -> None:
        pass
