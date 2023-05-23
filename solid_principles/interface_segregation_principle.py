class Sendable:
    def send(self):
        pass


class Receivable:
    def receive(self):
        pass


class Email(Sendable, Receivable):
    def send(self):
        print("Sending email")

    def receive(self):
        print("Receiving email")


class SMS(Sendable, Receivable):
    def send(self):
        print("Sending SMS")

    def receive(self):
        print("Receiving SMS")


class PushNotification(Sendable):
    def send(self):
        print("Sending push notification")


if __name__ == "__main__":
    email = Email()
    email.send()
    email.receive()

    sms = SMS()
    sms.send()
    sms.receive()

    push = PushNotification()
    push.send()
