from abc import ABC, abstractmethod


# Let's consider a classic example that demonstrates the violation of the Liskov Substitution Principle
#                   when using a Square and Rectangle class hierarchy.

# class Rectangle:
#     def __init__(self, width: int, height: int):
#         self.width = width
#         self.height = height
#
#     def set_width(self, width: int):
#         self.width = width
#
#     def set_height(self, height: int):
#         self.height = height
#
#     def calculate_area(self) -> int:
#         return self.width * self.height
#
#
# class Square(Rectangle):
#     def set_width(self, width: int):
#         self.width = width
#         self.height = width
#
#     def set_height(self, height: int):
#         self.height = height
#         self.width = height
#
#
# def print_area(rectangle: Rectangle):
#     area = rectangle.calculate_area()
#     print(f"The area of the rectangle is: {area}")

# By redesigning the classes and adhering to the Liskov Substitution Principle,
#                   we create a clear separation between shapes.
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def calculate_area(self) -> int:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side_length: int):
        self.side_length = side_length

    def set_side_length(self, side_length: int):
        self.side_length = side_length

    def calculate_area(self) -> int:
        return self.side_length ** 2


def print_area(shape: Shape):
    area = shape.calculate_area()
    print(f"The area of the shape is: {area}")


if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    print_area(rectangle)

    square = Square(5)
    print_area(square)
