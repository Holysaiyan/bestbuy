"""
This module defines the promotions applied to products in a retail system.
"""


from abc import ABC, abstractmethod


class Promotions(ABC):
    """
    Abstract base class for promotions applied to products.
    """

    def __init__(self, name):
        """
        Initializes a new Promotion instance.

        Args:
            name (str): The name of the promotion.
        """
        self._name = name

    def get_name(self):
        """
        Returns the name of the promotion.

        Returns:
            str: The name of the promotion.
        """
        return self._name

    def set_name(self, new_name):
        """
        Sets the name of the promotion.

        Args:
            new_name (str): The new name of the promotion.
        """
        self._name = new_name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the promotion to the product for the specified quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total cost of the product after applying the promotion.
        """
        pass


class SecondHalfPrice(Promotions):
    """
    Represents a promotion where every second item is priced at half the original price.

    Inherits from the Promotions class.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the second half price promotion to the product for the specified quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total cost of the product after applying the promotion.
        """
        if quantity < 2:
            return product.get_price() * quantity
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        total_cost = (full_price_items * product.get_price()) + (half_price_items * (product.get_price() / 2))
        return total_cost


class ThirdOneFree(Promotions):
    """
    Represents a promotion where every third item is free.

    Inherits from the Promotions class.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the third one free promotion to the product for the specified quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total cost of the product after applying the promotion.
        """
        if quantity < 3:
            return product.get_price() * quantity
        else:
            full_price_items = quantity // 3
            free_items = full_price_items
            total_cost = full_price_items * 2 * product.get_price()
            return total_cost


class PercentDiscount(Promotions):
    """
    Represents a promotion where a percentage discount is applied to the product.

    Inherits from the Promotions class.
    """

    def __init__(self, name, percent):
        """
        Initializes a new PercentDiscount instance.

        Args:
            name (str): The name of the promotion.
            percent (float): The percentage discount.
        """
        super().__init__(name)
        self._percent = percent

    def get_percent(self):
        """
        Returns the percentage discount of the promotion.

        Returns:
            float: The percentage discount.
        """
        return self._percent

    def set_percent(self, new_percent):
        """
        Sets the percentage discount of the promotion.

        Args:
            new_percent (float): The new percentage discount.
        """
        self._percent = new_percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the percent discount promotion to the product for the specified quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total cost of the product after applying the promotion.
        """
        discounted_price = product.get_price() * (1 - self.get_percent() / 100)
        return discounted_price * quantity
