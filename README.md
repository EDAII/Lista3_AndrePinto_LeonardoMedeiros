# Aplicação de algoritmos de ordenação nLog(n)

3º Exercício Prático - Estrutura de Dados 2 - 2019.1 - UnB - Gama
=========================
André Lucas de Sousa Pinto - 17/0068251
Leonardo de Araujo Medeiros - 17/0038891

## Instalação

1. Faça o clone deste projeto com ```$ git clone https://github.com/EDAII/Lista3_AndrePinto_LeonardoMedeiros.git ```
2. Acesse a pasta do projeto via terminal
3. Execute a aplicação com ``` $ python3 main.py``` 
> OBS: Necessário instalar o [matplotlib](https://matplotlib.org/index.html).

## Ideia proposta
Dado o dataset das mensagens gravadas por jogadores do jogo Dark Souls coletados entre 2018-03-05 e 2018-03-08 do tráfego de rede pública gerado pelos clientes do jogo, nos propomos a ordena-las para possibilitar uma busca mais eficiente nas mensagens, que poderiam então ser encontradas em ` log (n)` , além disto, analisar qual seria o melhor algoritmo a se aplicar num dataset como este, onde uma das chaves de ordenação, o numero de mundos, se repetia constantemente.

## Resultado
Como resultado final podemos avaliar que, neste dataset, dada a distribuição da chave de busca escolhida, o número do mundo, com muitas repetições, o Merge sort apresentou desempenho melhor que o Quick sort, principalmente pelo fato de ser um algoritmo estável, fazendo menos atribuições.
```
Foram lidos: 53305 Blood Messages
O Merge sort, algoritmo estavel, demorou 2.064948797225952 segundos, tendo feito 840649 atribuicoes e o Quick sort, instavel, demorou 2.509984016418457 segundos, tendo feito 1055490 atribuicoes
```

Também é possivel, separando as mensagens pelo mundo em que estão, montar um gráfico que da uma noção do mapa do jogo, apenas usando as posições das mensagens deixadas pelos jogadores, como por exemplo estes:
![mapa14](https://github.com/EDAII/Lista3_AndrePinto_LeonardoMedeiros/blob/master/map14.png)
![mapa15](https://github.com/EDAII/Lista3_AndrePinto_LeonardoMedeiros/blob/master/map15.png)
