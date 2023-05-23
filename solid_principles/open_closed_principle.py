from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


if __name__ == "__main__":
    # Creating objects
    rectangle = Rectangle(5, 5)
    circle = Circle(4)
    shapes = [rectangle, circle]

    # Calculating area
    print(f"The total area is: {rectangle.area()}")
    print(f"The total area is: {circle.area()}")
