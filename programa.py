from funcoes import *

frota = {}

embarcacoes = [
    ["porta-aviões", 4, 1],
    ["navio-tanque", 3, 2],
    ["contratorpedeiro", 2, 3],
    ["submarino", 1, 4]
]

for nome, tamanho, quantidade in embarcacoes:
    for i in range(quantidade):
        valida = False

        while not valida:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            orientacao = "vertical"

            if tamanho > 1:
                escolha = int(input("[1] Vertical [2] Horizontal >"))

                if escolha == 2:
                    orientacao = "horizontal"

            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)

            if valida:
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    jogada_valida = False

    while not jogada_valida:
        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if tabuleiro_oponente[linha][coluna] == "X" or tabuleiro_oponente[linha][coluna] == "-":
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            jogada_valida = True

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

