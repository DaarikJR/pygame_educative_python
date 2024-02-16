import pygame
import sys
import random

pygame.init()

fenetre = pygame.display.set_mode((640,480))

background = pygame.image.load("./assets/img/background.jpg").convert()
perso = pygame.image.load("./assets/img/perso.png").convert_alpha()
autre_perso = pygame.image.load("./assets/img/mario.webp").convert_alpha()
explosion_image = pygame.image.load("./assets/img/explosion.png").convert_alpha()
# Load the image for the second appearance of the first character
autre_perso2 = pygame.image.load("./assets/img/kingboo.png").convert_alpha()
champignon = pygame.image.load("./assets/img/champignon.png").convert_alpha()  # Charger l'image du champignon

perso_rect = perso.get_rect()
perso_rect.topleft = (320,240)

autre_perso_rect = autre_perso.get_rect()
autre_perso_rect.topleft = (100, 100)

# Charge le son de collision
collision_sound = pygame.mixer.Sound("./assets/audio/TheHowieScream.mp3")  # Utilisez le fichier WAV

fenetre.blit(background,(0,0))
pygame.display.flip()

clock = pygame.time.Clock()

# Définit la vitesse de déplacement de l'autre personnage
autre_perso_speed = 3

# Game loop
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
            elif event.key == pygame.K_d: # Déplacement à droite
                if perso_rect.left < 500:
                    perso_rect = perso_rect.move(25, 0)
                else:
                    collision_sound.play()  # Joue le son si collision avec le mur de droite
            elif event.key == pygame.K_q: # Déplacement à gauche
                if perso_rect.left > 0:
                    perso_rect = perso_rect.move(-25, 0)
                else:
                    collision_sound.play()  # Joue le son si collision avec le mur de gauche
            elif event.key == pygame.K_s: # Déplacement vers le bas
                if perso_rect.top < 380:
                    perso_rect = perso_rect.move(0, 25)
                else:
                    collision_sound.play()  # Joue le son si collision avec le mur du bas
            elif event.key == pygame.K_z: # Déplacement vers le haut
                if perso_rect.top > 0:
                    perso_rect = perso_rect.move(0, -25)
                else:
                    collision_sound.play()  # Joue le son si collision avec le mur du haut

    # Déplacement automatique de l'autre personnage
    direction = random.choice(['left', 'right', 'up', 'down'])
    if direction == 'left':
        if autre_perso_rect.left > 0:
            autre_perso_rect = autre_perso_rect.move(-autre_perso_speed, 0)
    elif direction == 'right':
        if autre_perso_rect.right < 640:
            autre_perso_rect = autre_perso_rect.move(autre_perso_speed, 0)
    elif direction == 'up':
        if autre_perso_rect.top > 0:
            autre_perso_rect = autre_perso_rect.move(0, -autre_perso_speed)
    elif direction == 'down':
        if autre_perso_rect.bottom < 480:
            autre_perso_rect = autre_perso_rect.move(0, autre_perso_speed)

    # Vérification de collision avec le mur pour l'autre personnage
    if autre_perso_rect.colliderect(perso_rect):
        collision_sound.play()

 # Vérification de collision entre les deux personnages
    if perso_rect.colliderect(autre_perso_rect):
        # Si collision détectée, remplacer le deuxième personnage par son deuxième apparence
        autre_perso = autre_perso2
        # Si collision détectée, déplacer l'autre personnage hors de l'écran
        autre_perso_rect.topleft = (-1000, -1000)
        
# Affiche l'explosion à la position de la collision
        fenetre.blit(explosion_image, perso_rect.topleft)
        fenetre.blit(explosion_image, autre_perso_rect.topleft)
        pygame.display.flip()
        pygame.time.delay(1000)  # Pause pour montrer l'explosion
        # Replacer les personnages à leur position initiale
        perso_rect.topleft = (320, 240)
        autre_perso_rect.topleft = (100, 100)
         # Obtenez le point de collision entre les deux rectangles
    explosion_pos = perso_rect.clip(autre_perso_rect).topleft
    # Affiche l'explosion à la position de la collision
    fenetre.blit(explosion_image, explosion_pos)

    fenetre.blit(background, (0, 0))
    fenetre.blit(perso, perso_rect)
    fenetre.blit(autre_perso, autre_perso_rect)
    pygame.display.flip()

    clock.tick(30)  # Limite le framerate à 30 FPS

pygame.quit()
sys.exit()