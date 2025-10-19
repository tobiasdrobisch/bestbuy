import products

class Store():

    list_of_products = []

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)


    def remove_product(self, product):
        self.list_of_products = [item for item in self.list_of_products if item != product]

    '''Removes
    a
    product
    from store.'''


    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.get_quantity()

        return total_quantity

    '''Returns
    how
    many
    items
    are in the
    store in total.'''

    def get_all_products(self) -> list[products.Product]:
        return [product for product in self.list_of_products if product.is_active()]


    '''Returns
    all
    products in the
    store
    that
    are
    active.'''

    def order(self, shopping_list) -> float:
        total_price = 0.0

        for product_to_buy in shopping_list:
            for product_in_store in self.list_of_products:
                if product_to_buy[0].name == product_in_store.name:
                    total_price += product_in_store.buy(product_to_buy[1])

        return total_price


    '''Gets
    a
    list
    of
    tuples, where
    each
    tuple
    has
    2
    items:
    Product(Product

    class ) and quantity (int).
    Buys the products and returns the total price of the order.'''


bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

best_buy = Store([bose, mac])
price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")

print("--------------------------------------------------------")
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))