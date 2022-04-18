# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
fps = 60
frame_per_sec = pygame.time.Clock()

# Creating colors
blue_color = (0, 0, 255)
red_color = (255, 0, 0)
green_color = (0, 255, 0)
black_color = (0, 0, 0)
white_color = (255, 255, 255)

# Other Variables for use in the program
screen_width = 400
screen_height = 600
speed = 5
score = 0
coin_count = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, black_color)

background_image = pygame.image.load(r"C:\Users\Самир\Desktop\pp2\lab9\racer\images\street.png")

# Create a white screen
display_surface = pygame.display.set_mode((400, 600))
display_surface.fill(white_color)
pygame.display.set_caption("Game")

# background sound
pygame.mixer.music.load(r"C:\Users\Самир\Desktop\pp2\lab9\racer\music\back music.wav")
pygame.mixer.music.play(-1) # i use -1 to loop the music

# Create a sprite group Enemy
class Enemy(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Самир\Desktop\pp2\lab9\racer\images\enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    # move method
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)

# Create a sprite group Player
class Player(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Самир\Desktop\pp2\lab9\racer\images\player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    # move method
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Create a sprite group Coin
class Coin(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Самир\Desktop\pp2\lab9\racer\images\gold coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > screen_height:
            self.reset()

class BigCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Самир\Desktop\pp2\lab9\racer\images\red coin.png")
        self.rect = self.image.get_rect()
    def move(self):
        self.rect.move_ip(0, speed)

# Setting up Sprites
player = Player()
enemy = Enemy()
coin = Coin()
big_coin = BigCoin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

big_coins = pygame.sprite.Group()
big_coins.add(big_coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, coin, big_coin, enemy)
# Adding a new User event
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.blit(background_image, (0, 0))
    scores = font_small.render(str(score), True, black_color)
    display_surface.blit(scores, (10, 10))

    counter = font_small.render(str(coin_count), True, black_color)
    display_surface.blit(counter, (380, 10))

    # Check for collision with coins
    collided_coins = pygame.sprite.spritecollide(player, coins, True)
    for coin in collided_coins:
        coin_count += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        new_coin.rect.top = 0
        new_coin.rect.center = (random.randint(40, screen_width - 40), 0)
        if coin_count % 10 == 0:
            speed += 1
            new_coin = BigCoin()
            big_coins.add(new_coin)
            all_sprites.add(new_coin)
            new_coin.rect.top = 0
            new_coin.rect.center = (random.randint(40, screen_width - 40), 0)
    big_coins_collided = pygame.sprite.spritecollide(player, big_coins, True)
    for big_coin in big_coins_collided:
        coin_count += 5
        big_coin.kill()

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        display_surface.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound(r"C:\Users\Самир\Desktop\pp2\lab9\racer\music\crash.wav").play()
        time.sleep(0.5)

        display_surface.fill(red_color)
        display_surface.blit(game_over_text, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    frame_per_sec.tick(fps)
