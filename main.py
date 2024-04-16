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
    for entity in [player_one, player_two, destination]:
        entity['coordinates'] = [random.randint(-800, 800), random.randint(-800, 800)]

# 2.3 Calculating Distance, Midpoint, and Gradient
# Implement functions to calculate distance, midpoint, and gradient

# 2.4 Displaying Information
def print_player_info(player):
    print(f"Player Location: ({player['coordinates'][0]}, {player['coordinates'][1]})")
    print(f"Distance to Destination: {player['distance_to_destination']} units")
    print(f"Gradient with Destination: {player['gradient_with_destination']}")
    # Check if the 'midpoint_with_player_one' or 'midpoint_with_player_two' key exists
    if 'midpoint_with_player_one' in player:
        print(f"Midpoint with Other Player: ({player['midpoint_with_player_one'][0]}, {player['midpoint_with_player_one'][1]})")
    elif 'midpoint_with_player_two' in player:
        print(f"Midpoint with Other Player: ({player['midpoint_with_player_two'][0]}, {player['midpoint_with_player_two'][1]})")

# Example usage
place_entities()
print_player_info(player_one)
print_player_info(player_two)
print(f"Destination Location: ({destination['coordinates'][0]}, {destination['coordinates'][1]})")

