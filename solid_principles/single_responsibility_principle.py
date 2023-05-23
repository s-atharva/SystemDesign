class Backpack:
    def __init__(self):
        self.bag = []

    def add_item(self, item):
        self.bag.append(item)

    def get_items(self):
        return self.bag


class MusicPlayer:
    def play_music(self, song):
        print(f"Playing {song}")


class Phone:
    def make_call(self, number):
        print(f"Calling {number}")


if __name__ == "__main__":
    # Creating objects
    my_backpack = Backpack()
    my_music_player = MusicPlayer()
    my_phone = Phone()

    # Using the objects
    my_backpack.add_item("Books")
    print(my_backpack.get_items())

    my_music_player.play_music("Coldplay")  # Playing music
    my_phone.make_call("9309276204")  # Making a phone call
