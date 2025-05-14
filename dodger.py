# Import required libraries
import pygame
import sys
import random
import time

# Initialize Pygame and set up the game window
pygame.init()

# Set the dimensions for the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the game window
pygame.display.set_caption("Dodger Game")  # Set the title of the window

# Define colors using RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]  # List of colors for game over text

# Set up player properties and position
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2  # Start player at the center bottom of the screen
player_y = screen_height - player_height - 10
player_speed = 5  # Player movement speed
player = pygame.Rect(player_x, player_y, player_width, player_height)  # Create a rectangle to represent the player

# Set up obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5  # Speed of falling obstacles
obstacle_gap = 200  # Minimum distance between consecutive obstacles
obstacle_list = []  # List to keep track of obstacles

# Initialize the score and fonts for displaying text
score = 0
font = pygame.font.SysFont(None, 55)  # Font for displaying score
game_over_font = pygame.font.SysFont(None, 100)  # Font for displaying game over text

# Load and set up background music and sound effects
pygame.mixer.music.load('background_music.mp3')  # Load background music file
pygame.mixer.music.set_volume(0.5)  # Set volume for background music
pygame.mixer.music.play(-1)  # Play background music in a loop
boing_sound = pygame.mixer.Sound('boing.wav')  # Load sound effect for scoring
arrgh_sound = pygame.mixer.Sound('arrgh.wav')  # Load sound effect for collision

# Set volume levels for sound effects
boing_sound.set_volume(0.75)  # Volume for scoring sound
arrgh_sound.set_volume(1.0)  # Volume for collision sound

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Function to display the current score on the screen
def display_score(score):
    score_text = font.render(f'SCORE: {score}', True, BLACK)  # Render the score text
    screen.blit(score_text, [10, 10])  # Draw the score text on the screen at the top-left corner

# Function to handle the game over sequence
def game_over():
    pygame.mixer.music.stop()  # Stop the background music
    end_time = time.time() + 4  # Set the duration for the game over display
    color_index = 0  # Index to cycle through colors
    while time.time() < end_time:
        screen.fill(WHITE)  # Clear the screen
        game_over_text = game_over_font.render('GAME OVER!', True, COLORS[color_index])  # Render game over text
        screen.blit(game_over_text, [screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2])  # Center the text
        pygame.display.flip()  # Update the display
        color_index = (color_index + 1) % len(COLORS)  # Cycle through colors
        time.sleep(0.2)  # Wait for 0.2 seconds before changing color

# Main game loop
running = True  # Variable to keep the game loop running
while running:
    screen.fill(WHITE)  # Clear the screen for each frame

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the window close button is clicked
            pygame.quit()  # Quit Pygame
            sys.exit()  # Exit the program

    # Handle player movement based on keyboard input
    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
    if keys[pygame.K_LEFT] and player.x > 0:  # Move player left if left arrow key is pressed
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:  # Move player right if right arrow key is pressed
        player.x += player_speed

    # Spawn new obstacles at random positions
    if len(obstacle_list) == 0 or obstacle_list[-1].y > obstacle_gap:  # Check if a new obstacle should be spawned
        obstacle_x = random.randint(0, screen_width - obstacle_width)  # Random x position for the new obstacle
        obstacle_y = 0 - obstacle_height  # Start above the screen
        obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)  # Create a new obstacle rectangle
        obstacle_list.append(obstacle)  # Add the new obstacle to the list

    # Move obstacles down the screen
    for obstacle in obstacle_list:
        obstacle.y += obstacle_speed  # Move the obstacle down
        pygame.draw.rect(screen, RED, obstacle)  # Draw the obstacle

        # Check for collision with the player
        if obstacle.colliderect(player):
            arrgh_sound.play()  # Play collision sound
            game_over()  # Show game over screen
            pygame.quit()  # Quit Pygame
            sys.exit()  # Exit the program

    # Remove obstacles that are off the screen and update the score
    for obstacle in obstacle_list[:]:  # Iterate over a copy of the obstacle list
        if obstacle.y > screen_height:  # Check if the obstacle is off the screen
            obstacle_list.remove(obstacle)  # Remove the obstacle from the list
            score += 1  # Increment the score
            boing_sound.play()  # Play scoring sound

    # Display the current score
    display_score(score)

    # Draw the player rectangle on the screen
    pygame.draw.rect(screen, BLACK, player)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)  # Limit the frame rate to 60 frames per second