# Importation des bibliothèques nécessaires
import pygame
import random

# Initialisation de la bibliothèque pygame
pygame.init()

# Création d'une fenêtre de 600x800 pixels
win = pygame.display.set_mode((600, 800))

# Chargement des images du pendu
hangman_images = [pygame.image.load('pendu1.png'), pygame.image.load('pendu2.png'), pygame.image.load('pendu3.png'), pygame.image.load('pendu4.png'), pygame.image.load('pendu5.png'), pygame.image.load('pendu6.png'), pygame.image.load('pendu7.png')]

# Fonction pour lire les mots du fichier 'mots.txt'
def lire_mots():
    with open('mots.txt', 'r') as f:
        mots = f.read().splitlines()
    print(mots)  # Ajoutez cette ligne pour le débogage
    return mots


# Fonction pour ajouter un mot au fichier 'mots.txt'
def ajouter_mot(mot):
    with open('mots.txt', 'a') as f:
        f.write(f'\n{mot}')

# Fonction pour ajouter un score au fichier 'scores.txt'
def ajouter_score(nom, score):
    with open('scores.txt', 'a') as f:
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
        essais = jouer(mot_a_deviner, pendu, essais)
        win.blit(hangman_images[essais], (0,0))
        pygame.display.flip()
        pygame.time.delay(100)
        # Si le mot a été deviné, on augmente le score et on choisit un nouveau mot
        if '_' not in pendu:
            score = 1
            print(f'Bravo {nom_joueur}! Votre score est maintenant de {score}.')
            ajouter_score(nom_joueur, score)
            reponse = input('Voulez-vous continuer à jouer ? Tapez P pour continuer ou Q pour quitter : ')
            if reponse.lower() == 'q':
                pygame.quit()
            elif reponse.lower() == 'p':
                mot_a_deviner = random.choice(lire_mots())
                pendu = ['_',] * len(mot_a_deviner)
                essais = 0
                win.blit(hangman_images[essais], (0,0))
                pygame.display.flip()
        elif essais == 6:  # Si toutes les images du pendu ont été affichées
            score = 0
            print(f'Désolé {nom_joueur}, vous n\'avez pas trouvé le mot. Le mot était "{mot_a_deviner}". Votre score est de {score}.')
            ajouter_score(nom_joueur, score)
            reponse = input('Voulez-vous continuer à jouer ? Tapez P pour continuer ou Q pour quitter : ')
            if reponse.lower() == 'q':
                pygame.quit()
            elif reponse.lower() == 'p':
                mot_a_deviner = random.choice(lire_mots())
                pendu = ['_',] * len(mot_a_deviner)
                essais = 0
                win.blit(hangman_images[essais], (0,0))
                pygame.display.flip()
# Gestion des erreurs
except Exception as e:
    print(f"Une erreur s'est produite : {e}")