from products import Product
from store import Store

product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
media_markt = Store(product_list)


def show_active_products(store):
    """Display all active products in the store with their price and available quantity."""
    products = store.get_all_products()
    print('-----')
    for i, product in enumerate(products, start=1):
        print(f'{i}. {product.name}, Price: {product.price}, Quantity: {product.quantity}')
    print('-----')


def order(store):
    """Allow the user to create an order by selecting products and quantities from the store."""
    show_active_products(store)
    my_list= []
    print('When you want to finish order, enter empty text.')

    while True:
        user_input_product = input(
            'Which product # do you want? '
        )
        if user_input_product == '':
            break

        user_input_amount = int(input('What amount do you want? '))

        user_product = store.get_all_products()[int(user_input_product) - 1]

        my_list.append((user_product, user_input_amount))
        print('Product added to list!\n')

    print(f'Order made! Total payment: {store.order(my_list)}')


def start(store):
    """Run the main store menu loop and handle user actions."""
    while True:
        user_input = input(
            '\n********** Store Menu **********\n'
            '1. List all products in store\n'
            '2. Show total amount in store\n'
            '3. Make an order\n'
            '4. Quit\n'
            'Please choose a number: '
        ).strip()

        try:
            user_input = int(user_input)
        except ValueError:
            print("Choose a number between 1 and 4")
            continue

        if user_input == 1:
            show_active_products(store)
        elif user_input == 2:
            print(f'Total of {store.get_total_quantity()} items in store')
        elif user_input == 3:
            order(store)
        elif user_input == 4:
            break


def main():
    """Start the store application."""
    start(media_markt)


if __name__ == "__main__":
        main()

