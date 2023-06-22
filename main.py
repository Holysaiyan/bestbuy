"""
A program that simulates a store and allows users to make orders.
"""

from colorama import Fore, Style
from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, PercentDiscount, ThirdOneFree
from store import Store


def start():
    """
    Display the store menu.
    """
    print("    Store Menu\n    ___________\n1. List all products in store\n2."
          " Show total amount in store\n3. Make an "
          "order\n4. Quit")


def list_products(products):
    """
    List all products in the store.
    """
    product_index = 1
    print("______")
    for product in products:
        print(f"{Fore.RED}{product_index}. {product.show()}{Style.RESET_ALL}")
        product_index += 1
    print("______")


def show_total_amount(store):
    """
    Show the total amount of products in the store.
    """
    total_quantity = store.get_total_quantity()
    print(f"{Fore.YELLOW}Total of {total_quantity} items in store{Style.RESET_ALL}")


def make_order(store, products):
    """
    Make an order for products.
    """
    list_products(products)
    order_list = []
    while True:
        order_choice = input("Which product # do you want? (Enter 0 to finish): ")
        if order_choice == "0":
            if order_list:
                try:
                    total_cost = store.order(order_list)
                    print(f"{Fore.GREEN}Order placed successfully! "
                          f"Total cost: £{total_cost}{Style.RESET_ALL}")
                    break
                except ValueError as error:
                    print(f"{Fore.RED}{str(error)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Shopping cart is empty!{Style.RESET_ALL}")
            break
        try:
            order_choice = int(order_choice)
            if 1 <= order_choice <= len(products):
                selected_product = products[order_choice - 1]
                if isinstance(selected_product, NonStockedProduct):
                    try:
                        order_quantity = int(input("Enter quantity: "))
                        if order_quantity < 1:
                            raise ValueError("Quantity must be a positive value")
                        print(f"{Fore.GREEN}Product added to order!{Style.RESET_ALL}")
                        order_list.append((selected_product, order_quantity))
                    except ValueError as error:
                        print(f"{Fore.RED}{str(error)}{Style.RESET_ALL}")
                elif isinstance(selected_product, LimitedProduct):
                    available_quantity = selected_product.get_quantity()
                    if available_quantity > 0:
                        try:
                            order_quantity = int(input("Enter quantity: "))
                            if 1 <= order_quantity <= available_quantity:
                                print(f"{Fore.GREEN}Product added to order!{Style.RESET_ALL}")
                                order_list.append((selected_product, order_quantity))
                            else:
                                print(f"{Fore.RED}Invalid quantity!{Style.RESET_ALL}")
                        except ValueError:
                            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}Product is out of stock!{Style.RESET_ALL}")
                else:
                    available_quantity = selected_product.get_quantity()
                    print(f"{Fore.YELLOW}Available quantity: {available_quantity}{Style.RESET_ALL}")
                    if available_quantity > 0:
                        try:
                            order_quantity = int(input("Enter quantity: "))
                            if 1 <= order_quantity <= available_quantity:
                                print(f"{Fore.GREEN}Product added to order!{Style.RESET_ALL}")
                                order_list.append((selected_product, order_quantity))
                            else:
                                print(f"{Fore.RED}Invalid quantity!{Style.RESET_ALL}")
                        except ValueError:
                            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}Product is out of stock!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid product number!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")


def main():
    """
    Run the main program.
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = Store(product_list)
    products = best_buy.get_all_products()

    while True:
        start()
        user_choice = input("Please choose a number: ")

        if user_choice == "1":
            list_products(products)

        elif user_choice == "2":
            show_total_amount(best_buy)

        elif user_choice == "3":
            make_order(best_buy, products)

        elif user_choice == "4":
            print(f"{Fore.LIGHTBLUE_EX}Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
