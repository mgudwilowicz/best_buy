from products import Product


class Store:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)


    def remove_product(self, product):
        self.list_of_products.remove(product)


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.get_quantity()
        return int(total_quantity)

    def get_all_products(self):
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        price = 0
        for order in shopping_list:
            product, quantity = order
            price += product.buy(quantity)

        return price



def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    product_list = [mac, bose, pixel]

    media_mark = Store(product_list)

    products = media_mark.get_all_products()

    print(media_mark.get_total_quantity())
    print(media_mark.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()
