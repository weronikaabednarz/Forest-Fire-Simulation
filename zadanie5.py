import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import pygame
import random

pygame.init()
win = pygame.display.set_mode((800, 400))
# wyświetlenie okna gry
pygame.display.set_caption("Pożar lasu")
clock = pygame.time.Clock()

# Wczytanie obrazu
image = Image.open("mapa.bmp").convert("RGB")

# Konwersja obrazu na tablicę numpy
img_array = np.array(image)


trees = []

class Tree:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.z = 0      #ile razy plonie zanim sie spali
        self.w = 0      #ile razy sie zweglilo
        self.g = 0      #ile byla gleba
        self.o = 0      #ile czasu woda wsiaka w ziemie

trees =  [[Tree(x,y, img_array[x,y]) for x in range(100)] for y in range(200)]


land = []

#stan początkowy
for x in range(100):
    for y in range(200):
        if img_array[x,y][1] < img_array[x,y][2]:   #woda
            img_array[x,y] = [175, 230, 237]
            pygame.draw.rect(win, [175, 230, 237], (y*4, x*4, 4, 4))
        else:           #drzewa
            #pygame.draw.rect(win, [157, 237, 128], (y*4, x*4, 800, 400))
            img_array[x,y] = [13, 163, 66]
            pygame.draw.rect(win, [13, 163, 66], (y*4, x*4, 4, 4))
            land.append(trees[y][x])   
for t in land:
    img_array[t.x,t.y] = trees[t.y][t.x].color
    pygame.draw.rect(win, img_array[t.x,t.y], (t.y*4, t.x*4, 4, 4))          
  
max_fire = 4
max_wegiel = 6
max_gleba = 8
max_nawodnienie = 4
def step():

    while True:
        x = random.randint(50, 99)
        y = random.randint(150, 199)
        if np.array_equal (img_array[x,y], [13, 163, 66]):
            trees[y][x].color = [255, 0, 13]
            for t in land:
                img_array[t.x,t.y] = trees[t.y][t.x].color
                pygame.draw.rect(win, img_array[t.x,t.y], (t.y*4, t.x*4, 4, 4)) 
            break
        

def final_step(pas):

    i = 20*(pas-1)
    j = 20*pas
    for x in range(100):
        for y in range(i,j):
            if np.array_equal (img_array[x,y], [255, 0, 13]):
                trees[y][x].color = [175, 230, 237]
    for t in land:
        img_array[t.x,t.y] = trees[t.y][t.x].color
        pygame.draw.rect(win, img_array[t.x,t.y], (t.y*4, t.x*4, 4, 4)) 


def next_step():
    for t in land:
            if np.array_equal (img_array[t.x,t.y], [13, 163, 66]):
                water_neighbors = 0
                fire_neighbors = 0
                for a in range(-1,2):
                    for b in range(-1,2):
                        if t.x+a >= 0 and t.y+b >= 0 and t.x+a < 100 and t.y+b < 200 and not (a==0 and b==0):
                            if np.array_equal (img_array[t.x+a,t.y+b],[175, 230, 237]):
                                water_neighbors += 1
                            if np.array_equal (img_array[t.x+a,t.y+b],[255, 0, 13]):
                                fire_neighbors += 1
                chance = fire_neighbors * 0.5 - water_neighbors * 0.4 #prawdopodbienstwo

                if random.random() < chance:
                    trees[t.y][t.x].color = [255, 0, 13]
                else: 
                    trees[t.y][t.x].color = img_array[t.x,t.y]
            if np.array_equal (trees[t.y][t.x].color,[255, 0, 13]):
                trees[t.y][t.x].z += 1
            if np.array_equal (trees[t.y][t.x].color,[175, 230, 237]):
                trees[t.y][t.x].o += 1
            if np.array_equal (trees[t.y][t.x].color,[184, 145, 90]):
                trees[t.y][t.x].g +=1
            if np.array_equal (trees[t.y][t.x].color,[51, 44, 44]):
                trees[t.y][t.x].w += 1
            if  trees[t.y][t.x].z == max_fire:
                trees[t.y][t.x].color = [51, 44, 44]
            if  trees[t.y][t.x].o == max_nawodnienie:
                trees[t.y][t.x].color = [13, 163, 66]
            if trees[t.y][t.x].w == max_wegiel:
                trees[t.y][t.x].color = [184, 145, 90]
            if trees[t.y][t.x].g == max_gleba:
                trees[t.y][t.x].color = [13, 163, 66]

    for t in land:
        img_array[t.x,t.y] = trees[t.y][t.x].color
        pygame.draw.rect(win, img_array[t.x,t.y], (t.y*4, t.x*4, 4, 4)) 


run = True
# pętla główna

while run:
    clock.tick(60)

    next_step()
    pygame.time.delay(100) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_SPACE]:
                step()
            if keys[pygame.K_1]:
                final_step(1)
            if keys[pygame.K_2]:
                final_step(2)
            if keys[pygame.K_3]:
                final_step(3)
            if keys[pygame.K_4]:
                final_step(4)
            if keys[pygame.K_5]:
                final_step(5)
            if keys[pygame.K_6]:
                final_step(6)
            if keys[pygame.K_7]:
                final_step(7)
            if keys[pygame.K_8]:
                final_step(8)
            if keys[pygame.K_9]:
                final_step(9)
            if keys[pygame.K_0]:
                final_step(10)

    pygame.display.flip()
