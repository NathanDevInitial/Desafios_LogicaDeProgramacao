rankingHero = "null Ranking"
xpHero = 1

while xpHero < 10001: 
    xpHero += 1000

    if xpHero <= 1000:
        rankingHero = "Seu Heroi ainda precisa de xp para receber um ranking!"
    elif xpHero >= 1001 and xpHero < 2001 :
        rankingHero = "Seu Herói é nivel Ferro, não pare por aqui continue evoluindo!"
    elif xpHero >= 2001 and xpHero < 5000:
        rankingHero = "Seu Herói é nivel Bronze. Não pare por aqui continue evoluindo!"     
    elif xpHero >= 5000 and xpHero < 6000:
        rankingHero = "Seu Herói é nivel Prata. Não pare por aqui continue evoluindo!"
    elif xpHero >= 6000 and xpHero < 7001:
        rankingHero = "seu Herói é nivel Ouro. Não Pare por aqui continue evoluindo!"
    elif xpHero >= 7001 and xpHero < 8001:
        rankingHero = "Seu herói é nivel Platina."
    elif xpHero >= 8001 and xpHero < 9001:
        rankingHero = "Seu herói é nivel Ascendente."
    elif xpHero >= 9000 and xpHero < 10000:
        rankingHero = "Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços!"
        xpHero -= 900
    elif xpHero >= 10000:
        rankingHero = "Parabéns por chegar até aqui, o seu herói agora é ranking Radiante. Você chegou ao nível máximo !!! "

    print(f"O seu Herói é nivel: {rankingHero} e a quantidade de xp que ele tem é: {xpHero} " )




    