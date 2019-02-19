
import random

start_position = (0, 0)

treasure_location = (random.randint(-5, 5), random.randint(-5, 5))
searched_locations = []
treasure_found = False


def go(position, direction):
    """
    Move in the specified direction.
    """
    direction = direction.lower()
    print(f'Going {direction}') 
    if direction == 'north':
        new_position = (position[0], position[1] + 1)
    elif direction == 'south':
        new_position = (position[0], position[1] - 1)
    elif direction == 'east':
        new_position = (position[0] + 1, position[1])
    elif direction == 'west':
        new_position = (position[0] - 1, position[1])
    else:
        print('No such direction')
        return position
    return new_position

def where_am_i(position):
    """
    Print my position
    """
    print('I am at:', position)
    return position

def load(position, file):
    """
    Read a set of instructions from a file.
    """
    with open(file, 'rt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        command, *args = line.split()
        position = process_command(position, command, args, from_load=True)
    return position

def dig(position):
    """
    Check to see if the treasure is here.
    """
    if position in searched_locations:
        print("I've already dug here")
    elif position == treasure_location:
        print('Yay, I found the treasure')
        treasure_found = True
    else:
        print("I didn't find anything")
        searched_locations.append(position)


def get_clue(position):
    """
    Get a clue for the location of the treasure.
    """
    direction = random.choice(['NS', 'EW'])
    if direction == 'NS':
        my_y = position[1]
        treasure_y = treasure_location[1]
        if my_y > treasure_y:
            print('The treasure is South of your position')
        elif my_y < treasure_y:
            print('The treasure is North of your position')
        else:
            print('The treasure is neither North nor South of your position')
    elif direction == 'EW':
        my_x = position[0]
        treasure_x = treasure_location[0]
        if my_x > treasure_x:
            print('The treasure is West of your position')
        elif my_x < treasure_x:
            print('The treasure is East of your position')
        else:
            print('The treasure is neither East nor West of your position')





def process_command(position, cmd, args, from_load=False):
    """
    Run the correct command based on input.
    """
    if cmd == 'go':
        for direction in args:
            position = go(position, direction)
    elif cmd == 'load':
        if from_load:
            print('Cannot load from a loaded file')
            return position
        for file_name in args:
            position = load(position, file_name)
    elif cmd == 'dig':
        dig(position)
    elif cmd == 'clue':
        get_clue(position)
    else:
        print("I don't recognise this command")
    return position



def loop():
    """
    Main loop, run the game.
    """
    print('Hello')
    position = start_position
    while not treasure_found:
        line = input('>>')
        if not line or line == 'end':
            break

        if line == 'where am I?':
            position = where_am_i(position)
            continue
        if line == 'Hello':
            print('Hello!')
            continue
        if line == 'This parrot is dead':
            print("He's just sleeping")
            continue
        command, *args = line.strip().split()

        position = process_command(position, command, args)


    print('Goodbye')




if __name__ == '__main__':
    loop()
