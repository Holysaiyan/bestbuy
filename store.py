"""
This module defines the Store class representing a store and its operations.
"""
import products


class Store:
    """
    Represents a store and its operations.
    """

    def __init__(self, product):
        """
        Initialize the Store with a list of products.

        Args:
            product (list): A list of products to add to the store.
        """
        self.products = list(product)

    def add_product(self, product):
        """
        Add a product to the store.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Get the total quantity of all products in the store.

        Returns:
            int: The total quantity of products.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        Get a list of all active products in the store.

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
        Place an order for a list of products.

        Args:
            shopping_list (list): A list of (product, quantity) tuples representing the order.

        Returns:
            float: The total cost of the order.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active() and product.get_quantity() >= quantity:
                cost = product.buy(quantity)
                total_cost += cost
            else:
                raise ValueError("Invalid order. Product is out of stock or insufficient quantity.")
        return total_cost


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]
