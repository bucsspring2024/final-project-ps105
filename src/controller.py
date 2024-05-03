import pygame
import random

"""Initializes pygame"""
pygame.init()

"""Screen dimensions"""
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

"""Colors"""
"""background"""
WHITE = (255, 255, 255)
"""platforms"""
BLACK = (0, 0, 0)
"""player"""
RED = (255, 0, 0)

"""Platform dimensions (black boxes)"""
PLATFORM_WIDTH = 80
PLATFORM_HEIGHT = 20

"""Player dimensions (red box)"""
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

"""Gravity"""
GRAVITY = 0.5

"""Jump height"""
JUMP_HEIGHT = 12

"""Platform speed"""
PLATFORM_SPEED = 5

"""Font settings"""
FONT_SIZE = 24
FONT_COLOR = BLACK
FONT_POS_JUMP = (SCREEN_WIDTH // 2, 50) 
FONT_POS_GAME_OVER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3) 

"""Button stuff"""
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 40
BUTTON_COLOR = (100, 100, 255)
BUTTON_TEXT_COLOR = WHITE
BUTTON_TEXT_SIZE = 20

"""Sets up the screen"""
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doodle Jump")

font = pygame.font.Font(None, FONT_SIZE)

"""Defines the Player class"""
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT
        self.velocity = 0
        self.jump_count = 0

    def update(self):
        """Track mouse movement (horizonally from side to side)"""
        mouse_x, _ = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

        self.velocity += GRAVITY
        self.rect.y += self.velocity

        """Checks if player falls below the screen"""
        if self.rect.top > SCREEN_HEIGHT:
            game_over()

        """Checks for collision with platforms"""
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.rect.bottom = hits[0].rect.top
            self.velocity = -JUMP_HEIGHT
            self.jump_count += 1

"""Defines the Platform class"""
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.y += PLATFORM_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.left = random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH)

"""initializes the game"""
def initialize_game():

    """Create groups for sprites"""
    global all_sprites, platforms, player
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    """Adds platforms"""
    for _ in range(10):
        platform = Platform(random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH), random.randint(0, SCREEN_HEIGHT))
        platforms.add(platform)
        all_sprites.add(platform)

    """Creates the player"""
    player = Player()
    all_sprites.add(player)

"""Display game over screen"""
def game_over():
    while True:
        screen.fill(WHITE)
        game_over_text = font.render("Game Over", True, FONT_COLOR)
        screen.blit(game_over_text, (FONT_POS_GAME_OVER[0] - game_over_text.get_width() // 2, FONT_POS_GAME_OVER[1] - 2 * game_over_text.get_height()))

        """Display's the player's score"""
        score_text = font.render(f"Your score: {player.jump_count}", True, FONT_COLOR)
        screen.blit(score_text, (FONT_POS_GAME_OVER[0] - score_text.get_width() // 2, FONT_POS_GAME_OVER[1] + score_text.get_height() // 2))  

        play_again_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
        quit_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, BUTTON_COLOR, play_again_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, quit_rect)

        play_again_text = font.render("Play Again", True, BUTTON_TEXT_COLOR)
        quit_text = font.render("Quit", True, BUTTON_TEXT_COLOR)
        screen.blit(play_again_text, (play_again_rect.centerx - play_again_text.get_width() // 2, play_again_rect.centery - play_again_text.get_height() // 2))
        screen.blit(quit_text, (quit_rect.centerx - quit_text.get_width() // 2, quit_rect.centery - quit_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_again_rect.collidepoint(mouse_x, mouse_y):
                    """restarts the game"""
                    initialize_game()
                    return
                elif quit_rect.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    quit()

""""Initialize the game"""
initialize_game()

"""Main loop"""
running = True
game_started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_started = True

    if game_started:
        all_sprites.update()

    screen.fill(WHITE)

    """Click to start"""
    if not game_started:
        click_to_start_text = font.render("Click to start", True, FONT_COLOR)
        screen.blit(click_to_start_text, (SCREEN_WIDTH // 2 - click_to_start_text.get_width() // 2, SCREEN_HEIGHT // 2))

    all_sprites.draw(screen)

    """Display jump count"""
    jump_text = font.render(f"Jumps: {player.jump_count}", True, FONT_COLOR)
    screen.blit(jump_text, (FONT_POS_JUMP[0] - jump_text.get_width() // 2, FONT_POS_JUMP[1]))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()