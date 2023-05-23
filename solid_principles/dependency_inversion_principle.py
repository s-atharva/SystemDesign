# high level class must not depend on lower level class
# High-level module: Directly depends on a low-level module
from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailService(NotificationService):
    def send_notification(self, message):
        print("Sending email notification:", message)


class SMSNotificationService(NotificationService):
    def send_notification(self, message):
        print("Sending SMS notification:", message)


class NotificationManager:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_notification(self, message):
        self.notification_service.send_notification(message)


# Application entry point
if __name__ == "__main__":
    # Using the NotificationManager
    email_service = EmailService()
    sms_service = SMSNotificationService()

    email_manager = NotificationManager(email_service)
    email_manager.send_notification("Hello via email")

    sms_manager = NotificationManager(sms_service)
    sms_manager.send_notification("Hello via SMS")
