class Room:
    def __init__(self, name):
        self.name = name
        self.jukebox = []
        self.guest = []
        self.song = "Left Behind", "Slipknot"
        self.new_guest = "Rachel"

    def add_song_to_jukebox(self, song):
        self.jukebox.append(self.song)

    def add_guest_to_room(self, guest):
        self.guest.append(self.new_guest)

    def remove_guest_from_room(self, guest):
        self.guest.remove(self.new_guest)
  