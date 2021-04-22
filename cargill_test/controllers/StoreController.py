from cargill_test.models.Item import Item
from cargill_test.models.StorePricingRuleFactory import StorePricingRuleFactory


class StoreControllerSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class StoreController(metaclass=StoreControllerSingleton):
    store_items = {}

    def __init__(self):
        pass

    def init_store_items(self):
        factory = StorePricingRuleFactory()

        self.store_items['stv'] = Item('stv', 'Sony TV', 549.99, factory.create_discount_rule())
        self.store_items['cac'] = Item('cac', 'Central AC', 1399.99, factory.create_gifting_rule())
        self.store_items['nsh'] = Item('nsh', 'Nike Shoe', 109.50, factory.create_buy_more_pay_less_rule())
        self.store_items['mch'] = Item('mch', 'Charger', 30.00, None)

    def checkout(self, shopping_list):
        checkout_sum = 0.0
        for item in shopping_list:
            if self.store_items[item]:
                self.store_items[item].to_string()
                checkout_sum += self.store_items[item].price
        return checkout_sum
