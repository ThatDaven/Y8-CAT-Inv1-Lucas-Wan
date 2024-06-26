# Y8-CAT-Inv1-Lucas-Wan


# Part 1.1: Create and explain a reusable means of achieving translations (10 Marks)
To achieve translations on the Cartesian plane according to the specified directions and distances, we can create a reusable function that utilizes a lookup table approach.

1. Lookup Table Creation: A lookup table that maps each direction (1 to 8) to the corresponding Pythagorean triple (a, b, c). This table will help us quickly determine the appropriate translation for each direction.
2. Translation Function: A function that takes the desired distance and direction as inputs. Using the lookup table, it will identify the corresponding Pythagorean triple and calculate the translation vector accordingly.
3. Error Handling: Error handling to ensure that the input direction is within the valid range (1 to 8) and that the distance is non-negative.
4. Documentation: We'll thoroughly document the function's purpose, inputs, outputs, and usage to ensure clarity and ease of understanding.


# Part 1.2:  Use functions, validate input and document imports (10 Marks)
Function Usage: Ensure that all operations, calculations, and functionalities are encapsulated within functions. This promotes modularity, readability, and reusability of code.
Input Validation: Validate input data to ensure it meets the specified criteria. For example, we'll reject negative lengths and directions beyond the range of 1 to 8.
Custom Implementation: Instead of relying on built-in libraries like math, have own versions of functions to perform required operations. For instance, if distance calculation is needed, we'll implement our own function instead of using math.dist().

    Example usage of input validation and distance calculation
        point1 = (2, -4)
        point2 = (-5, 3)
        if validate_distance(calculate_distance(point1, point2)):
        print("Distance:", calculate_distance(point1, point2))
        else:
        print("Invalid distance.")

    Example of validating direction
        direction = 10
        if validate_direction(direction):
         print("Valid direction.")
        else:
          print("Invalid direction.")


# Part 2.1 to 2.4: (25 marks)
2.1 Representing Entities with Dictionaries (5 Marks)
Create dictionaries for player_one, player_two, and destination, encapsulating relevant information about each entity, such as current coordinates, distance from the destination, midpoint coordinates to the other player, gradient with the destination, and personal space buffer.

2.2 Randomly Placing Entities (5 Marks)
Using the Python random module, generate random integer coordinates within the range of -800 to +800 for player_one, player_two, and destination, and store them in their respective dictionaries.

2.3 Calculating Distance, Midpoint, and Gradient (10 Marks)
Create functions to calculate the distance and gradient of each player to the destination, as well as the midpoint coordinates between the players. These functions will utilize custom implementations without relying on external modules.

2.4 Displaying Information (5 Marks)
Functions will be created to print information about each player and the destination, including their coordinates, distance to the destination, gradient with the destination, and midpoint coordinates with the other player. Aiming to reuse one function for printing player information to ensure modularity and consistency.


    Example of entities, functions and printing
        place_entities()
        update_player_info()
        print(f"Destination Location: ({destination['coordinates'][0]}, {destination['coordinates'][1]})")
        print_player_info(player_one)
        print_player_info(player_two)


# Part 3.1 to 3.2: (10 Marks)
First integrate the necessary functionality into the existing codebase. We'll focus on implementing functions to check for a winner based on reaching the destination's personal space buffer and to move players along the hypotenuse of a right-angled triangle.

check_winner() function checks if a player has reached the destination's personal space buffer.
move_player() function moves a player along the hypotenuse of a right-angled triangle by the specified distance and direction.
update_game_state() function updates the game state after each move, including checking for a winner.

An example usage demonstrates how to move a player and update the game state accordingly.

    Example of winning conditions
        # Example usage of moving a player
        move_distance = 15
        move_direction = 2
        actual_translation = move_player(player_one, move_distance, move_direction)
        print(f"Player One moved by {actual_translation}.")
        update_game_state()


# Part 4.1 to 4.3
4.1 You can use the time module to track the time taken by each player to make a move. If a player exceeds the time limit (e.g., 10 seconds), you can choose a random Pythagorean triple and direction for their move.

4.2 To design an NPC algorithm for player three, we need to create a strategy that allows the NPC to make intelligent decisions based on the game state. Here's a plausible algorithm for player three:
    Calculate Distance to Destination:
        Determine the current distance between player three and the destination.
    Evaluate Movement Options:
        Analyze the available movement options for player three:
    Check the distances along the hypotenuse of right-angled triangles to see which one brings the NPC closer to the destination.
        Consider potential obstacles or other players' positions that might influence the NPC's movement.
    hoose Optimal Move:
        Select the movement option that minimizes the distance between player three and the destination.
        If multiple options are equally good, prioritize moves that avoid collisions with obstacles or other players.
    Execute Move:
        Implement the chosen movement option by updating player three's position accordingly.
    Update Game State:
        After the NPC's move, update the game state to reflect the new positions of all players and any other relevant information.
    Repeat:
        Continue this process for each turn of the game, allowing the NPC to make decisions dynamically based on the evolving game state.

4.3 You can use Pygame to create a visual representation of the Cartesian plane and the movement of players. Each player's position can be represented by a different color or shape on the screen. After each turn, update the display to show the new positions of the players.
    
Implementing the game state:
How I created the game using this selected code
1. Defined the game's entities, directions, and the game's state
(player_one, player_two, destination, game_state)
2. Created functions to manipulate the game's state
(place_entities, update_player_info, move_player, move_player_with_time_limit, update_game_state, check_winner, print_player_info)
3. Created a game loop that alternates turns between the human players and the NPC
(while True)
4. Added input validation to prevent invalid directions and distances
(if direction: and if distance:)
5. Displayed the game state after each turn
(print("\nUpdated Game State after [Player/NPC]'s Turn:"))
6. Checked for a winner after each turn and ended the game if a winner is detected
(if check_winner([player]): break)
7. Finally, added some text-based user interface to make the game more interactive
(input() and print() statements)