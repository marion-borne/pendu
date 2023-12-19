import pygame
import random

pygame.init()

win = pygame.display.set_mode((600, 800))

hangman_images = [pygame.image.load('pendu1.png'), pygame.image.load('pendu2.png'), pygame.image.load('pendu3.png'), pygame.image.load('pendu4.png'), pygame.image.load('pendu5.png'), pygame.image.load('pendu6.png'), pygame.image.load('pendu7.png')]

def lire_mots():
    with open('mots.txt', 'r') as f:
        mots = f.read().splitlines()
    return mots

def ajouter_mot(mot):
    with open('mots.txt', 'a') as f:
        f.write(f'\n{mot}')

def jouer(mot, pendu, essais):
    lettre = input('Entrez une lettre : ')
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                pendu[i] = lettre
    else:
        essais += 1
    print(' '.join(pendu))
    return essais

mot_a_deviner = random.choice(lire_mots())
pendu = ['_',] * len(mot_a_deviner)
essais = 0

# Afficher l'image initiale
win.blit(hangman_images[0], (0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    essais = jouer(mot_a_deviner, pendu, essais)
    win.blit(hangman_images[essais], (0,0))
    pygame.display.flip()
    pygame.time.delay(100)