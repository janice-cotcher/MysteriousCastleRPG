# Text-based Adventure Game in Python

# Define the different rooms in the game
rooms = {
    "outside": {
        "description": "You are standing outside of a mysterious castle. The door is locked.",
        "exits": {"south": "garden", "west": "path"}
    },
    "garden": {
        "description": "You are in a beautiful garden. There is a key on the ground.",
        "exits": {"north": "outside"}
    },
    "path": {
        "description": "You are on a path leading to the castle. There is a signpost.",
        "exits": {"east": "outside"}
    }
}

# Initialize the player's current location
current_room = "outside"

# Game loop
while True:
    # Print the description of the current room
    print(rooms[current_room]["description"])
    # Print the exits available from the current room
    exits = rooms[current_room]["exits"]
    print("Exits: ", end="")
    for direction in exits:
        print(direction, end=" ")
    print()

    # Get the player's next move
    move = input("Where would you like to go? ").lower()

    # Check if the move is valid
    if move in exits:
        current_room = exits[move]
    else:
        print("You can't go that way.")
