#Part 4.3: Visual Part:
import pygame
import sys
import random
import math

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

# Rest of the code remains the same
pygame.init()
app_clock = pygame.time.Clock()

def create_app_window(width, height):
    print(f'\nWelcome. The plane goes from -{width/2} to {width/2} in both the x and y directions')
    pygame.display.set_caption("<App Name> TBD")
    app_dimensions = (width + 10, height + 10)
    app_surf = pygame.display.set_mode(app_dimensions)
    app_surf_rect = app_surf.get_rect()
    return app_surf, app_surf_rect

def app_surf_update(destination, player_one, player_two, timer_text, current_turn):
    app_surf.fill('white')
    pygame.draw.line(app_surf, 'grey', (0, app_surf_rect.height/2), (app_surf_rect.width, app_surf_rect.height/2), width=1)
    pygame.draw.line(app_surf, 'grey', (app_surf_rect.width/2, 0), (app_surf_rect.width/2, app_surf_rect.height), width=1)
    pygame.draw.circle(app_surf, 'black', destination['pygame_coords'], radius=3, width=3)
    pygame.draw.circle(app_surf, player_one['colour'], player_one['pygame_coords'], radius=3, width=2)
    pygame.draw.circle(app_surf, player_two['colour'], player_two['pygame_coords'], radius=3, width=2)
    display_coordinates(player_one['pygame_coords'], player_two['pygame_coords'], destination['pygame_coords'], timer_text, current_turn)

def refresh_window():
    pygame.display.update()
    app_clock.tick(24)

def conv_cartesian_to_pygame_coords(x, y):
    pygame_x = x + app_surf_rect.width / 2
    pygame_y = -y + app_surf_rect.height / 2
    return (pygame_x, pygame_y)

def initialise_entities():
    p1_rand_x, p1_rand_y = random.randint(-400, 400), random.randint(-400, 400)
    player_one['cartesian_coords'] = (p1_rand_x, p1_rand_y)
    player_one['pygame_coords'] = conv_cartesian_to_pygame_coords(p1_rand_x, p1_rand_y)

    p2_rand_x, p2_rand_y = random.randint(-400, 400), random.randint(-400, 400)
    player_two['cartesian_coords'] = (p2_rand_x, p2_rand_y)
    player_two['pygame_coords'] = conv_cartesian_to_pygame_coords(p2_rand_x, p2_rand_y)

    dest_rand_x, dest_rand_y = random.randint(-400, 400), random.randint(-400, 400)
    destination['cartesian_coords'] = (dest_rand_x, dest_rand_y)
    destination['pygame_coords'] = conv_cartesian_to_pygame_coords(dest_rand_x, dest_rand_y)

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

def switch_turn(current_turn):
    return 1 if current_turn == 2 else 2

def countdown_timer(start_time, time_limit):
    elapsed_time = time_limit - (pygame.time.get_ticks() - start_time) // 1000
    return max(0, elapsed_time)

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

app_surf, app_surf_rect = create_app_window(800, 800)

initialise_entities()

print('\nThree entities initialised... here is a raw printout of their dictionaries')
print(destination)
print(player_one)
print(player_two)
print('\nLEFT click inside the window to make player ONE move')
print('RIGHT click inside the window to make player TWO move')
print('You might need to first click the window to select it, then L/R click to make a move')

current_turn = 1
time_limit = 10  # Time limit for each turn in seconds
start_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Move players randomly based on current turn
    if current_turn == 1:
        player_one['pygame_coords'] = hypotenuse_move(player_one['pygame_coords'], destination['pygame_coords'], speed=5)
    else:
        player_two['pygame_coords'] = hypotenuse_move(player_two['pygame_coords'], destination['pygame_coords'], speed=5)

    # Switch turn if time limit is reached
    timer_text = countdown_timer(start_time, time_limit)
    if timer_text == 0:
        current_turn = switch_turn(current_turn)
        start_time = pygame.time.get_ticks()

    # Update display
    app_surf_update(destination, player_one, player_two, timer_text, current_turn)
    refresh_window()
