"""
This module defines the Product class representing a product in the store,
and its derived classes for non-stocked and limited products.
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
        self._promotion = None

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
        Sets the quantity of the product. Deactivates product if quantity is less than 1.

        Args:
            quantity (int): The new quantity of the product.
        """
        if quantity >= 0:
            self._quantity = quantity
            if quantity < 1:
                self.deactivate()
            else:
                self.activate()

    def get_price(self):
        """
        Returns the price of the product.

        Returns:
            float: The price of the product.
        """
        return self._price

    def set_price(self, new_price):
        """
        Sets the price of the product.

        Args:
            new_price (float): The new price of the product.

        Returns:
            str: A message indicating the success or failure of setting the price.
        """
        if new_price > 0:
            self._price = new_price
            return "Price has been updated."
        else:
            return "The value set is invalid. Please use a positive value."

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

    def get_promotion(self):
        """
        Returns the promotion applied to the product.

        Returns:
            Promotions or None: The promotion applied to the product, or None if no promotion is applied.
        """
        return self._promotion

    def set_promotion(self, new_promotion):
        """
        Sets the promotion for the product.

        Args:
            new_promotion (Promotions): The new promotion to apply to the product.
        """
        self._promotion = new_promotion

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string representation of the product.
        """
        if self.get_promotion():
            promotion_name = self.get_promotion().get_name()
            promotion_info = f", Promotion: {promotion_name}"
            return f"{self.get_name()}, Price: £{self.get_price()}, Quantity: {self.get_quantity()}{promotion_info}"
        else:
            return f"{self.get_name()}, Price: £{self.get_price()}, Quantity: {self.get_quantity()}"

    def buy(self, quantity):
        """
        Buys a specified quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the product is inactive, there is insufficient quantity available, or the quantity is less than 1.
        """
        if not self.active:
            raise ValueError("Product is out of stock")
        elif self.get_quantity() < quantity:
            raise ValueError("Insufficient quantity available")
        elif quantity < 1:
            raise ValueError("Invalid quantity. Please provide a positive value.")

        if not self.get_promotion():
            remaining_quantity = self.get_quantity() - quantity
            self.set_quantity(remaining_quantity)
            return float(quantity * self.get_price())
        else:
            discounted_price = self.get_promotion().apply_promotion(self, quantity)
            remaining_quantity = self.get_quantity() - quantity
            self.set_quantity(remaining_quantity)
            return float(discounted_price)


class NonStockedProduct(Product):
    """
    A class representing a non-stocked product.

    Inherits from the Product class.
    """

    def __init__(self, name, price):
        """
        Initialize a non-stocked product with the given name and price.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.

        Note:
            The quantity for a non-stocked product is always set to 0.
        """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """
        Overrides the set_quantity method to prevent any changes to the quantity.

        Args:
            quantity: The quantity value (ignored).

        Note:
            This method does nothing for a non-stocked product.
        """
        pass

    def show(self):
        """
        Return a string representation of the non-stocked product.

        Returns:
            str: The formatted string representation of the non-stocked product.
                 Format: "<name>, Price: £<price>"
        """
        if self.get_promotion():
            promotion_name = self.get_promotion().get_name()
            promotion_info = f", Promotion: {promotion_name}"
            return f"{self.get_name()}, Price: £{self.get_price()}{promotion_info}"
        else:
            return f"{self.get_name()}, Price: £{self.get_price()}"

    def buy(self, quantity):
        """
        Buy a specified quantity of the non-stocked product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the quantity is less than 1.

        Note:
            Since the product is non-stocked, the purchase quantity is multiplied by the price to calculate the cost.
        """
        if quantity < 1:
            raise ValueError("Quantity must be a positive value")
        if not self.get_promotion() and quantity > self.get_quantity():
            remaining_quantity = self.get_quantity() - quantity
            self.set_quantity(remaining_quantity)
            return float(quantity * self.get_price())
        elif self.get_promotion() and quantity > self.get_quantity():
            discounted_price = self.get_promotion().apply_promotion(self, quantity)
            remaining_quantity = self.get_quantity() - quantity
            self.set_quantity(remaining_quantity)
            return float(discounted_price)


class LimitedProduct(Product):
    """
    A class representing a limited product with a maximum purchase limit.

    Inherits from the Product class.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        Initialize a limited product with the given name, price, quantity, and maximum purchase limit.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
            maximum (int): The maximum purchase limit.

        Raises:
            ValueError: If the maximum limit is less than 1 or greater than the quantity.
        """
        super().__init__(name, price, quantity)
        if maximum < 1 or maximum > quantity:
            raise ValueError("Invalid maximum limit")
        self._maximum = maximum

    def get_maximum(self):
        """
        Return the maximum purchase limit of the limited product.

        Returns:
            int: The maximum purchase limit.
        """
        return self._maximum

    def show(self):
        """
        Return a string representation of the limited product.

        Returns:
            str: The formatted string representation of the limited product.
                 Format: "<name>, Price: £<price>, Quantity: <quantity>, Maximum: <maximum>"
        """
        if self.get_promotion():
            promotion_name = self.get_promotion().get_name()
            promotion_info = f", Promotion: {promotion_name}"
            return f"{self.get_name()}, Price: £{self.get_price()}, Quantity: {self.get_quantity()}, Maximum: {self.get_maximum()}{promotion_info}"
        else:
            return f"{self.get_name()}, Price: £{self.get_price()}, Quantity: {self.get_quantity()}, Maximum: {self.get_maximum()}"

    def buy(self, quantity):
        """
        Buy a specified quantity of the limited product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the product is inactive, the quantity exceeds the maximum limit, or the quantity is less than 1.
        """
        if not self.active:
            raise ValueError("Product is out of stock")
        elif quantity > self.get_maximum():
            raise ValueError("Exceeds maximum purchase limit")
        elif quantity < 1:
            raise ValueError("Invalid quantity. Please provide a positive value.")

        if not self.get_promotion():
            remaining_quantity = self.get_quantity() - quantity
            self.set_quantity(remaining_quantity)
            return float(quantity * self.get_price())
        else:
            discounted_price = self.get_promotion().apply_promotion(self, quantity)
            remaining_quantity = self.get_quantity() - quantity
            self.set_quantity(remaining_quantity)
            return float(discounted_price)
