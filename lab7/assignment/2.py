import pygame
import os

pygame.init()

import os
screen = pygame.display.set_mode((800, 600))
def design():
    COLOR1 = (186, 85, 211)
    COLOR2 = (75, 0, 130)
    playing_button = pygame.image.load(r"C:\Users\Самир\Desktop\pp2\lab7\images\play-pause-button.png")
    playing_button = pygame.transform.scale(playing_button, (300, 80))
    f1 = pygame.font.SysFont("Arial", 32)
   
    for x in range(800):
        # Интерполяция цветов для каждой строки экрана
        color = pygame.Color(
            int(COLOR1[0] + (COLOR2[0] - COLOR1[0]) * (x / 800)),
            int(COLOR1[1] + (COLOR2[1] - COLOR1[1]) * (x / 800)),
            int(COLOR1[2] + (COLOR2[2] - COLOR1[2]) * (x / 800))
        )
        pygame.draw.line(screen, color, (x, 0), (x, 600))

    for x in range(350):
        color = pygame.Color(
            int(COLOR2[0] + (COLOR1[0] - COLOR2[0]) * (x / 300)),
            int(COLOR2[1] + (COLOR1[1] - COLOR2[1]) * (x / 300)),
            int(COLOR2[2] + (COLOR1[2] - COLOR2[2]) * (x / 300))
        )
        pygame.draw.line(screen, color, (x + 200, 112.5 ), (x + 200, 337.5))

    screen.blit(playing_button, (220, 360))
    
SONG_END = pygame.USEREVENT +  1
pygame.mixer.music.set_endevent(SONG_END)
songs = ['lab7/song/song2.mp3', 'lab7/song/song3.mp3', 'lab7/song/song4.mp3']
curently = None
next_song = 0

def play_music(next_song):
    global curently
    if next_song >= len(songs):
        next_song = 0
    elif next_song < -len(songs):
        next_song = len(songs) - 1
    while next_song == curently:
        next_song += 1
    curently = next_song
    pygame.mixer.music.load(songs[next_song])
    pygame.mixer.music.play()

play_music(next_song)
flag_pause = True

while True:
    design()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                next_song -= 1
                play_music(next_song)
            elif event.key == pygame.K_RIGHT:
                next_song += 1
                play_music(next_song)
            elif event.key == pygame.K_SPACE and flag_pause == True:
                flag_pause = False
                pygame.mixer.music.pause()
            elif event.key == pygame.K_SPACE and flag_pause == False:
                flag_pause = True
                pygame.mixer.music.unpause()
        