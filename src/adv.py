from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["SAND", "STICK"], 'outside'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [], 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["SKULL", "ROCK"], 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["COIN", "MUG"], 'treasure'),
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

player = Player(input('Enter Name: '), room['outside'], [])

color = '\033[94m'

bold = '\033[1m'

underlined = '\033[4m'

red = '\033[31m'

magenta = '\033[95m'

reset = '\033[0m'

done = False

err = red + 'You cannot travel in that direction' + reset

print(bold + magenta + 'Enter Q to quit at any time')
print('Enter N, S, E or W to pick a direction')
print('Enter I or INVENTORY to view inventory')
print('To pick things up, enter TAKE ITEM. To drop, DROP ITEM' + reset)

while not done:
    print(bold + underlined + color + player.currentRoom.name)
    print(reset + bold + color + player.currentRoom.description)
    if len(player.currentRoom.items) > 0:
        print(f"You see the following items: {player.currentRoom.items}")
    elif len(player.currentRoom.items) < 0:
        print("There are no items in this room.")
    dir = input('$ ').upper()
    cmd = dir.split()
    if len(cmd) < 2:
        if dir == "I":
            print(reset + f"Inventory: {player.items}")
        elif dir == "N":
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
            done = True
    else:
        if cmd[0] == "DROP":
            if cmd[1] in player.items:
                player.removeItem(cmd[1])
                room[player.currentRoom.shortname].addItem(cmd[1])
                print(reset + f"You have dropped {cmd[1]}")
            else:
                print(red + f"{cmd[1]} is not in your inventory")
        elif cmd[0] == "GET" or "TAKE":
            if cmd[1] in player.currentRoom.items:
                player.addItem(cmd[1])
                room[player.currentRoom.shortname].removeItem(cmd[1])
                print(reset + f"You have picked up {cmd[1]}")
            else:
                print(red + f"{cmd[1]} is not in this room")

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
