# Desafio 21 - Reproduzir arquivo mp3.com
# Faça um programa em Phyton que abra e reproduza o áudio de um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('rope.mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
