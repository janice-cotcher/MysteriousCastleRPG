class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

class Game:
    def __init__(self):
        self.rooms = {
            "outside": Room("outside", "You are standing outside of a mysterious castle. The door is locked.", {"south": "garden", "west": "path"}),
            "garden": Room("garden", "You are in a beautiful garden. There is a key on the ground.", {"north": "outside"}),
            "path": Room("path", "You are on a path leading to the castle. There is a signpost.", {"east": "outside"})
        }
        self.current_room = self.rooms["outside"]

    def play(self):
        while True:
            print(self.current_room.description)
            print("Exits: ", end="")
            for direction in self.current_room.exits:
                print(direction, end=" ")
            print()

            move = input("Where would you like to go? ").lower()

            if move in self.current_room.exits:
                self.current_room = self.rooms[self.current_room.exits[move]]
            else:
                print("You can't go that way.")

game = Game()
game.play()
