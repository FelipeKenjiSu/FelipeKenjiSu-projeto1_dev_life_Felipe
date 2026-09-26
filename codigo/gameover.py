from constantes import *
import motor_grafico as motor

def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, PRETO)
    motor.desenha_string(janela,0, 1, '-'*largura, PRETO, BRANCO)
    motor.desenha_string(janela,0, altura-2, '-'*largura, PRETO, BRANCO)
    motor.desenha_string(janela,largura//2-8, altura//2, 'GAME OVER!!!', PRETO, BRANCO)
    motor.desenha_string(janela,0, 4, '[Aperte ESQ para voltar ao menu!]', PRETO, BRANCO)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada =='ESCAPE':
        estado['tela_atual'] = TELA_INICIO

    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR
