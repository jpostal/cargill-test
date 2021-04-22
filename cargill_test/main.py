"""
    Application Entrypoint

"""
from os.path import dirname, realpath
import sys
sys.path.append(dirname(realpath(__file__))) 
from controllers.StoreController import StoreController


if __name__ == '__main__':
    store = StoreController()
    store.init_store_items()

    print('Welcome to our Store!')
    print('Check out our available items:\n')
    print("Item ID \t Name \t\t\t Price")
    for item in store.store_items.items():
        print("{id} \t\t {n} \t\t ${p}".format(id=item[1].item_id, n=item[1].name, p=item[1].price))

    print('\nType item_id of items you want to buy, separated by whitespace.')
    print('Repeat an item_id if you want to buy more than 1.\n')
    shopping_list = input().split()

    total_checkout = store.checkout(shopping_list)
    print("Your total checkout is: ${:.2f}".format(round(total_checkout, 2)))
