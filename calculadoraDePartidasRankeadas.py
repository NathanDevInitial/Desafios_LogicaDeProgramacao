import random



#--->Forma comum com entrada de dados do usuário.
def calculoDeRankeadas(vitorias, derrotas):
    mediaRankeadas = vitorias - derrotas

    

    if vitorias < 10:
        ranking = "Ferro"
    elif 10 <= vitorias <= 20:
        ranking = "Bronze"
    elif 21 <= vitorias <= 50:
        ranking = "Prata"
    elif 51 <= vitorias <= 80:
        ranking = "Ouro"
    elif 81 <= vitorias <= 90:
        ranking = "Diamante"
    elif 91 <= vitorias <= 100:
        ranking = "Lendário"
    else:
        ranking = "Imortal"

    if mediaRankeadas < 0:
        mediaRankeadas = 0

    if mediaRankeadas == 0:
        ranking = f"Jogador {ranking} com média de Ranking insuficiente!"

    return ranking, mediaRankeadas


vitorias = int(input("Digite o número de vitórias>>> "))
derrotas = int(input("Digite o número de derrotas>>> "))

ranking, partidas = calculoDeRankeadas(vitorias, derrotas)

print(f"O Herói tem de saldo de **{vitorias}** está no nível de **{ranking}**")

#---------------------------------------------------------------------------------------------------------------------------------***

#--->Desenvolvendo o mesmo código mas com a utilização do modulo radom pertencente a documentação do Python

def calculadoraDeRankingJogadorAutomatica(vitorias2, derrotas2):
    
    mediaDaRanked2 = vitorias2 - derrotas2

    if mediaDaRanked2 < 0:
        mediaDaRanked2 = 0

    if vitorias2 < 10:
        ranking2 = "Ferro"
    elif 11 <= vitorias2 <= 20:
        ranking2 = "Bronze"
    elif 21 <= vitorias2 <= 50:
        ranking2 = "Prata"
    elif 51 <= vitorias2 <= 80:
        ranking2 = "Ouro"
    elif 81 <= vitorias2 <= 90:
        ranking2 = "Diamante"
    elif 91 <= vitorias2 <= 100:
        ranking2 = "Lendário"
    else:
        ranking2 = "Imortal" 

    return ranking2, mediaDaRanked2


# Utilização direta do modulo: Random

vitorias2 = random.randint(0, 200)
derrotas2 = random.randint(0, 200)

ranking2, partidas2 = calculadoraDeRankingJogadorAutomatica(vitorias2, derrotas2)

print(f"O Herói tem de saldo de **{vitorias2}** está no nível de **{ranking2}**")