import pygame
pygame.mixer.init()
pygame.mixer.music.load('clock.mp3')
pygame.mixer.music.play()
#input()
while pygame.mixer.music.get_busy():
    continue