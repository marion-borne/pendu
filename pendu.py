import pygame
import random
import os

# Initialisation de la bibliothèque pygame
pygame.init()

# Création d'une fenêtre de 600x800 pixels
win = pygame.display.set_mode((600, 800))

# Fonction pour construire le chemin d'accès à une image
def image_path(name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, name)

# Chargement des images du pendu
hangman_images = [pygame.image.load(image_path(f'pendu{i}.png')) for i in range(1, 8)]

# Fonction pour lire les mots du fichier 'mots.txt'
def lire_mots():
    with open(image_path('mots.txt'), 'r') as f:
        mots = f.read().splitlines()
    return mots

# Fonction pour ajouter un mot au fichier 'mots.txt'
def ajouter_mot(mot):
    with open(image_path('mots.txt'), 'a') as f:
        f.write(f'\n{mot}')

# Fonction pour ajouter un score au fichier 'scores.txt'
def ajouter_score(nom, score):
    with open(image_path('scores.txt'), 'a') as f:
        f.write(f'joueur "{nom}" score "{score}"\n')

# Fonction pour jouer une manche du jeu
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

# Demande du nom du joueur
nom_joueur = input('Entrez votre nom : ')
# Choix d'un mot aléatoire à deviner
mot_a_deviner = random.choice(lire_mots())
# Initialisation du tableau du pendu
pendu = ['_',] * len(mot_a_deviner)
# Initialisation du nombre d'essais
essais = 0
# Initialisation du score
score = 0

# Affichage de l'image initiale
win.blit(hangman_images[0], (0,0))
pygame.display.flip()

# Boucle principale du jeu
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        essais = jouer(mot_a_deviner, pendu, essais)
        win.blit(hangman_images[min(essais, 6)], (0,0))
        pygame.display.flip()
        pygame.time.delay(100)
        # Si le mot a été deviné
        if '_' not in pendu:
            score += 1
            print(f'Bravo {nom_joueur}! Votre score est maintenant de {score}.')
            ajouter_score(nom_joueur, score)
            reponse = input('Voulez-vous continuer à jouer ? Tapez P pour continuer ou Q pour quitter : ')
            if reponse.lower() == 'q':
                pygame.quit()
                exit()
            elif reponse.lower() == 'p':
                mot_a_deviner = random.choice(lire_mots())
                pendu = ['_',] * len(mot_a_deviner)
                essais = 0
                win.blit(hangman_images[0], (0,0))
                pygame.display.flip()
        # Si toutes les images du pendu ont été affichées
        elif essais >= 6:  
            print(f'Désolé {nom_joueur}, vous n\'avez pas trouvé le mot. Le mot était "{mot_a_deviner}".')
            ajouter_score(nom_joueur, score)
            reponse = input('Voulez-vous continuer à jouer ? Tapez P pour continuer ou Q pour quitter : ')
            if reponse.lower() == 'q':
                pygame.quit()
                exit()
            elif reponse.lower() == 'p':
                mot_a_deviner = random.choice(lire_mots())
                pendu = ['_',] * len(mot_a_deviner)
                essais = 0
                win.blit(hangman_images[0], (0,0))
                pygame.display.flip()
# Gestion des erreurs
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
