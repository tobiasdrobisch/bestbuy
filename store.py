from products import Product
from typing import List, Tuple


class Store:
    """
    A class that represents a store with a list of products.
    """

    def __init__(self, list_of_products: List[Product]):
        """
        Initialize the store with a list of products.

        Args:
            list_of_products (List[Product]): List of Product instances.
        """
        self.list_of_products = list_of_products

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.list_of_products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        self.list_of_products = [
            item for item in self.list_of_products if item != product
        ]

    def get_total_quantity(self) -> int:
        """Return total quantity of all products in store."""
        return sum(product.get_quantity() for product in self.list_of_products)

    def get_all_products(self) -> List[Product]:
        """Return all active products."""
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Process an order and return total price.

        Args:
            shopping_list (List[Tuple[Product, int]]): List of (product, quantity) tuples.

        Returns:
            float: Total cost of the order.
        """
        total_price = 0.0

        for ordered_product, quantity in shopping_list:
            if ordered_product in self.list_of_products:
                total_price += ordered_product.buy(quantity)
            else:
                raise ValueError(f"{ordered_product.name} not found in store.")

        return total_price
