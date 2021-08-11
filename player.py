
from my_song import my_note

import os
import sys
import pygame
from pygame.constants import QUIT

num_samples = 24000  # 采样数
sampling_rate = 48000.0  # 采样频率
amplitude = 1000  # 最大幅值，最大值32767，需是整数
file_name = "sun.wav"

# 音符
notes = ['la_low', 'mi', 'mi', 'mi', 'fa',
         'mi', 'mi', 'fa', 'sol',
         'la', 'la', 'sol', 'sol',
         'mi',
         'la_low', 're', 're', 're', 'mi',
         're', 'mi',
         'sol', 'mi', 'sol', 'si_low', 'do',
         'la_low',
         'la_low', 'do', 'mi',
         'la', 'sol', 'la', 'sol',
         'la', 'sol', 'la', 'sol', 'sol',
         'mi',
         're', 'la', 'sol',
         'mi', 're', 'mi',
         're', 'la', 'fa',
         'mi', 're', 'mi', 'sol', 'si', 'do',
         'la_low', ]
# 音符对应的时长
times = [1, 1, 1, 3/4, 1/4,
         5/2, 1/2, 1/2, 1/2,
         3/2, 1/2, 1, 1,
         4,
         1, 1, 1, 3/4, 1/4,
         2, 2,
         3/4, 1/4, 2, 3/4, 1/4,
         5,
         1, 1, 1,
         3/4, 1/4, 11/4, 1/4,
         3/4, 1/4, 2, 3/4, 1/4,
         5,
         1, 1, 1,
         3/4, 1/4, 4,
         1, 1, 1,
         3/4, 1/4, 1, 1, 3/4, 1/4,
         4, ]

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([600, 400])
pygame.display.set_caption("太阳照常升起")

background_img = pygame.image.load('image/image1.jpg')
screen.blit(background_img, (0, 0))
pygame.display.update()

if os.path.exists(file_name):
    pass
else:
    background_img = pygame.image.load('image/image2.jpg')
    screen.blit(background_img, (0, 0))
    pygame.display.update()

    note = my_note(num_samples, sampling_rate, amplitude)
    note.generate_audio(file_name, notes, times)

background_img = pygame.image.load('image/image3.jpg')
screen.blit(background_img, (0, 0))
pygame.display.update()

pygame.mixer.music.load(file_name)
pygame.mixer.music.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
