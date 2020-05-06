from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player = Player(input('Enter Name: '), room['outside'])

err = '\033[91m' + 'You cannot travel in that direction' + '\033[0m'

color = '\033[94m'

print('Enter Q to quit at any time' + '\033[0m')

for i in range(100):
    print(color + '\033[1m' + color + "\033[4m" + player.currentRoom.name)
    print('\033[0m' + player.currentRoom.description)
    dir = input('Enter N, S, E or W to pick a direction: ').upper()
    if dir == "N":
        if hasattr(player.currentRoom, "n_to"):
            player.currentRoom = player.currentRoom.n_to
            color = "\033[92m"
        elif not hasattr(player.currentRoom, "n_to"):
            print(err)
    elif dir == "S":
        if hasattr(player.currentRoom, "s_to"):
            player.currentRoom = player.currentRoom.s_to
            color = "\033[94m"
        elif not hasattr(player.currentRoom, "s_to"):
            print(err)
    elif dir == "E":
        if hasattr(player.currentRoom, "e_to"):
            player.currentRoom = player.currentRoom.e_to
            color = "\033[95m"
        elif not hasattr(player.currentRoom, "e_to"):
            print(err)
    elif dir == "W":
        if hasattr(player.currentRoom, "w_to"):
            player.currentRoom = player.currentRoom.w_to
            color = "\033[96m"
        elif not hasattr(player.currentRoom, "w_to"):
            print(err)
    elif dir == "Q":
        exit()
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
