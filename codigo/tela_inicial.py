from constantes import *
import motor_grafico as motor

def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, PRETO)
    if estado['opcao_menu'] == 0:
        motor.desenha_string(janela,largura//2-len('JOGAR')-6, altura//2,'==>', PRETO, BRANCO)
    else:
        motor.desenha_string(janela,largura//2-len('JOGAR')-6, altura//2+1,'==>', PRETO, BRANCO)
    motor.desenha_string(janela,0, 1, '-'*largura, PRETO, BRANCO)
    motor.desenha_string(janela,0, altura-2, '-'*largura, PRETO, BRANCO)
    motor.desenha_string(janela,largura//20,altura//8,'Ω',PRETO,BRANCO)
    motor.desenha_string(janela,largura//6,altura//6,'♛',PRETO,BRANCO)
    motor.desenha_string(janela,largura//3,altura//9,'♥',PRETO,BRANCO)
    motor.desenha_string(janela,largura//2,altura//7,'▲',PRETO,BRANCO)
    motor.desenha_string(janela,largura*2//3,altura//8,'★',PRETO,BRANCO)
    motor.desenha_string(janela,largura*5//6,altura//6,'☠',PRETO,BRANCO)
    motor.desenha_string(janela,largura*19//20,altura//9,'Ψ',PRETO,BRANCO)
    motor.desenha_string(janela,largura//12,altura//3,'◈',PRETO,BRANCO)
    motor.desenha_string(janela,largura//4,altura//3,'♞',PRETO,BRANCO)
    motor.desenha_string(janela,largura*3//4,altura//3,'§',PRETO,BRANCO)
    motor.desenha_string(janela,largura*11//12,altura//3,'$',PRETO,BRANCO)
    motor.desenha_string(janela,largura//15,altura//2,'Ψ',PRETO,BRANCO)
    motor.desenha_string(janela,largura//5,altura//2,'#',PRETO,BRANCO)
    motor.desenha_string(janela,largura*4//5,altura//2,'@',PRETO,BRANCO)
    motor.desenha_string(janela,largura*14//15,altura//2,'▲',PRETO,BRANCO)
    motor.desenha_string(janela,largura//10,altura*2//3,'♦',PRETO,BRANCO)
    motor.desenha_string(janela,largura//3,altura*2//3,'†',PRETO,BRANCO)
    motor.desenha_string(janela,largura*2//3,altura*2//3,'¤',PRETO,BRANCO)
    motor.desenha_string(janela,largura*9//10,altura*2//3,'Ω',PRETO,BRANCO)
    motor.desenha_string(janela,largura//20,altura*5//6,'☠',PRETO,BRANCO)
    motor.desenha_string(janela,largura//4,altura*4//5,'★',PRETO,BRANCO)
    motor.desenha_string(janela,largura//2,altura*5//6,'♥',PRETO,BRANCO)
    motor.desenha_string(janela,largura*3//4,altura*4//5,'♛',PRETO,BRANCO)
    motor.desenha_string(janela,largura*19//20,altura*5//6,'◈',PRETO,BRANCO)
    motor.desenha_string(janela, largura//2-len('JOGAR')-2, altura//2, 'JOGAR', PRETO, BRANCO)
    motor.desenha_string(janela, largura//2-len('INSTRUCOES')+3, altura//2+1, 'INSTRUÇÕES', PRETO, BRANCO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada =='BAIXO':
        estado['opcao_menu'] = 1
    if tecla_apertada =='CIMA':
        estado['opcao_menu'] = 0
    if tecla_apertada == 'ESPACO' and estado['opcao_menu'] == 0:
        estado['tela_atual'] = TELA_JOGO
    if tecla_apertada == 'ESPACO' and estado['opcao_menu'] == 1:
        estado['tela_atual'] = INSTRUCOES
    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR
