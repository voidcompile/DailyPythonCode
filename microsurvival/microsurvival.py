# Import necessary libraries
import pygame        # Game development library for graphics, events, sprites
import random        # Used for generating random positions/values
import sys           # Allows exiting the program
import time          # Used for tracking survival time

# Game screen settings
WIDTH, HEIGHT = 800, 600        # Window size
FPS = 60                        # Frames per second (smooth gameplay)

# Player and object sizes/speeds
CELL_SIZE = 40                  # Size of the player's cell
START_SPEED = 5                 # Starting movement speed

# Define RGB color values
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Initialize Pygame engine
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))    # Create game window
pygame.display.set_caption("Microsurvival")          # Set game title
clock = pygame.time.Clock()                          # Create a clock to control FPS
font = pygame.font.SysFont(None, 24)                 # Default font for drawing text

# Global variable to track the best survival time
high_score = 0


# Define the player's Cell class
class Cell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()                         # Call parent class constructor
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))  # Create a square surface for the cell
        self.image.fill(BLUE)                      # Fill it with blue color
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Start at screen center

        # Energy and survival stats
        self.atp = 100             # Current ATP (energy)
        self.atp_max = 100         # Max ATP
        self.speed = START_SPEED   # Movement speed
        self.xp = 0                # XP (experience points)
        self.level_up_ready = False  # Flag to show upgrade option
        self.shield = False        # Shield against viruses
        self.recovery = False      # Rare evolution: slow ATP recovery

    def update(self, keys_pressed, environment):
        # Move the cell based on key input
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

        # ATP decreases over time, faster in heat or toxins
        atp_loss = 0.15 + environment["heat"] * 0.1 + environment["toxins"] * 0.05
        self.atp -= atp_loss

        # Passive ATP recovery if evolved
        if self.recovery:
            self.atp += 0.03  # very slow healing
        self.atp = max(0, min(self.atp, self.atp_max))  # Clamp ATP between 0 and max

        # Prevent cell from leaving the screen
        self.rect.clamp_ip(screen.get_rect())

        # Check if ready to level up
        if self.xp >= 150:
            self.level_up_ready = True

    def level_up(self, choice):
        # Upgrade system based on player's choice
        if choice == 1:
            self.atp_max += 50         # Max ATP increase
        elif choice == 2:
            self.speed += 1            # Speed increase
        elif choice == 3:
            self.shield = True         # One-time virus protection
        elif choice == 4:
            self.recovery = True       # Rare evolution: passive ATP regen
        self.xp = 0                     # Reset XP
        self.level_up_ready = False    # Remove level up prompt

# Define a class for food particles the cell can collect
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Call the Sprite constructor
        self.image = pygame.Surface((20, 20))  # Small square shape
        self.image.fill(GREEN)  # Green color represents nutrients
        # Random position within the screen
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))


# Define a class for viruses that move randomly and harm the cell
class Virus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Call the Sprite constructor
        self.image = pygame.Surface((30, 30))  # Slightly larger than food
        self.image.fill(RED)  # Red color represents danger
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        # Random direction and speed
        self.vx = random.choice([-1, 1]) * random.uniform(1, 2)
        self.vy = random.choice([-1, 1]) * random.uniform(1, 2)

    def update(self):
        # Move the virus
        self.rect.x += self.vx
        self.rect.y += self.vy
        # Bounce off screen edges
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy *= -1


# Function to display text messages in the center of the screen
def show_text_lines(lines, y_offset=0):
    screen.fill(GRAY)  # Clear the screen with a background
    for i, line in enumerate(lines):
        # Render each line of text and position it vertically
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (WIDTH // 2 - 200, HEIGHT // 2 + y_offset + i * 30))
    pygame.display.flip()  # Update the screen with text


# Function to randomly vary environment values (heat, toxins)
def update_environment(environment):
    # Slight random changes to simulate fluctuation
    environment["heat"] += random.uniform(-0.02, 0.02)
    environment["toxins"] += random.uniform(-0.015, 0.015)

    # Clamp values between 0 and 1
    environment["heat"] = max(0.0, min(1.0, environment["heat"]))
    environment["toxins"] = max(0.0, min(1.0, environment["toxins"]))

# Main game loop where the game runs continuously until quit or game over
def main_game():
    global high_score  # Access global variable to track high score

    # Initialize all sprite groups
    all_sprites = pygame.sprite.Group()
    foods = pygame.sprite.Group()  # Group to hold all food objects
    viruses = pygame.sprite.Group()  # Group to hold all virus objects

    # Create the player cell and add it to the sprite group
    player = Cell()
    all_sprites.add(player)

    # Create food objects and add them to the respective groups
    for _ in range(10):  # Create 10 food items
        food = Food()
        all_sprites.add(food)
        foods.add(food)

    # Create virus objects and add them to the respective groups
    for _ in range(8):  # Create 8 viruses
        virus = Virus()
        all_sprites.add(virus)
        viruses.add(virus)

    # Start the survival timer
    start_time = time.time()
    running = True
    game_over = False

    # Environment settings: heat and toxins, which affect the player
    environment = {
        "heat": random.uniform(0.0, 0.3),  # Initial heat level (0-1)
        "toxins": random.uniform(0.0, 0.3)  # Initial toxin level (0-1)
    }

    while running:
        clock.tick(FPS)  # Maintain the game at the desired frames per second
        keys = pygame.key.get_pressed()  # Get current key states

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Close the game window
                sys.exit()  # Exit the program

        if not game_over:
            player.update(keys, environment)  # Update player's position and energy
            for virus in viruses:  # Update each virus in the game
                virus.update()

            # Check for collisions between the player and food items
            food_hit = pygame.sprite.spritecollide(player, foods, True)
            for food in food_hit:
                player.atp = min(player.atp_max, player.atp + 20)  # Increase ATP (energy)
                player.xp += 30  # Increase XP for collecting food
                new_food = Food()  # Generate a new food item
                all_sprites.add(new_food)
                foods.add(new_food)

            # Check for collisions between the player and viruses
            if pygame.sprite.spritecollideany(player, viruses):
                if player.shield:
                    player.shield = False  # Temporary shield protects from one virus hit
                else:
                    game_over = True  # Game over if a virus hits the player
                    survival_time = int(time.time() - start_time)
                    if survival_time > high_score:
                        high_score = survival_time  # Update high score if necessary
                    show_text_lines([
                        f"💀 You were infected!",
                        f"⏱️ Survival Time: {survival_time} sec",
                        f"🏆 Best Time: {high_score} sec",
                        "Press R to restart or ESC to quit"
                    ])
                    continue

            # If ATP (energy) runs out, game over
            if player.atp <= 0:
                game_over = True
                survival_time = int(time.time() - start_time)
                if survival_time > high_score:
                    high_score = survival_time
                show_text_lines([
                    f"💤 You ran out of ATP!",
                    f"⏱️ Survival Time: {survival_time} sec",
                    f"🏆 Best Time: {high_score} sec",
                    "Press R to restart or ESC to quit"
                ])
                continue

            # If player reaches enough XP, prompt for upgrade
            if player.level_up_ready:
                show_text_lines([
                    "🎉 UPGRADE AVAILABLE! Choose:",
                    "1. 🔋 Max ATP +50",
                    "2. ⚡ Speed +1",
                    "3. 🛡️ Virus Shield (one-time)",
                    "4. 🧬 Evolution: Passive ATP Recovery"
                ])
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                player.level_up(1)  # Upgrade ATP
                                waiting = False
                            elif event.key == pygame.K_2:
                                player.level_up(2)  # Upgrade speed
                                waiting = False
                            elif event.key == pygame.K_3:
                                player.level_up(3)  # Activate shield
                                waiting = False
                            elif event.key == pygame.K_4:
                                player.level_up(4)  # Evolution upgrade
                                waiting = False

        else:
            # If game is over, check for restart or quit
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:  # Restart game if R key is pressed
                return  # Restart the game
            if keys[pygame.K_ESCAPE]:  # Quit game if ESC key is pressed
                pygame.quit()
                sys.exit()

        if not game_over:
            # Update the screen by drawing all sprites
            screen.fill(GRAY)
            all_sprites.draw(screen)

            # Display ATP bar (current vs max ATP)
            pygame.draw.rect(screen, BLACK, (10, 10, 200, 20))
            pygame.draw.rect(screen, GREEN, (10, 10, int(200 * player.atp / player.atp_max), 20))
            screen.blit(font.render("ATP", True, WHITE), (215, 10))

            # Display XP bar (progress toward level up)
            pygame.draw.rect(screen, BLACK, (10, 40, 200, 10))
            pygame.draw.rect(screen, BLUE, (10, 40, int(200 * player.xp / 150), 10))
            screen.blit(font.render("XP", True, WHITE), (215, 35))

            # Show survival time
            current_time = int(time.time() - start_time)
            screen.blit(font.render(f"Time: {current_time}s", True, WHITE), (WIDTH - 120, 10))

            # Show environment variables: heat and toxins
            screen.blit(font.render(f"Heat: {environment['heat']:.2f}", True, WHITE), (10, 60))
            screen.blit(font.render(f"Toxins: {environment['toxins']:.2f}", True, WHITE), (10, 80))

            pygame.display.flip()  # Update the display

# Main game loop
while True:
    main_game()  # Start a new game
