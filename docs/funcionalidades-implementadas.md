# Funcionalidades Implementadas

As seguintes funcionalidades do projeto foram implementadas:

Coloque aqui o link para o vídeo, de no máximo 2 minutos, do jogo: [LINK VÍDEO](https://linkparaovideo.com)

### [Nível Básico](basico.md)

No nível básico você deve entender o código fornecido e implementar as seguintes funcionalidades (marque com `x` as que já tiver concluido - nós utilizaremos este checklist para corrigir seu projeto):

- [x] Configurar o Git e o GitHub (já deixamos esta primeira tarefa marcada como feita);
- [X] Implementar a função `gera_posicao_desocupada`;
    - [X] Devolver uma posição aleatória dentro do mapa;
    - [X] Adicionar a posição à lista de posições ocupadas.
- [X] Implementar a função `desenha_tela`:
    - [X] Mostrar mapa;
    - [X] Mostrar jogador;
    - [X] Mostrar objetos;
    - [X] Mostrar quantidade de vidas (se o jogador tiver menos vidas do que o máximo, o restante deve ser mostrado como corações brancos - exemplo: 🧡🧡🧡🤍🤍);
    - [X] Mostrar mensagem.
- [X] Implementar a função `atualiza_estado`:
    - [X] Mover o jogador;
    - [X] Impedir o jogador de sair do mapa;
    - [X] Ao colidir com um coração:
        - [X] Remover o coração da lista de objetos;
        - [X] Aumentar uma vida caso ainda não esteja no máximo;
        - [X] Não aumentar caso contrário;
        - [X] Adicionar uma mensagem indicando o que aconteceu.
    - [X] Ao colidir com um espinho:
        - [X] Diminuir uma vida;
        - [X] Terminar o jogo caso tenha atingido zero vidas (mudar `estado['tela_atual']`).

### [Nível Proficiente](proficiente.md)

- [X] Adiciona paredes na inicialização (ainda sem colisão);
- [X] Adiciona colisão com as paredes:
    - [X] Impede o movimento do jogador:
    - [X] Mostra mensagem na tela.
- [X] Adiciona monstros:
    - [X] Sorteia posições aleatórias para os monstros;
    - [X] Adiciona `'vida'` e `'probabilidade_de_ataque'` aos monstros;
    - [X] Mostra monstros na tela.
- [X] Implementa sistema de batalha:
    - [X] Verifica se a nova posição do jogador está ocupada por um monstro e impede o movimento;
    - [X] Sorteia um número aleatório;
    - [X] Verifica quem ataca quem e diminui as vidas do alvo;
    - [X] Se o jogador morrer, acaba o jogo;
    - [X] Se o monstro morrer, o monstro é removido da lista e o jogador avança para a posição do monstro;
    - [X] Mostra mensagem na tela.
- [X] Implementa movimentação aleatória dos monstros:
    - [x] Sorteia um movimento para cada monstro e tenta andar naquela direção;
    - [X] Atualiza a posição se for uma posição válida (dentro do mapa e desocupada).

### [Nível Avançado](avancado.md)

- [ ] Funcionalidade 1: Personagem centralizado na tela e mapa maior do que a janela;
- [X] Funcionalidade 2: Diferentes tipos de inimigos;
- [ ] Funcionalidade 3: Chefão;
- [ ] Funcionalidade 4: Sala secreta;
- [ ] Funcionalidade 5: Sistema de experiência e níveis;
- [ ] Funcionalidade 6: Itens e inventário;
- [ ] Funcionalidade 7: Equipamento e limite de mochila;
- [ ] Funcionalidade 8: Mapa em arquivo;
- [ ] Funcionalidade 9: Monstro cobrinha;
- [ ] Funcionalidade 10: Telas adicionais;
- [ ] Funcionalidade 11: [Sua sugestão validada por um professor - INDIQUE AQUI O NOME DO PROFESSOR QUE VALIDOU SUA IDEIA].
