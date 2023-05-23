high-level modules should not depend on low-level modules. Instead, both should depend on abstractions. It promotes
loose coupling between modules and emphasizes the use of interfaces or abstract classes to define those abstractions.

In simpler terms, the DIP suggests that the implementation details of low-level modules should not be directly relied
upon by high-level modules. Instead, both modules should depend on common abstractions or interfaces, allowing for
flexibility, extensibility, and easier maintenance of the system.

By depending on the NotificationService abstraction, the NotificationManager is decoupled from the concrete
implementations (EmailService and SMSNotificationService). This allows for easy swapping of notification services and
promotes the Dependency Inversion Principle. The high-level NotificationManager module doesn't depend on low-level
modules directly, but on abstractions, resulting in a more flexible and maintainable system.