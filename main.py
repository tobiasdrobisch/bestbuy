from store import Store
from products import Product


def start(marketstore: Store):
    """
    Start the store menu loop.

    Args:
        marketstore (Store): The store instance.
    """
    while True:
        print("    Store Menu")
        print("--------------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            user_input = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if user_input == 1:
            print("------")
            for product in marketstore.list_of_products:
                product.show()
            print("------")

        elif user_input == 2:
            print(f"Total quantity in store: {marketstore.get_total_quantity()}")

        elif user_input == 3:
            shopping_list = []
            while True:
                print("------")
                for idx, product in enumerate(marketstore.list_of_products, start=1):
                    print(f"{idx}.", end=" ")
                    product.show()
                print("------")
                print("When you want to finish order, enter empty input.")

                product_number = input("Which product # do you want? ").strip()
                if product_number == "":
                    break

                amount = input("What amount do you want? ").strip()
                if amount == "":
                    break

                try:
                    product_index = int(product_number) - 1
                    quantity = int(amount)
                    selected_product = marketstore.list_of_products[product_index]
                    shopping_list.append((selected_product, quantity))
                except (ValueError, IndexError):
                    print("Invalid product number or quantity.")
                    continue

            try:
                total_price = marketstore.order(shopping_list)
                print(f"Order cost: {total_price} dollars.")
            except ValueError as e:
                print(f"Error processing order: {e}")

        elif user_input == 4:
            print("Exiting store. Goodbye!")
            return

        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    # Setup initial stock
    initial_products = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(initial_products)

    start(best_buy)
