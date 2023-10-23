 <h1>Desafio01 de Lógica de Programação - Progressão de Herói</h1>
 
<div>
 <p>Este é um desafio de lógica de programação que simula o progresso de um herói em um jogo, onde o herói ganha pontos de experiência (xp) e avança por diferentes rankings.
   O objetivo é criar um programa que acompanha o progresso do herói e exibe mensagens de classificação correspondentes de acordo com a quantidade de xp acumulada.
   O desafio envolve a exibição de cada classificação apenas uma vez e a redução da xp necessária para atingir o próximo ranking quando o herói atinge o ranking "Imortal".</p>
 <h3>Linguagem utilizada: Python</h3>
</div>

<div>
<h3>Funcionalidades:</h3>

>  Inicialização das variáveis xpHero e rankingHero.<br/>
>  Um loop que incrementa a xpHero em 1000 unidades a cada iteração.<br/>
>  Condicionais para determinar o ranking atual do herói com base na quantidade de xpHero.<br/>
>  Utilização da variável rankingHero para mostrar mensagens de classificação apropriadas.<br/>
>  Redução da xpHero em 900 unidades quando o herói atinge o ranking "Imortal" para ajustar a progressão.<br/>
</div>

<div>
<h3>Exemplo de Uso:</h3>
```

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

<h3>Resultado Esperado:</h3>

    seu Herói é nivel: Seu Herói é nivel Ferro, não pare por aqui continue evoluindo! e a quantidade de xp que ele tem é: 1001 
    O seu Herói é nivel: Seu Herói é nivel Bronze. Não pare por aqui continue evoluindo! e a quantidade de xp que ele tem é: 2001
    O seu Herói é nivel: Seu Herói é nivel Bronze. Não pare por aqui continue evoluindo! e a quantidade de xp que ele tem é: 3001
    O seu Herói é nivel: Seu Herói é nivel Bronze. Não pare por aqui continue evoluindo! e a quantidade de xp que ele tem é: 4001
    O seu Herói é nivel: Seu Herói é nivel Prata. Não pare por aqui continue evoluindo! e a quantidade de xp que ele tem é: 5001
    O seu Herói é nivel: seu Herói é nivel Ouro. Não Pare por aqui continue evoluindo! e a quantidade de xp que ele tem é: 6001
    O seu Herói é nivel: Seu herói é nivel Platina. e a quantidade de xp que ele tem é: 7001
    O seu Herói é nivel: Seu herói é nivel Ascendente. e a quantidade de xp que ele tem é: 8001
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8101
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8201
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8301
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8401
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8501
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8601
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8701
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8801
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 8901
    O seu Herói é nivel: Seu herói já pertence ao ranking Imortal. Para o proximo ranking você precisará de mais esforços! e a quantidade de xp que ele tem é: 9001
    O seu Herói é nivel: Parabéns por chegar até aqui, o seu herói agora é ranking Radiante. Você chegou ao nível máximo !!!  e a quantidade de xp que ele tem é: 10001

</div>


<div>
<h1>Desafio02 de Lógica de Programação - Calculadora para Rankeadas (Entrada do Usuário)</h1>

Este código em Python permite que o usuário insira a quantidade de vitórias e derrotas de um jogador para calcular seu título e saldo de Rankeadas. Ele oferece uma maneira interativa de avaliar o desempenho do jogador.


<h3>Exemplo de Uso</h3>

<h4>Suponhamos que um jogador tenha 30 vitórias e 15 derrotas:</h4>
  
```
  Digite o número de vitórias: 30
  Digite o número de derrotas: 15
````
<h4>A saida será:</h4>

```
  O jogador tem o ranking de Bronze com um saldo de Rankeadas de 15 vitórias.
````
<h3>Funcionalidades</h3>

1.  Solicita que o usuário insira a quantidade de vitórias e derrotas do jogador.<br>
2.  Com base nas entradas do usuário, determina o título do jogador (como "Ferro", "Bronze", "Prata", "Ouro", etc.) com base em critérios específicos.<br>
3.  Calcula o saldo de Rankeadas (vitórias - derrotas) e garante que seja um valor não negativo, ajustando para zero se necessário.<br>
4.  Exibe o título, a quantidade de vitórias, a quantidade de derrotas e o saldo de Rankeadas.<br>


<h1>Desafio02(auto imposto) de Lógica de Programação - Calculadora para Rankeadas (Valores Gerados Automaticamente)</h1>
Este código em Python gera automaticamente valores aleatórios para a quantidade de vitórias e derrotas de um jogador e calcula seu título e saldo de Rankeadas com base nesses valores. Ele é útil para avaliar o desempenho de jogadores sem a necessidade de entrada do usuário.


<h3>Exemplo de Uso</h3>
-Exemplo de Uso:

```
O jogador tem o ranking de Prata com um saldo de Rankeadas de 10 vitórias.
```
<h3>Funcionalidades</h3>

1.  Gera valores aleatórios para a quantidade de vitórias e derrotas do jogador.
2.  Com base nos valores gerados, determina o título do jogador (como "Ferro", "Bronze", "Prata", "Ouro", etc.) com base em critérios específicos.
3.  Calcula o saldo de Rankeadas (vitórias - derrotas) e garante que seja um valor não negativo, ajustando para zero se necessário.
4.  Exibe o título, a quantidade de vitórias, a quantidade de derrotas e o saldo de Rankeadas.

<h3>Uso</h3>

*  Os usuários podem executar o código para avaliar o desempenho de jogadores em um jogo, gerando automaticamente valores para vitórias e derrotas.

</div>
