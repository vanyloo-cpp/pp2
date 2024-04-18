import pygame as pg
import random, time
pg.init()

w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pg.display.set_mode((w, h))
pg.display.set_caption('racer')
clock = pg.time.Clock()
y = 0
ry = 2
step, enemy_step, score, score_coin = 5, 5, 0, 0
game_over = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\race\images\gameover.jpg")
bg = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\race\images\AnimatedStreet.png")
game_over = pg.transform.scale(game_over, (w, h))
# Set font for text
score_font = pg.font.SysFont("Verdana", 20)
score_coins = pg.font.SysFont("Verdana", 20)

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\race\images\Enemy.png") # load image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0) # set random coordinates

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step) # move this sprite from top to bottom
        if(self.rect.bottom > h + 90): 
            score += 1 # add 1 when this sprite moves down without colliding with the player
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface): # draw sprite
        surface.blit(self.image, self.rect)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\race\images\Player.png") # load image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self): # move player sprite with keyboard keys
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pg.K_a]:
                self.rect.move_ip(-step, 0)

        if self.rect.right < w:
            if pressed_keys[pg.K_d]:
                self.rect.move_ip(step, 0)

        if self.rect.top > 0:
            if pressed_keys[pg.K_w]:
                self.rect.move_ip(0, -step)
            
        if self.rect.bottom < h:
            if pressed_keys[pg.K_s]:
                self.rect.move_ip(0, step)        

    def draw(self, surface): # draw sprite
        surface.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\race\images\coin.png") # load image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130)) # random coordinates for the coin

    def draw(self): # draw coin
        screen.blit(self.image, self.rect)
# create objects
p = Player()
e = Enemy()
c = Coin()
# create groups and add objects to them
enemies = pg.sprite.Group()
enemies.add(e)

coins = pg.sprite.Group()
coins.add(c)

# main loop
while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    # animate the moving background
    screen.blit(pg.transform.scale(bg, (w, h)), (0, y % h))
    screen.blit(pg.transform.scale(bg, (w, h)), (0, -h + (y % h)))
    y += ry

    p.update()
    e.update()
    # check collision between player and enemy sprites
    if pg.sprite.spritecollideany(p, enemies):
        lose = True # start "game over" loop

    for c in coins:
        c.draw()
        if pg.sprite.collide_rect(p, c): # if player sprite gets the coin
            c.kill() 
            score_coin += 1
            new = Coin() # create a new coin object
            coins.add(new) # add the new object to coins group

    e.draw(screen)
    p.draw(screen)

    # "game over" loop
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            else:
                lose = False
        screen.blit(game_over, (0, 0))
        pg.display.flip()
    # display score at the top right corner
    counter = score_coins.render(f'Coins: {score_coin}', True, 'black')
    screen.blit(counter, (300, 10))
    
    pg.display.flip()
pg.quit()