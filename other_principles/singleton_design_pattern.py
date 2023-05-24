class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, message):
        # logic to log the message
        print(f"Logging : {message}")


if __name__ == "__main__":
    logger_1 = Logger()
    logger_2 = Logger()

    logger_1.log("This is a log message.")
    logger_2.log("Another log message.")

    print(logger_1 is logger_2)
