class Product:
    """Represents a product with a name, price, quantity, and active status."""

    def __init__(self, name, price, quantity):
        """
        Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product (must be >= 0).
            quantity (int): The available quantity (must be >= 0).

        Raises:
            ValueError: If name is empty, or price/quantity are negative.
        """
        if name == "":
            raise ValueError("Sorry, name of product missing")
        elif price < 0:
            raise ValueError("Sorry, negative price is not possible.")
        elif quantity < 0:
            raise ValueError("Sorry, negative quantity is not possible")

        self.active = True
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self) -> int:
        """
        Returns:
            int: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the product's quantity.

        Args:
            quantity (int): The new quantity value (must be >= 0).

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Sets the product status to active.
        """
        self.active = True

    def deactivate(self):
        """
        Sets the product status to inactive.
        """
        self.active = False

    def show(self):
        """
        Prints a string that represents the product.
        Format: "<name>, Price: <price>, Quantity: <quantity>"
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Processes a purchase of the product.

        Decreases the quantity accordingly and deactivates the product
        if the quantity reaches zero.

        Args:
            quantity (int): The quantity to purchase (must be > 0).

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If quantity is not positive or not enough in stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")

        quantity_in_stock = self.get_quantity()
        if quantity_in_stock >= quantity:
            quantity_in_stock -= quantity
            self.set_quantity(quantity_in_stock)
            if quantity_in_stock == 0:
                self.deactivate()
            return float(self.price * quantity)
        else:
            raise ValueError("Sorry, there is not enough in stock")


# Example usage:
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
