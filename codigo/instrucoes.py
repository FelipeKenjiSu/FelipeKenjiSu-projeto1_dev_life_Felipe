from constantes import *
import motor_grafico as motor

def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, PRETO)
    motor.desenha_string(janela,0, 1, '-'*largura, PRETO, BRANCO)
    motor.desenha_string(janela,largura//2-len('instrucoes')+4, 1, 'INSTRUÇÕES', PRETO, BRANCO)
    motor.desenha_string(janela,0, altura-2, '-'*largura, PRETO, BRANCO)
    motor.desenha_string(janela,0,3,'OBJETIVO:Explore o mapa, derrote os monstros e sobreviva!', PRETO, BRANCO)
    motor.desenha_string(janela,0,6,'CONTROLES:', PRETO, BRANCO)
    motor.desenha_string(janela,0,7,'↑ ↓ ← →  - Mover personagem', PRETO, BRANCO)
    motor.desenha_string(janela,0,8,'I          - Abrir inventário', PRETO, BRANCO)
    motor.desenha_string(janela,0,9,'Q / ESC    - Sair do jogo', PRETO, BRANCO)
    motor.desenha_string(janela,0,11,'COMBATE:', PRETO, BRANCO)
    motor.desenha_string(janela,0,12,'Encoste nos monstros para enfrentá-los.', PRETO, BRANCO)
    motor.desenha_string(janela,0,13,'Cada monstro possui força e vidas diferentes.', PRETO, BRANCO)
    motor.desenha_string(janela,0,15,'ITENS:', PRETO, BRANCO)
    motor.desenha_string(janela,0,16,'♥  - Recupera vida', PRETO, BRANCO)
    motor.desenha_string(janela,0,17,'#  - Espinho: causa dano', PRETO, BRANCO)
    motor.desenha_string(janela,0,19,'PROGRESSÃO:', PRETO, BRANCO)
    motor.desenha_string(janela,0,20,'Derrote monstros para ganhar EXP.', PRETO, BRANCO)
    motor.desenha_string(janela,0,21,'Ao conseguir EXP suficiente, você sobe de nível', PRETO, BRANCO)
    motor.desenha_string(janela,0,22,'e aumenta sua vida máxima.', PRETO, BRANCO)
    motor.desenha_string(janela,0,24,'Boa sorte!!!', PRETO, BRANCO)

def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada =='ESCAPE':
        estado['tela_atual'] = TELA_INICIO
    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR
