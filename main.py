#Part 1.1: Reusable mean of translation.
# Lookup table containing the first 127 primitive Pythagorean triples
pythagorean_triples = [
    [3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25], [20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53], [11, 60, 61], [33, 56, 65], [16, 63, 65], [48, 55, 73], [13, 84, 85], [36, 77, 85], [39, 80, 89], [65, 72, 97], [20, 99, 101], [60, 91, 109], [15, 112, 113], [44, 117, 125], [88, 105, 137], [17, 144, 145], [24, 143, 145], [51, 140, 149], [85, 132, 157], [119, 120, 169], [52, 165, 173], [19, 180, 181], [57, 176, 185], [104, 153, 185], [95, 168, 193], [28, 195, 197], [133, 156, 205], [84, 187, 205], [21, 220, 221], [140, 171, 221], [60, 221, 229], [105, 208, 233], [120, 209, 241], [32, 255, 257], [23, 264, 265], [96, 247, 265], [69, 260, 269], [115, 252, 277], [160, 231, 281], [161, 240, 289], [68, 285, 293], [207, 224, 305], [136, 273, 305], [25, 312, 313], [75, 308, 317], [204, 253, 325], [36, 323, 325], [175, 288, 337], [180, 299, 349], [225, 272, 353], [27, 364, 365], [76, 357, 365], [252, 275, 373], [135, 352, 377], [152, 345, 377], [189, 340, 389], [228, 325, 397], [40, 399, 401], [120, 391, 409], [29, 420, 421], [87, 416, 425], [297, 304, 425], [145, 408, 433], [203, 396, 445], [84, 437, 445], [280, 351, 449], [168, 425, 457], [261, 380, 461], [31, 480, 481], [319, 360, 481], [93, 476, 485], [44, 483, 485], [155, 468, 493], [132, 475, 493], [217, 456, 505], [336, 377, 505], [220, 459, 509], [279, 440, 521], [308, 435, 533], [92, 525, 533], [341, 420, 541], [33, 544, 545], [184, 513, 545], [165, 532, 557], [396, 403, 565], [276, 493, 565], [231, 520, 569], [48, 575, 577], [368, 465, 593], [240, 551, 601], [35, 612, 613], [105, 608, 617], [336, 527, 625], [429, 460, 629], [100, 621, 629], [200, 609, 641], [315, 572, 653], [300, 589, 661], [385, 552, 673], [52, 675, 677], [37, 684, 685], [156, 667, 685], [111, 680, 689], [400, 561, 689], [185, 672, 697], [455, 528, 697], [260, 651, 701], [259, 660, 709], [333, 644, 725], [364, 627, 725], [108, 725, 733], [407, 624, 745], [216, 713, 745], [468, 595, 757], [39, 760, 761], [481, 600, 769], [195, 748, 773], [273, 736, 785], [56, 783, 785], [432, 665, 793], [168, 775, 793], [555, 572, 797], ]

def translate_player(distance, direction):
    """
    Translate a player a specified distance in a particular direction on the Cartesian plane.

    Args:
    - distance (int): The distance to move.
    - direction (int): The direction of movement (1 to 8).

    Returns:
    - translation (tuple): A tuple representing the translation vector (dx, dy).
    """

    # Validate direction input
    if direction < 1 or direction > 8:
        raise ValueError("Direction must be an integer between 1 and 8.")

    # Retrieve the corresponding Pythagorean triple from the lookup table
    pythagorean_triple = pythagorean_triples[direction - 1]

    # Calculate the translation vector based on the Pythagorean triple
    a, b, c = pythagorean_triple
    if direction in [1, 2, 8]:
        dx = a
    else:
        dx = -a
    if direction in [1, 4, 5]:
        dy = b
    else:
        dy = -b

    # Adjust distance if necessary to match available hypotenuse lengths
    actual_distance = min(distance, c)
    return (dx * actual_distance, dy * actual_distance)
#With this function, we can easily translate players on the Cartesian plane according to the specified directions and distances.

##########################################################################################################################################################################

#Part 1.2: Utilising functions in order to complete operations.
def validate_distance(distance):
    """
    Validate the input distance.

    Args:
    - distance (int): The distance to validate.
    
    Returns:
    - bool: True if the distance is valid, False otherwise.
    """
    return distance >= 0  # Reject negative distances
def validate_direction(direction):
    """
    Validate the input direction.
    
    Args:
    - direction (int): The direction to validate.
    
    Returns:
    - bool: True if the direction is valid, False otherwise.
    """
    return direction >= 1 and direction <= 8  # Accept directions within the range of 1 to 8
def calculate_distance(point1, point2):
    """
    Calculate the distance between two points on the Cartesian plane.
    
    Args:
    - point1 (tuple): The coordinates of the first point (x1, y1).
    - point2 (tuple): The coordinates of the second point (x2, y2).
    
    Returns:
    - float: The distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Euclidean distance formula

##########################################################################################################################################################################

#Part 2.1 to 2.4: 
import random
import math

# 2.1 Representing Entities with Dictionaries
player_one = {
    'coordinates': [0, 0],
    'distance_to_destination': None,
    'midpoint_with_player_two': None,  # Change this key
    'gradient_with_destination': None,
    'personal_space_buffer': 10
}

player_two = {
    'coordinates': [0, 0],
    'distance_to_destination': None,
    'midpoint_with_player_one': None,  # Change this key
    'gradient_with_destination': None,
    'personal_space_buffer': 10
}

destination = {
    'coordinates': [0, 0],
    'personal_space_buffer': 10
}

# 2.2 Randomly Placing Entities
def place_entities():
    for entity in [player_one, player_two, player_three,destination]:
        entity['coordinates'] = [random.randint(-800, 800), random.randint(-800, 800)]

# 2.3 Calculating Distance, Midpoint, and Gradient
# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return round(math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2),1)

# Function to calculate midpoint between two points
def calculate_midpoint(point1, point2):
    midpoint_x = (point1[0] + point2[0]) / 2
    midpoint_y = (point1[1] + point2[1]) / 2
    return [round(midpoint_x,1), round(midpoint_y,1)]

# Function to calculate gradient between two points
def calculate_gradient(point1, point2):
    if point2[0] - point1[0] == 0:
        return round(float('inf'),1)
    else:
        return round((point2[1] - point1[1]) / (point2[0] - point1[0]),1)

# Update player dictionaries with calculated values
def update_player_info():
    player_one['distance_to_destination'] = round(calculate_distance(player_one['coordinates'], destination['coordinates']),1)
    player_two['distance_to_destination'] = round(calculate_distance(player_two['coordinates'], destination['coordinates']),1)
    player_one['midpoint_with_player_two'] = calculate_midpoint(player_one['coordinates'], player_two['coordinates'])
    player_two['midpoint_with_player_one'] = calculate_midpoint(player_one['coordinates'], player_two['coordinates'])
    player_one['gradient_with_destination'] = calculate_gradient(player_one['coordinates'], destination['coordinates'])
    player_two['gradient_with_destination'] = calculate_gradient(player_two['coordinates'], destination['coordinates'])
    player_three['gradient_with_destination'] = calculate_gradient(player_one['coordinates'], destination['coordinates'])
    player_three['distance_to_destination'] = round(calculate_distance(player_two['coordinates'], destination['coordinates']),1)

# 2.4 Displaying Information
def print_player_info(player):
    print(f"Player Location: ({player['coordinates'][0]}, {player['coordinates'][1]})")
    print(f"Distance to Destination: {player['distance_to_destination']} units")
    print(f"Gradient with Destination: {player['gradient_with_destination']}")
    # Check if the 'midpoint_with_player_one' or 'midpoint_with_player_two' key exists
    if 'midpoint_with_player_one' in player:
        midpoint = player['midpoint_with_player_one']
        if midpoint is not None:
            print(f"Midpoint with Other Player: ({midpoint[0]}, {midpoint[1]})")
        else:
            print("No midpoint with other player")
    elif 'midpoint_with_player_two' in player:
        midpoint = player['midpoint_with_player_two']
        if midpoint is not None:
            print(f"Midpoint with Other Player: ({midpoint[0]}, {midpoint[1]})")
        else:
            print("No midpoint with other player")

# Part 3.1: Use the personal space buffer to identify a winner
def check_winner(player):
    """
    Check if a player has reached the destination's personal space buffer.

    Args:
    - player (dict): The player dictionary containing coordinates and personal space buffer.

    Returns:
    - bool: True if the player has reached the destination's personal space buffer, False otherwise.
    """
    distance_to_destination = calculate_distance(player['coordinates'], destination['coordinates'])
    if distance_to_destination <= player['personal_space_buffer']:
        print("Player has reached the destination's personal space buffer.")
        return True
    else:
        print("Player has not reached the destination's personal space buffer.")
        return False

# Part 3.2: Move players along the hypotenuse of a right-angled triangle
def move_player(player, distance, direction):
    """
    Move a player along the hypotenuse of a right-angled triangle by the specified distance and direction.
    Args:
    - player (dict): The player dictionary to be moved.
    - distance (int): The requested distance to move.
    - direction (int): The direction of movement (1 to 8).
    Returns:
    - tuple: A tuple representing the actual translation vector (dx, dy) applied to the player.
    """
    # Retrieve the corresponding Pythagorean triple from the lookup table
    pythagorean_triple = pythagorean_triples[direction - 1]

    # Calculate the maximum available distance along the hypotenuse
    max_available_distance = pythagorean_triple[2]

    # Adjust the requested distance if necessary to match the available hypotenuse length
    actual_distance = min(distance, max_available_distance)

    # Translate the player based on the Pythagorean triple
    translation = translate_player(actual_distance, direction)

    # Update player coordinates
    player['coordinates'][0] += translation[0]
    player['coordinates'][1] += translation[1]

    # Print message about player movement
    print(f"Player has moved by {translation} units.")

    return translation

# Update player information after each move
def update_game_state():
    update_player_info()  # Update player distances, midpoints, and gradients
    if check_winner(player_one):
        print("Player One has reached the destination and won!")
    elif check_winner(player_two):
        print("Player Two has reached the destination and won!")
    else:
        print("No winner yet. Keep playing!")

import time
import random

#Part 4.1 to 4.2
#Introducing a time penalty with time and random library functions
def move_player_with_time_limit(player, distance, direction, time_limit=10): #Sets time limit at 10 seconds.
    start_time = time.time()
    translation = move_player(player, distance, direction)
    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time > time_limit: #Checking if time limit is out
        print("Player exceeded time limit. Choosing random move.") #Gives random moves to not disadvantage the player. Losing a turn is too harsh and too hard to code.
        random_direction = random.randint(1, 8)
        random_distance = random.randint(1, pythagorean_triples[random_direction - 1][2])
        translation = move_player(player, random_distance, random_direction) #This is the only function of the random library to give a random move. 
        #(besides generating random placements in earlier part 2.2)

    return translation

import random
import math

# Define the NPC (player three) dictionary
player_three = {
    'coordinates': [0, 0],
    'distance_to_destination': None,
    'personal_space_buffer': 10
}

def calculate_distance(point1, point2):
    """
    Calculate the distance between two points on the Cartesian plane.
    
    Args:
    - point1 (tuple): The coordinates of the first point (x1, y1).
    - point2 (tuple): The coordinates of the second point (x2, y2).
    
    Returns:
    - float: The distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Euclidean distance formula

def move_npc():
    """
    Move the NPC (player three) based on the calculated optimal move.
    """
    # Calculate distance to destination
    player_three['distance_to_destination'] = calculate_distance(player_three['coordinates'], destination['coordinates'])
    
    # Evaluate movement options (hypotenuses of right-angled triangles)
    optimal_move = None
    min_distance = float('inf')
    
    for direction in range(1, 9):
        pythagorean_triple = pythagorean_triples[direction - 1]
        max_available_distance = pythagorean_triple[2]
        actual_distance = min(max_available_distance, player_three['distance_to_destination'])
        if actual_distance < min_distance:
            min_distance = actual_distance
            optimal_move = direction
    
    # Execute optimal move
    actual_translation = move_player(player_three, min_distance, optimal_move)
    print(f"NPC (Player Three) moved by {actual_translation}.")

#Game
# Define the directions
directions = {
    'Up': 1,
    'Down': 2,
    'Left': 3,
    'Right': 4,
    'Diagonal Up Right': 5,
    'Diagonal Up Left': 6,
    'Diagonal Down Right': 7,
    'Diagonal Down Left': 8
}

# Initialize the game
place_entities()  # Randomly place players and destination
update_player_info()  # Update initial player information

# Inform players about the game setup
print("Welcome Lucas Wan's Cartesian Game")
print("The game setup is as follows:")
print(f"- Destination Location: {destination['coordinates']}")
print(f"- Player One Starting Position: {player_one['coordinates']}")
print(f"- Player Two Starting Position: {player_two['coordinates']}")
print(f"- NPC (Player Three) Starting Position: {player_three['coordinates']}")
print("Let's begin!\n")

# Display initial game state
print("Initial Game State:")
print("Player One's Information:")
print_player_info(player_one)
print("\nPlayer Two's Information:")
print_player_info(player_two)
print("\nNPC's Information:")
print_player_info(player_three)
print("\nDestination Location:", destination['coordinates'])

# Game Loop
while True:
    # Human Player One's Turn
    print("\nPlayer One's Turn:")
    direction_name = input("Enter direction (Up, Down, Left, Right, Diagonal Up Right, Diagonal Up Left, Diagonal Down Right, Diagonal Down Left): ")
    direction = directions.get(direction_name)
    if direction:
        distance = int(input("Enter distance: "))
        move_player_with_time_limit(player_one, distance, direction)
        update_game_state()  # Update game state
        print("\nUpdated Game State after Player One's Turn:")
        print("Player One's Information:")
        print_player_info(player_one)
        print("\nPlayer Two's Information:")
        print_player_info(player_two)
        print("\nNPC's Information:")
        print_player_info(player_three)
        print("\nDestination Location:", destination['coordinates'])
        if check_winner(player_one):
            break
    else:
        print("Invalid direction. Please enter a valid direction.")

     # Human Player Two's Turn
    print("\nPlayer Two's Turn:")
    direction_name = input("Enter direction (Up, Down, Left, Right, Diagonal Up Right, Diagonal Up Left, Diagonal Down Right, Diagonal Down Left): ")
    direction = directions.get(direction_name)
    if direction:
        distance = int(input("Enter distance: "))
        move_player_with_time_limit(player_two, distance, direction)
        update_game_state()  # Update game state
        print("\nUpdated Game State after Player Two's Turn:")
        print("Player One's Information:")
        print_player_info(player_one)
        print("\nPlayer Two's Information:")
        print_player_info(player_two)
        print("\nNPC's Information:")
        print_player_info(player_three)
        print("\nDestination Location:", destination['coordinates'])
        if check_winner(player_two):
            break
    else:
        print("Invalid direction. Please enter a valid direction.")

    # NPC (Player Three) Turn
    print("\nNPC's Turn:")
    move_npc()
    update_game_state()  # Update game state
    print("\nUpdated Game State after NPC's Turn:")
    print("Player One's Information:")
    print_player_info(player_one)
    print("\nPlayer Two's Information:")
    print_player_info(player_two)
    print("\nNPC's Information:")
    print_player_info(player_three)
    print("\nDestination Location:", destination['coordinates'])
    if check_winner(player_three):
        break


