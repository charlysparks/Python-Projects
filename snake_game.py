# Snake Game
# by Charly

# Game imports
import pygame, sys, random, time

# Check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing erros, exiting...".format(check_errors[1]))
    sys.exit()
else:
    print("(+) PyGame successfully initialized!")

# Game area
play_area = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game')

# Colors
red = pygame.Color(255, 0, 0) # Game Over
green = pygame.Color(0, 255, 0) # Snake
black = pygame.Color(0, 0, 0) # Score
white = pygame.Color(255, 255, 255) # Background
brown = pygame.Color(165, 42, 42) # Food

# FPS Controller
fps_controller = pygame.time.Clock()

# Variables
snake_pos = [100, 45]
snake_body = [[100, 45],[90, 45],[80, 45]]

food_pos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
food_spawn = True

direction = 'RIGHT'
change_to = direction


# Game Over
def game_over():
    my_font = pygame.font.SysFont('monaco', 72)
    gameover_area = myFont.render('Game Over!', True, red)
    gameover_rect = gameover_area.get_rect()
    gameover_rect.midtop = (360, 15)
    play_area.blit(gameover_area, gameover_rect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() # Exit
    sys.exit() # Console Exit

# Main Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT '
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
