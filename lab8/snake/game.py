import pygame as pg 
from random import randint, randrange
pg.init()

w, h, fps, level, step = 700, 600, 2, 0, 50
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Snake Game')
is_running, lose = True, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390), pg.SRCALPHA)
bg = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\snake\images\background.jpg")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\snake\images\game_over.jpg")
gameover = pg.transform.scale(gameover, (390, 390))

class Food:
    def __init__(self):
        # Set random coordinates for food within the game window with a step of 40
        self.x1 = randrange(50, w-50, step)
        self.y1 = randrange(50, h-50, step)
        self.x2 = randrange(50, w-50, step)
        self.y2 = randrange(50, h-50, step)
        self.pic_cherry = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\snake\images\pixel_cherry.png")
        self.pic_banana = pg.image.load(r"C:\Users\Самир\Desktop\pp2\lab8\snake\images\banana_pixel.png")
        self.pic_cherry = pg.transform.scale(self.pic_cherry, (50, 50))
        self.pic_banana = pg.transform.scale(self.pic_banana, (50, 50))

    def draw(self):
        screen.blit(self.pic_cherry, (self.x1, self.y1))

    def draw_banana(self):
        screen.blit(self.pic_banana, (self.x2, self.y2))


class Snake:
    def __init__(self):
        self.speed = 50
        self.body = [[350, 300]]
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = (0, 150, 0)  # Green color

    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a and self.dx == 0:
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_d and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_w and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_s and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))
    
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x1 and self.body[0][1] == f.y1:
            self.score += 1
            self.body.append([1000, 1000]) 
        elif self.body[0][0] == f.x2 and self.body[0][1] == f.y2:
            self.score += 3
            self.body.append([1000, 1000]) 
    
    def self_collide(self):
        global is_running
        if self.body[0] in self.body[1:]:
            lose = True 

    def check_food(self, f:Food): 
        if [f.x1, f.y1] in self.body:
            f.x1 = randrange(50, w-50, step)
            f.y1 = randrange(50, h-50, step)
        elif[f.x2, f.y2] in self.body:
            f.x2 = randrange(50, w-50, step)
            f.y2 = randrange(50, h-50, step)

s = Snake()
f = Food()

while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False
        
    screen.blit(bg, (0, 0))

    f.draw()
    if s.score % 3 == 0:
        f.draw_banana()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.self_collide()
    s.check_food(f)

    counter = score.render(f'Score: {s.score}', True, 'black')
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    if s.score >= 10:
        level += 1
        s.score = 0


    if (s.body[0][0] <= 0 or s.body[0][0] >= 700) or (s.body[0][1] <= 0 or s.body[0][1] >= 600):
        lose = True

    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False  
                lose = False
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (150, 100))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (280, 340))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (280, 360))
        pg.display.flip()

    pg.display.flip()
pg.quit()