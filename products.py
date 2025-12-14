class Product:
    """Represent a product with a name, price, quantity, and active status."""

    def __init__(self, name, price, quantity):
        """Represent a product with a name, price, quantity, and active status."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """Return the current available quantity of the product."""
        return int(self.quantity)


    def set_quantity(self, quantity):
        """Reduce the product quantity by the given amount and deactivate if it reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False


    def is_active(self):
        """Return whether the product is currently active."""
        return self.active


    def activate(self):
        """Mark the product as active."""
        self.active = True


    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False


    def show(self):
        """Print the product name, price, and current quantity."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """Purchase a given quantity of the product and return the total price."""
        if self.get_quantity() < quantity:
            raise ValueError("Not enough quantity.")
        self.set_quantity(quantity)
        total_price = quantity * self.price
        return float(total_price)


def main():
    """Demonstrate basic usage of the Product class."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()
