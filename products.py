"""
This module defines the Product class representing a product in the store.
"""
import promotions


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
        self._promotion = None
        self.active = True

    def get_name(self):
        """
        Returns the name of the product.

        Returns:
            str: The name of the product.
        """
        return self._name

    def set_name(self, name):
        """
        Sets the name of the product
        """
        self._name = name

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
            if quantity == 0:
                self.deactivate()
            else:
                self.activate()

    def get_price(self):
        """
        Returns the price of the product.

        Returns:
            float: The price of the product
        """
        return self._price

    def set_price(self, price):
        """
        Sets the price of the product
        """
        self._price = price

    def get_promotion(self):
        """
        Returns the promotion applied to the product.

        Returns:
            Promotion: The promotion applied to the product.
        """
        return self._promotion

    def set_promotion(self, promotion):
        """
        Sets the promotion for the product.

        Args:
            promotion (Promotion): The promotion instance to set.

        Raises:
            ValueError: If the promotion is not an instance of the Promotion class.
        """
        if not isinstance(promotion, promotions.Promotion):
            raise ValueError("Invalid promotion. Must be an instance of the Promotion class.")
        self._promotion = promotion

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
        return str(f"{self.get_name()}, Price: £{self.get_price()}, Quantity: {self.get_quantity()}")

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

        if self._quantity == 0:
            self.deactivate()

        return float(quantity * self.get_price())


class NonStockProducts(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string representation of the product.
        """
        return f"{self.get_name()}, and the price is £{self.get_price()}"

    def buy(self, quantity):
        """
        Buys a specified quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total cost of the purchase.
        """
        return quantity * self.get_price()


class LimitedProduct(Product):
    """
    Initializes a new LimitedProduct instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
            maximum (int): The maximum order limit for the product.

        Raises:
            ValueError: If the name is empty, or the price/quantity/maximum is negative.

    """
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def get_maximum(self):
        """
        Returns the maximum order limit for the product.

        Returns:
            int: The maximum order limit.

        """
        return self._maximum

    def set_maximum(self, maximum):
        """
        Sets the maximum order limit for the product.

        Args:
            maximum (int): The new maximum order limit.

        """
        self._maximum = maximum

    def buy(self, quantity):
        """
        Buys a specified quantity of the limited product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the quantity exceeds the maximum order limit.

        """
        if quantity > self._maximum:
            raise ValueError("The quantity exceeds the maximum order limit")

        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)

        self.set_quantity(self.get_quantity() - quantity)

        return float(quantity * self.get_price())





# product_test = LimitedProduct("Shipping", 100, 200, 1)
# print(product_test.get_quantity())
# print(product_test.buy(1))
# print(product_test.get_quantity())