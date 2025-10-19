class Product:
    """Represents a product with a name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product (must be >= 0).
            quantity (int): The available quantity (must be >= 0).
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set a new quantity for the product.

        Args:
            quantity (int): New quantity (must be >= 0).
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print product details."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Process a purchase.

        Args:
            quantity (int): Quantity to purchase.

        Returns:
            float: Total price.

        Raises:
            ValueError: If not enough stock or invalid quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if self.quantity >= quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            return self.price * quantity
        else:
            raise ValueError(
                f"Insufficient stock. Available: {self.quantity}."
            )
