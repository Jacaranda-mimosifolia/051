import pygame
import random

pygame.mixer.init()
pygame.mixer.music.set_volume(0.6)
# path1 = [""]
print("[国际歌]")
while True:
    i = random.randint(0, 10)
    # print(path1[i], '\n')
    pygame.mixer.music.load(r"D:\CloudMusic\中央乐团合唱队 - 国际歌.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
