# MysteriousCastleRPG
Example of a Python text-based adventure game created by ChatGBT

From ChatGPT about main.py:
>>This code defines a dictionary called "rooms" that contains the different rooms in the game, and their descriptions and exits. The player starts in the "outside" room, and the game loop allows them to move between rooms by entering a direction (north, south, east, or west in this example) when         prompted. If the player enters an invalid direction, the game will print "You can't go that way."
>>
>>This is a simple example, you could add different levels, puzzles and items that the player can pick up and interact with to make it more interesting.

From ChatGPT about OOPex.py
>>This code defines two classes, Room and Game. The Room class has a constructor method (__init__) that takes in the name, description, and exits of a room. The Game class has a constructor method that creates a dictionary of rooms and sets the current room to "outside". The play method runs a game loop that allows the player to move between rooms by entering a direction when prompted. If the player enters an invalid direction, the game will print "You can't go that way."
>>
>>This example is similar to the previous example, but instead of using a dictionary for the rooms, it uses instances of the Room class. This allows for more flexibility and organization in the code, and makes it easier to add additional properties and methods to the Room class. You could also add additional classes like Player, Inventory, Items, etc, that interact with the Room class and the game logic.
