import pygame
import random
import math
import sys
from main import *

# Hypotenuse movement function
def hypotenuse_move(current_position, target_position, speed):
    dx = target_position[0] - current_position[0]
    dy = target_position[1] - current_position[1]
    distance = math.hypot(dx, dy)
    if distance == 0:
        return current_position
    move_x = dx / distance * speed
    move_y = dy / distance * speed
    new_position = (current_position[0] + move_x, current_position[1] + move_y)
    return new_position

# Initialise Pygame
pygame.init()
app_clock = pygame.time.Clock()

# Function to create the Pygame window
def create_app_window(width, height):
    print(f'\nWelcome. The plane goes from -{width/2} to {width/2} in both the x and y directions')
    pygame.display.set_caption("Cartesian Game")
    app_dimensions = (width + 10, height + 10)
    app_surf = pygame.display.set_mode(app_dimensions)
    app_surf_rect = app_surf.get_rect()
    return app_surf, app_surf_rect

# Function to update the Pygame window
def app_surf_update(destination, player_one, player_two, timer_text, current_turn):
    app_surf.fill('white')
    pygame.draw.line(app_surf, 'grey', (0, app_surf_rect.height/2), (app_surf_rect.width, app_surf_rect.height/2), width=1)
    pygame.draw.line(app_surf, 'grey', (app_surf_rect.width/2, 0), (app_surf_rect.width/2, app_surf_rect.height), width=1)
    pygame.draw.circle(app_surf, 'black', destination['pygame_coords'], radius=3, width=3)
    pygame.draw.circle(app_surf, player_one['colour'], player_one['pygame_coords'], radius=3, width=2)
    pygame.draw.circle(app_surf, player_two['colour'], player_two['pygame_coords'], radius=3, width=2)
    display_coordinates(player_one['pygame_coords'], player_two['pygame_coords'], destination['pygame_coords'], timer_text, current_turn)

# Function to refresh the Pygame window
def refresh_window():
    pygame.display.update()
    app_clock.tick(24)

# Function to convert Cartesian coordinates to Pygame coordinates
def conv_cartesian_to_pygame_coords(x, y):
    pygame_x = x + app_surf_rect.width / 2
    pygame_y = -y + app_surf_rect.height / 2
    return (pygame_x, pygame_y)
    p1_rand_x, p1_rand_y = random.randint(-400, 400), random.randint(-400, 400)
    player_one['cartesian_coords'] = (p1_rand_x, p1_rand_y)
    player_one['pygame_coords'] = conv_cartesian_to_pygame_coords(p1_rand_x, p1_rand_y)

    p2_rand_x, p2_rand_y = random.randint(-400, 400), random.randint(-400, 400)
    player_two['cartesian_coords'] = (p2_rand_x, p2_rand_y)
    player_two['pygame_coords'] = conv_cartesian_to_pygame_coords(p2_rand_x, p2_rand_y)

    dest_rand_x, dest_rand_y = random.randint(-400, 400), random.randint(-400, 400)
    destination['cartesian_coords'] = (dest_rand_x, dest_rand_y)
    destination['pygame_coords'] = conv_cartesian_to_pygame_coords(dest_rand_x, dest_rand_y)

# Function to display coordinates on the Pygame window
def display_coordinates(player_one_coords, player_two_coords, destination_coords, timer_text, current_turn):
    font = pygame.font.Font(None, 24)
    player_one_text = font.render(f'Player One: {player_one_coords}', True, pygame.Color('black'))
    player_two_text = font.render(f'Player Two: {player_two_coords}', True, pygame.Color('black'))
    destination_text = font.render(f'Destination: {destination_coords}', True, pygame.Color('black'))
    timer = font.render(f'Time left: {timer_text}', True, pygame.Color('black'))
    turn_text = font.render(f"Turn: Player {current_turn}", True, pygame.Color('black'))
    app_surf.blit(player_one_text, (20, 20))
    app_surf.blit(player_two_text, (20, 50))
    app_surf.blit(destination_text, (20, 80))
    app_surf.blit(timer, (20, 110))
    app_surf.blit(turn_text, (20, 140))

# Function to switch turns between players
def switch_turn(current_turn):
    return 1 if current_turn == 2 else 2

# Function to calculate the remaining time for a turn
def countdown_timer(start_time, time_limit):
    elapsed_time = time_limit - (pygame.time.get_ticks() - start_time) // 1000
    return max(0, elapsed_time)

# Define players and destination
player_one = {
    'name': 'Player One',
    'cartesian_coords': None,
    'pygame_coords': None,
    'colour': 'red',
}

player_two = {
    'name': 'Player Two',
    'cartesian_coords': None,
    'pygame_coords': None,
    'colour': 'blue',
}

destination = {
    'name': 'Destination',
    'cartesian_coords': None,
    'pygame_coords': None,
    'colour': 'black',
}

# Create Pygame window and initialise entities
app_surf, app_surf_rect = create_app_window(800, 800)

current_turn = 1
time_limit = 10  # Time limit for each turn in seconds
start_time = 0

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
print("\nDestination Location:", destination['coordinates'])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
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


    # Switch turn if time limit is reached
    timer_text = countdown_timer(start_time, time_limit)
    if timer_text == 0:
        current_turn = switch_turn(current_turn)
        start_time = pygame.time.get_ticks()

    # Update display
    app_surf_update(destination, player_one, player_two, timer_text, current_turn)
    refresh_window()
