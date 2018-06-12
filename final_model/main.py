# -*- coding: utf-8 -*-
import pygame
import random
import numpy as np
import math
from evaluacionred import evalred

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)


"""
[-8, -6, 0, -5, -3, -1, 1, 6, 1, 5, 0, -5, 5, -3, -7, -2, -4, 1, -1, 3, 3, 1, 1, 8, 7, 9, 2, 1, 6, -3, 9, -7]0
[-3, -5, -9, -5, -4, 1, 5, 0, 8, 8, 2, 10, -8, 2, -1, -8, 7, 9, -1, -1, 4, -10, 0, -1, 8, -2, 1, -9, 6, 3, 9, -5]8
[9, 3, -1, 9, -2, 2, -9, -10, 8, 7, 0, 10, 10, -10, 9, 1, -2, 1, -2, 7, 0, 10, -7, 3, -10, -6, 4, -9, 5, 7, -9, 4]15
[-7, -4, 4, -5, -7, -8, -4, 3, -4, -8, 0, 10, -1, -1, -1, 4, 8, -7, -9, 9, 10, 9, 0, 10, 9, 5, -2, -1, 3, 5, 10, 6]50
[-7, -4, 4, -5, -7, -8, -4, 3, -4, -8, 0, 10, -1, -1, -9, 4, 8, -7, -9, 9, -2, 2, -10, -1, 8, 4, 1, -8, 3, 5, 7, -7]90
[-7, -4, 4, -5, -7, -8, -4, 3, -4, -8, 0, 10, -1, -1, -9, 4, 8, -4, -9, 9, -2, 2, -10, -1, 4, 4, 1, -8, -1, 3, 9, -6] ultimagen 150
"""
picture = pygame.image.load('berticara.jpg')
picture = pygame.transform.scale(picture, (80, 80))

p = np.array([-7, -4, 4, -5, -7, -8, -4, 3, -4, -8, 0, 10, -1, -1, -9, 4, 8, -4, -9, 9, -2, 2, -10, -1, 4, 4, 1, -8, -1, 3, 9, -6])
def dispd(a,b):
    d=(a-b)/(np.sqrt(np.dot(a-b,a-b)))
    return d



class Bloque(pygame.sprite.Sprite):


    def __init__(self, color, largo, alto):

        super(Bloque,self).__init__()

        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
        self.image=picture


        self.rect = self.image.get_rect()


pygame.init()


pantalla_largo = 1000
pantalla_alto = 700
pantalla = pygame.display.set_mode([pantalla_largo, pantalla_alto])


bloque_lista = pygame.sprite.Group()


listade_todoslos_sprites = pygame.sprite.Group()

for i in range(0):

    bloque = Bloque(NEGRO, 10, 10)


    bloque.rect.x = random.randrange(pantalla_largo)
    bloque.rect.y = random.randrange(pantalla_alto)


    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)


protagonista = Bloque(ROJO, 20, 15)
listade_todoslos_sprites.add(protagonista)
presa=Bloque(ROJO,10,10)
listade_todoslos_sprites.add(presa)
bloque_lista.add(presa)
presa.rect.x=3
presa.rect.y=5

hecho = False


reloj = pygame.time.Clock()

marcador = 0


t=0
dt=1
xp = np.array([pantalla_largo/2, pantalla_alto/2])

"""pygame.mixer.music.load('bertinsongc.wav')
pygame.mixer.music.play()"""
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True


    pantalla.fill(BLANCO)


    pos = pygame.mouse.get_pos()


    protagonista.rect.x = pos[0]
    protagonista.rect.y = pos[1]
    presa.rect.x =pantalla_alto/2
    presa.rect.y =pantalla_alto/2
    xd=np.array([pos[0],pos[1]])
    vp=0


    if np.sqrt(np.dot(xd - xp, xd - xp)) < 300:
        vpp = evalred(p, dispd(xp, xd))
        vp = np.array([vpp[0] - vpp[1], vpp[2] - vpp[3]])

        print(vp)

        if np.sqrt(np.dot(vp, vp)) != 0:
            vp = vp / np.sqrt(np.dot(vp, vp))
        vp =0.5*vp
        t = t + dt
        if (np.sqrt(np.dot(xd - xp,xd - xp))<=250)&(np.sqrt(np.dot(xd - xp,xd - xp))>220):
            vp=2*vp
        elif (np.sqrt(np.dot(xd - xp,xd - xp))<=220)&(np.sqrt(np.dot(xd - xp,xd - xp))>190):
            vp = 4* vp
        elif (np.sqrt(np.dot(xd - xp,xd - xp))<=190)&(np.sqrt(np.dot(xd - xp,xd - xp))>160):
            vp = 6 * vp
        elif (np.sqrt(np.dot(xd - xp,xd - xp))<=160)&(np.sqrt(np.dot(xd - xp,xd - xp))>130):
            vp = 8 * vp
        elif (np.sqrt(np.dot(xd - xp,xd - xp))<=130)&(np.sqrt(np.dot(xd - xp,xd - xp))>100):
            vp = 11 * vp
        elif (np.sqrt(np.dot(xd - xp,xd - xp))<=100)&(np.sqrt(np.dot(xd - xp,xd - xp))>70):
            vp = 14 * vp
        elif (np.sqrt(np.dot(xd - xp,xd - xp))<=70):
            vp = 18 * vp
    xp = xp + vp * dt
    presa.rect.x=xp[0]
    presa.rect.y=xp[1]


    if (np.sqrt(np.dot(xd - xp, xd - xp)) < 200)&(pygame.mixer.music.get_busy()==0):
        pygame.mixer.music.load('bertinsongc.wav')
        pygame.mixer.music.play()
    if np.sqrt(np.dot(xd - xp, xd - xp)) > 300:
        pygame.mixer.music.stop()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)


    for bloque in lista_impactos_bloques:
        marcador += 1
        print(marcador)


    listade_todoslos_sprites.draw(pantalla)
    t=t+dt




    reloj.tick(60)


    pygame.display.flip()

pygame.quit()