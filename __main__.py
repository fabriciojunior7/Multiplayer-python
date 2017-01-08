import pygame, sys
import players

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

def main():
    pygame.init()
    largura = 900
    altura = 700
    tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
    pygame.display.set_caption("Para Casais S2")
    relogio = pygame.time.Clock()
    frames = 60

    #Superficie do Jogo
    jogo = pygame.Surface((largura, altura))

    player1 = players.Player()

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()


        #Rodar
        pygame.display.update()
        relogio.tick(frames)
        #Pintar
        tela.fill(vermelho)
        jogo.fill(branco)
        tela.blit(jogo, (0, 0))
        player1.pintar(jogo)









main()