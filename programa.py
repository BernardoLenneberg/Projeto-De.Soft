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

print(frota)