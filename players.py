import pygame

#Cores
branco = (255, 255, 255)

class Player(object):
    def __init__(self):
        self.x = 10
        self.y = 10
        self.largura = 20
        self.altura = 20
        self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def pintar(self, tela):
        pygame.draw.rect(tela, branco, self.corpo)
