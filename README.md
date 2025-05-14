# 🎮 Dodger Game Using Pygame – Python

A beginner-friendly arcade game built using Python’s **Pygame** library. The objective is to **dodge falling obstacles** by controlling a player rectangle. The game features sound effects, background music, score tracking, and a dynamic “Game Over” screen.

---

## 🧩 Features

- **Player movement** using arrow keys  
- **Randomly generated** falling obstacles  
- **Score tracking** and display  
- **Background music** and sound effects  
- **Dynamic “Game Over”** screen with color cycling  
- Frame rate capped at **60 FPS**

---

## 📋 Game Algorithm

1. **Initialize** Pygame and necessary modules  
2. **Set up** the game window, colors, fonts, and sounds  
3. **Define** player and obstacle mechanics  
4. **Main loop**:  
   - Handle events (quit, movement)  
   - Spawn and move obstacles  
   - Detect collisions  
   - Update and render score  
5. **On collision**:  
   - Play crash sound  
   - Display “Game Over” screen for 4 seconds  
   - Exit gracefully  

---

## 🧠 Libraries Used

- `pygame` – Rendering, events, audio, game loop  
- `random` – Random obstacle positions  
- `time` – Delays and color cycling  
- `sys` – Exiting the game  

---

## 📦 Folder Structure

```
Dodger_Game/
├── dodger_game.py
├── background_music.mp3
├── boing.wav
├── arrgh.wav
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites

- Python 3.x  
- Pygame library  

```bash
pip install pygame
```

### Run the Game

```bash
python dodger_game.py
```

---

## 💻 Source Code

```python
import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Game window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# Player setup
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Obstacles setup
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_gap = 200
obstacle_list = []

# Score and fonts
score = 0
font = pygame.font.SysFont(None, 55)
game_over_font = pygame.font.SysFont(None, 100)

# Sounds
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
boing_sound = pygame.mixer.Sound('boing.wav')
arrgh_sound = pygame.mixer.Sound('arrgh.wav')
boing_sound.set_volume(0.75)
arrgh_sound.set_volume(1.0)

# Clock
clock = pygame.time.Clock()

def display_score(score):
    text = font.render(f"SCORE: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def game_over():
    pygame.mixer.music.stop()
    end_time = time.time() + 4
    idx = 0
    while time.time() < end_time:
        screen.fill(WHITE)
        msg = game_over_font.render("GAME OVER!", True, COLORS[idx])
        screen.blit(
            msg,
            (screen_width//2 - msg.get_width()//2,
             screen_height//2 - msg.get_height()//2)
        )
        pygame.display.flip()
        idx = (idx + 1) % len(COLORS)
        time.sleep(0.2)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += player_speed

    # Spawn obstacles
    if not obstacle_list or obstacle_list[-1].y > obstacle_gap:
        x = random.randint(0, screen_width - obstacle_width)
        obstacle = pygame.Rect(x, -obstacle_height, obstacle_width, obstacle_height)
        obstacle_list.append(obstacle)

    # Move and draw obstacles
    for obs in obstacle_list:
        obs.y += obstacle_speed
        pygame.draw.rect(screen, RED, obs)
        if obs.colliderect(player):
            arrgh_sound.play()
            game_over()
            pygame.quit()
            sys.exit()

    # Remove off-screen obstacles and update score
    for obs in obstacle_list[:]:
        if obs.y > screen_height:
            obstacle_list.remove(obs)
            score += 1
            boing_sound.play()

    display_score(score)
    pygame.draw.rect(screen, BLACK, player)
    pygame.display.flip()
    clock.tick(60)
```

---

## 📹 Gameplay Video

You can watch a quick demo of the game here:

[![Watch the Dodger Game Demo]

https://github.com/user-attachments/assets/978c2cd0-16d0-4097-bc04-ebd58f916979

*Replace `YOUR_VIDEO_ID` with your YouTube video's ID.*

---

## 📝 Full Tutorial

I have written a blog post as a tutorial for reference:

🔗 [Build Dodger Game Using Pygame – Python (CodeSpeedy)](https://www.codespeedy.com/build-dodger-game-using-pygame-python/)

---

## 🎨 Customization Ideas

- **Difficulty levels**: Easy, Medium, Hard  
- **High score** tracking and display  
- **“Try Again” / “Exit”** buttons on Game Over  
- **Login system** with per-player stats  

---

## 🙋‍♂️ Author

**Satyam Prashant**  
🔗 [LinkedIn](https://www.linkedin.com/in/satyam-prashant/)  

---

**Enjoy the game!**
