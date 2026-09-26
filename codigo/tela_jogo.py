from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto
from inicializacao import gera_posicao_desocupada
import random
def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão.
    # Por exemplo, para saber a posição do jogador, use estado['pos_jogador']
    # O mapa esta armazenado em estado['mapa'].
    motor.preenche_fundo(janela,PRETO)
    mapa = estado['mapa']
    inicial_y = altura_tela//2 - len(mapa)//2
    inicial_x = largura_tela//2 - len(mapa[0])//2
    mapa_cords = []
    # O seu código deve desenhar a tela do jogo aqui a partir dos valores no dicionário "estado"
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            motor.desenha_string(janela,x+inicial_x,y+inicial_y,mapa[y][x],VERDE_ESCURO,ROXO)
    # def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    objetos = estado['objetos']
    posicoes_ocupadas = []
    pos_jog = estado['pos_jogador']
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
    motor.desenha_string(janela,largura_tela-len(f'Nivel: {estado['nivel']} EXP:{estado['exp']}/10'),0,f'Nivel: {estado['nivel']} EXP:{estado['exp']}/10',PRETO,ROXO)


    # desenha_string(janela, x, y, string, cor_fundo, cor_texto)
    motor.mostra_janela(janela)
    

def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1
    motor.desenha_string
    estado['mensagem'] = ''
    anterior = estado['pos_jogador']
    objetos = estado['objetos']
    cords = [anterior[0],anterior[1]]
    direcoes = ["CIMA", "BAIXO", "ESQUERDA", "DIREITA"]
    direcao_sorteada = random.choice(direcoes)
    if tecla == 'ESQUERDA' and estado['pos_jogador'][0]>0 :
        estado['pos_jogador'][0] -=1
    if tecla == 'DIREITA' and estado['pos_jogador'][0]<49:
        estado['pos_jogador'][0] +=1
    if tecla == 'CIMA' and estado['pos_jogador'][1]>0:
        estado['pos_jogador'][1] -=1
    if tecla == 'BAIXO' and estado['pos_jogador'][1]<14:
        estado['pos_jogador'][1] +=1
    print(estado['pos_jogador'])
    if estado['pos_jogador'] == [26,13] and estado['esta_na_sala'] == False:
        estado['mapa_normal'] = estado['mapa']
        estado['objetos_normais'] = estado['objetos']
        secret_room = open('secret_room.txt', 'r', encoding='utf-8')
        linhas_secretas = secret_room.readlines()
        secret_room.close()
        secret_room = []
        for linha in linhas_secretas:
            secret_room.append(list(linha.rstrip('\n'))) #list  faz algo do tipo['a','b','c'] por isso conseguimos acessar x e y do mapa
        parede = []
        for y in range(len(secret_room)):
            for x in range(len(secret_room[y])):
                if secret_room[y][x] == "#":
                    parede.append([x, y])
        estado['mapa'] = secret_room
        estado['pos_jogador'] = [4, 2]
        estado['objetos'] = []
        for ordenado in parede:
            estado['objetos'].append({
                        'tipo': '█',
                        'posicao': ordenado,
                        'cor': MARROM_MAIS_ESCURO,
                    })
        estado['esta_na_sala'] = True
    if estado['pos_jogador'] == [4,12] and estado['esta_na_sala'] == True:
        estado['mapa'] = estado['mapa_normal']
        estado['objetos'] = estado['objetos_normais']
        estado['pos_jogador'] = [25,13]
        estado['esta_na_sala'] = False
        
    for objeto in objetos:
        anterior_monstro = objeto['posicao']
        cord_monstro = [anterior_monstro[0],anterior_monstro[1]]
        if direcao_sorteada == 'ESQUERDA' and objeto['posicao'][0]>0 and objeto['tipo'] == 'Ω' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][0] -=1
        if direcao_sorteada == 'DIREITA' and objeto['posicao'][0]<49 and objeto['tipo'] == 'Ω' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][0] +=1
        if direcao_sorteada == 'CIMA' and objeto['posicao'][1]>0 and objeto['tipo'] == 'Ω' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][1] -=1
        if direcao_sorteada == 'BAIXO' and objeto['posicao'][1]<14 and objeto['tipo'] == 'Ω' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][1] +=1
        if direcao_sorteada == 'ESQUERDA' and objeto['posicao'][0]>0 and objeto['tipo'] == 'º' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][0] -=1
        if direcao_sorteada == 'DIREITA' and objeto['posicao'][0]<49 and objeto['tipo'] == 'º' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][0] +=1
        if direcao_sorteada == 'CIMA' and objeto['posicao'][1]>0 and objeto['tipo'] == '*' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][1] -=1
        if direcao_sorteada == 'BAIXO' and objeto['posicao'][1]<14 and objeto['tipo'] == '*' and estado['pos_jogador'] != objeto['posicao']:
            objeto['posicao'][1] +=1
        for obj in objetos:
            if objeto['posicao'] == obj['posicao'] and obj['tipo'] == '█':
                objeto['posicao'] = cord_monstro
            
        if estado['pos_jogador'] == objeto['posicao'] and objeto['tipo'] == 'Ω':
            estado['pos_jogador'] = cords
            estado['mensagem'] = 'MONSTROOOOOO!!!!'
            numero = random.random()
            if numero>objeto['probabilidade de ataque']:
                objeto['vidas'] -=1
                estado['mensagem'] = f'Você conseguiu um ataque! Vida restante:{objeto['vidas']}'
            else:
                estado['vidas'] -=1
                estado['mensagem'] = 'voce foi ferido!'
            if objeto['vidas'] == 0:
                objeto['tipo'] = ''
                estado['mensagem'] = 'O monstro foi morto!'
                estado['exp'] +=4
                estado['pos_jogador'] = objeto['posicao']
            if estado['vidas'] == 0:
                estado['tela_atual'] = GAME_OVER
        if estado['pos_jogador'] == objeto['posicao'] and objeto['tipo'] == '*':
            estado['pos_jogador'] = cords
            estado['mensagem'] = 'MONSTROOOOOO!!!!'
            numero = random.random()
            if numero>objeto['probabilidade de ataque']:
                objeto['vidas'] -=1
                estado['mensagem'] = f'Você conseguiu um ataque! Vida restante:{objeto['vidas']}'
            else:
                estado['vidas'] -=1
                estado['mensagem'] = 'voce foi ferido!'
            if objeto['vidas'] == 0:
                objeto['tipo'] = ''
                estado['mensagem'] = 'O monstro foi morto!'
                estado['exp'] +=6
                estado['pos_jogador'] = objeto['posicao']
            if estado['vidas'] == 0:
                estado['tela_atual'] = GAME_OVER
        if estado['pos_jogador'] == objeto['posicao'] and objeto['tipo'] == 'º':
            estado['pos_jogador'] = cords
            estado['mensagem'] = 'MONSTROOOOOO!!!!'
            numero = random.random()
            if numero>objeto['probabilidade de ataque']:
                objeto['vidas'] -=1
                estado['mensagem'] = f'Você conseguiu um ataque! Vida restante:{objeto['vidas']}'
            else:
                estado['vidas'] -=1
                estado['mensagem'] = 'voce foi ferido!'
            if objeto['vidas'] == 0:
                objeto['tipo'] = ''
                estado['mensagem'] = 'O monstro foi morto!'
                estado['exp'] +=12
                estado['pos_jogador'] = objeto['posicao']
            if estado['vidas'] == 0:
                estado['tela_atual'] = GAME_OVER
                    
                




        if estado['pos_jogador'] == objeto['posicao'] and objeto['tipo'] == CORACAO:
                estado['mensagem'] = 'Você pegou um coração!'
                objeto['tipo'] = ''
                if estado['vidas']<estado['max_vidas']:
                    estado['vidas'] +=1
        if estado['pos_jogador'] == objeto['posicao'] and objeto['tipo'] == ESPINHO:
            estado['mensagem']= 'Voce pisou em um espinho!'
            if estado['vidas']>1:
                estado['vidas'] -=1
            else:
                estado['tela_atual'] = GAME_OVER
        if estado['pos_jogador'] == objeto['posicao'] and objeto['tipo'] == '█':
            estado['pos_jogador'] = cords
            estado['mensagem'] = 'Você colidiu com uma parede!'
    forca=estado['vidas']
    if estado['exp']>=10:
        resto = estado['exp']%10
        estado['exp'] = resto
        estado['nivel'] +=1
        estado['mensagem'] = 'Você subiu de nível!!! GANHOU 1 CORAÇÃO'
        estado['vidas'] += 1
        estado['max_vidas'] +=1
    


    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    # APAGUE ESTA LINHA E ESCREVA SEU CÓDIGO AQUI

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR