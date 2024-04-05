while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  # Выход из программы
        
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