import pygame

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('assets/sound/ingame.wav')
sound.play()

pygame.time.delay(int(sound.get_length() * 1000))

pygame.quit()
