from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract class representing a promotion for a product.
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
        returns the name of the promotion
        """
        return self._name

    def set_name(self, name):
        """
        sets the name of the promotion
        """
        self._name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Applies the promotion to a product and returns the discounted price.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """

        pass


class PercentageDiscount(Promotion):
    """
    Represents a promotion that applies a percentage discount to the product price.
    """

    def __init__(self, name, percent):
        """
        Initializes a new PercentageDiscountPromotion instance.

        Args:
            name (str): The name of the promotion.
            discount_percentage (float): The percentage discount to apply (e.g., 20% off).
        """
        super().__init__(name)
        self.discount_percentage = percent

    def apply_promotion(self, product, quantity):
        """
        Applies the percentage discount promotion to the product and returns the discounted price.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the percentage discount promotion.
        """
        price = product.get_price()
        discount = price * self.discount_percentage / 100
        total_discount = discount * quantity
        return price * quantity - total_discount


class SecondItemHalfPricePromotion(Promotion):
    """
    Represents a promotion where the second item is sold at half price.
    """

    def __init__(self, name):
        """
        Initializes a new SecondItemHalfPricePromotion instance.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Applies the second item half price promotion to the product and returns the discounted price.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the second item half price promotion.
        """
        price = product.get_price()
        discounted_quantity = quantity // 2
        remaining_quantity = quantity % 2
        return (discounted_quantity * price / 2) + (remaining_quantity * price)


class Buy2Get1FreePromotion(Promotion):
    """
    Represents a promotion where buying 2 items gets 1 item for free.
    """

    def __init__(self, name):
        """
        Initializes a new Buy2Get1FreePromotion instance.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Applies the buy 2, get 1 free promotion to the product and returns the discounted price.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the buy 2 get 1 free promotion.
        """
        price = product.get_price()
        discounted_quantity = quantity // 3
        remaining_quantity = quantity % 3
        return (discounted_quantity * 2 * price) + (remaining_quantity * price)


