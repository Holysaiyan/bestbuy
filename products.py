"""
This module defines the Product class representing a product in the store.
"""
class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If the name is empty or the price/quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input for product")
        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True

    def get_name(self):
        """
        Returns the name of the product.

        Returns:
            str: The name of the product.
        """
        return self._name

    def get_quantity(self):
        """
        Returns the quantity of the product.

        Returns:
            int: The quantity of the product.
        """
        return self._quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.
        """
        if quantity >= 0:
            self._quantity = quantity
            if quantity < 1:
                self.deactivate()
            else:
                self.activate()

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string representation of the product.
        """
        return str(f"{self._name}, Price: £{self._price}, Quantity: {self._quantity}")

    def buy(self, quantity):
        """
        Buys a specified quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the product is inactive or there is insufficient quantity available.
        """
        if not self.active or self._quantity < quantity:
            raise ValueError("Product is out of stock or insufficient quantity.")
        self._quantity -= quantity
        return float(quantity * self._price)
