from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto
from inicializacao import gera_posicao_desocupada

def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão.
    # Por exemplo, para saber a posição do jogador, use estado['pos_jogador']
    # O mapa esta armazenado em estado['mapa'].
    motor.preenche_fundo(janela, PRETO)
    mapa = estado['mapa']
    inicial_y = altura_tela//2 - len(mapa)//2
    inicial_x = largura_tela//2 - len(mapa[0])//2
    # O seu código deve desenhar a tela do jogo aqui a partir dos valores no dicionário "estado"
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            motor.desenha_string(janela,x+inicial_x,y+inicial_y,' ',VERDE_ESCURO,ROXO)
    # def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    objetos = estado['objetos']
    posicoes_ocupadas = []
    pos_jog = gera_posicao_desocupada(posicoes_ocupadas,len(mapa[0]),len(mapa))
    motor.desenha_string(janela,pos_jog[0]+inicial_x,pos_jog[1]+inicial_y,JOGADOR,VERDE_ESCURO,AZUL)
    for objeto in objetos:
        tipo = objeto['tipo']
        posicao = objeto['posicao']
        cor = objeto['cor']
        motor.desenha_string(janela,posicao[0]+inicial_x,posicao[1]+inicial_y,tipo,VERDE_ESCURO,cor)
    vidas = estado['vidas']
    branco = estado['max_vidas']-estado['vidas']
    for elemento in range(vidas):
        motor.desenha_string(janela,0+elemento,0,CORACAO,PRETO,VERMELHO)
    for elemento2 in range(vidas,branco+vidas):
        motor.desenha_string(janela,0+elemento2,0,CORACAO,PRETO,BRANCO)
    motor.desenha_string(janela,0,altura_tela-1,estado['mensagem'],PRETO,AMARELO)


    # desenha_string(janela, x, y, string, cor_fundo, cor_texto)
    motor.mostra_janela(janela)
    

def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado['mensagem'] = ''

    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    # APAGUE ESTA LINHA E ESCREVA SEU CÓDIGO AQUI

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR