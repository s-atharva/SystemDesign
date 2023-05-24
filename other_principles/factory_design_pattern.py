# The Factory design pattern provides a way to create objects without specifying their concrete classes directly.
# By using factory class or function it provides central place to manage another classes
from abc import ABC, abstractmethod


# Define the interface/abstract class
class Product(ABC):
    @abstractmethod
    def operate(self):
        pass


class ProductA(Product):
    def operate(self):
        return "Product A operation"


class ProductB(Product):
    def operate(self):
        return "Product B operation"


# factory_class
class ProductFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "A":
            return ProductA()
        elif product_type == "B":
            return ProductB()
        else:
            print("Invalid input")
            raise Exception("Invalid class")


if __name__ == "__main__":
    # without factory class
    # product_a = ProductA()
    # product_b = ProductB()
    # print(product_a.operate())
    # print(product_b.operate())
    # using factory class
    product = input("Enter the product name: ")
    print(f"Product = {product}")
    product_a = ProductFactory.create_product(product)
    print(product_a.operate())
