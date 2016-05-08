# -*- coding:UTF-8 -*-

import pygame, sys
from player import Player
from pygame.constants import K_UP, K_DOWN, K_RIGHT, K_LEFT
from enemy import Enemy
import random
from pygame.rect import Rect

# Iniciando o módulo do pygame
pygame.init()

# Criando a tela principal com dimenções 900x600
screen = pygame.display.set_mode((900, 600), 0, 0)

# Carregando as imagens que serão usadas no jogo...
background_image = pygame.image.load("../images/background.png").convert()
player_image = pygame.image.load("../images/ship.png").convert_alpha()
asteroid_image = pygame.image.load("../images/asteroide_small.png") 

# Criando o objeto do player e iniciando o x = 450, y =300, passando a imagem
# da nave e dando 100 de vida.
player = Player(450, 300, player_image, 100)

# Lista que irá conter todos os enemigos
listEnemies = []

# Lista de posições que será utilizada para
# determinar as posições dos enemigos(asteroides)
listPositions = [(100, 100),(200, 60), (300, 50)]

# Função que inicia todos os enemigos nas posições 
# da lista acima
def initEnemies():
    for i in range(1, 10):
        temp = i % 3
        listEnemies.append(Enemy(listPositions[temp][0], listPositions[temp][1], asteroid_image, 50))

# Função que desenha todos os enemigos na tela
def drawEnemies():
    for enemy in listEnemies:
        screen.blit(enemy.getImage(), (enemy.getX(), enemy.getY()));

# Função que retorna o retângulo de um objeto passado 
# seja ele o jogador ou os asteroides
# Esse retângulo será usado para detectar a colisão
def getRect(obj):
    return Rect(obj.getX(), obj.getY(), obj.getImage().get_width(), obj.getImage().get_height())

def calcCollision():
    rectPlayer = getRect(player)
    for enemy in listEnemies:
        rectEnemy = getRect(enemy)

        # Se esse if for TRUE, logo houve a colição entre o player e algum asteroide
        # na lista
        if rectPlayer.colliderect(rectEnemy):
            # Quando um asteroide colide com o player 
            # o player perde 5 de vida e o asteroide é
            # lançado para fora da tela.
            enemy.setX(900)
            player.lossLife(5)

# Função que move os enemigos 
def moveEnemies():
    for enemy in listEnemies:
        # Caso o x do enemigo seja menor que o x da tela
        # o enemigo é lançado para o x 940, fazendo que o mesmo
        # volte para o lado direito da tela.
        if enemy.getX() <= 0:
            enemy.setX(940)
            enemy.setY(random.randint(0, 800))
        else:
            enemy.move(-0.5, 0)

initEnemies()

running = True
while running:

    for event in pygame.event.get():
        # Se o evento for QUIT o jogo é fechado
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # Pega as ultimas teclas pressionadas
    keyPressed = pygame.key.get_pressed()
    
    # Confere se a tecla pressionada 
    # foi para cima
    if keyPressed[K_UP]:
        # Caso o y do player for > 0 então ele pode se mover
        # caso contrário o jogador estará saindo da tela
        if player.getY() > 0:
            player.move(0, -1)
        
    # Confere se a tecla pressionada 
    # foi para baixo
    if keyPressed[K_DOWN]:
        # Se o Y do player mais a sua altura for maior que 600 (altura da tela)
        # O player não poderá se mover
        if (player.getY() + player.getImage().get_height() < 600):
            player.move(0, 1)
    
    if keyPressed[K_RIGHT]:
        if (player.getX() + player.getImage().get_width()) < 900:
            player.move(1, 0)
            
    if keyPressed[K_LEFT]:
        if player.getX() > 0:
            player.move(-1, 0)
    
    # Desenha o fundo do jogo
    screen.blit(background_image, (0,0));
    
    # Move todos os enemigos (asteroides)
    moveEnemies()
    
    # desenha todos os enemigos
    drawEnemies()
    
    # Verifica se o player colidiu com algum enemigo
    calcCollision()
    
    # Se o life do player for <= 0 ele morreu.
    # TODO: Fazer uma tela de GameOver
    if player.getLife() <= 0:
        print "Morreu"

    # Desenha o player em sua posição X e Y
    screen.blit(player.getImage(), (player.getX(), player.getY()));
    
    # Atualiza a tela do jogo
    pygame.display.update()