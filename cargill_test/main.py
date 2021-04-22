"""
    Application Entrypoint

"""

from controllers.StoreController import StoreController


if __name__ == '__main__':
    store = StoreController()
    store.init_store_items()

    print('Welcome to our Store!')
    print('Type item_id of items you want to buy, separated by whitespace.')
    print('Repeat an item_id if you want to buy more than 1.')
    shopping_list = input().split()

    total_checkout = store.checkout(shopping_list)
    print("Your total checkout is: ${:.2f}".format(round(total_checkout, 2)))

