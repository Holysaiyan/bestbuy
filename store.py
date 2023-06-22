"""
This module defines the Store class representing a store and its operations.

Class:
    Store:
        Represents a store and provides methods for managing products and placing orders.

Methods:
    __init__(self, product):
        Initializes the Store object with a list of products.

    add_product(self, product):
        Adds a product to the store.

    remove_product(self, product):
        Removes a product from the store.

    get_total_quantity(self):
        Retrieves the total quantity of all products in the store.

    get_all_products(self):
        Retrieves a list of all active products in the store.

    order(self, shopping_list):
        Places an order for a list of products and calculates the total cost of the order.

        Args:
            shopping_list (list): A list of tuples containing a product and its desired quantity.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If an invalid order is encountered, such as a product being out of stock or insufficient quantity.
"""
import products


class Store:
    """
    Represents a store and provides methods for managing products and placing orders.
    """

    def __init__(self, product):
        """
        Initializes the Store object with a list of products.

        Args:
            product (list): A list of products to add to the store.
        """
        self.products = list(product)

    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Retrieves the total quantity of all products in the store.

        Returns:
            int: The total quantity of products.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        Retrieves a list of all active products in the store.

        Returns:
            list: A list of active products.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Places an order for a list of products and calculates the total cost of the order.

        Args:
            shopping_list (list): A list of tuples containing a product and its desired quantity.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If an invalid order is encountered, such as a product being out of stock or insufficient quantity.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active() and product.get_quantity() >= quantity:
                cost = product.buy(quantity)
                total_cost += cost
            elif isinstance(product, products.LimitedProduct):
                if product.get_maximum() > quantity:
                    raise ValueError(f"You can only get {product.get_maximum()} of this item")
                else:
                    cost = product.buy(quantity)
                    total_cost += cost
            elif isinstance(product, products.NonStockedProduct):
                if quantity > product.get_quantity():
                    cost = product.buy(quantity)
                    total_cost += cost
            else:
                raise ValueError("Invalid order. Product is out of stock or insufficient quantity.")
        return total_cost
