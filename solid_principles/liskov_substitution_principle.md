The Liskov Substitution Principle means that any object of a parent class should be able to be replaced with an object
of its child class without breaking the program.

* used to inherited properly

violates = breaks

This violates the Liskov Substitution Principle because a Square object is not a proper substitute
for a Rectangle object. The principle states that objects of a derived class should be substitutable
for objects of the base class without affecting the correctness of the program.
But in this case, when we treat a Square as a Rectangle, it leads to unexpected behavior.

    square = Square(5, 5) # answer = 25
    square = Square(5, 6) # unexpected answer = 30

To solve the problem and adhere to the Liskov Substitution Principle, we need to restructure
the Square and Rectangle classes. Approach is to remove the inheritance relationship between
them and instead introduce a common interface or base class that represents a shape.

By redesigning the classes and adhering to the Liskov Substitution Principle, we create a clear separation
between shapes, provide a common interface, and ensure that objects of derived classes can be used
interchangeably with objects of the base class without introducing unexpected behavior.

    square = Square(5) # answer = 25
