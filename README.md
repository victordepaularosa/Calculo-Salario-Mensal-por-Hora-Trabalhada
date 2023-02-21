# Cálculo Salario Mensal por Hora Trabalhada

> Status do Projeto: Finalizado com possibilidade de atualização

Este Projeto foi criado utilizano a linguagem Python, tendo o intuito de utilizando a orientação a objeto para melhor compreensão dos seus métodos e com a possibilidade de evolução deste código.

### Objetivo

Criação de um código na linguagem Python para realizar o cálculo de quanto será o salário de um funcionário que trabalha no regime de horas trabalhadas por mês.


### Premissas do Projeto

Primeiramente é necessário realizar a instalação das seguintes bibliotecas do Python:

```
pip install DateTime
pip install workadays
```

Sendo criadas 03 (três) classes para o desenvolvimento do presente projeto, sendo estas:
 
* Menu
* Salario_mensal
* Calendario_Br

Além disso, foi utilizada a biblioteca os para criação da função de limpeza de tela, conforme apresentado a seguir:

```
from os import system

def limpar_tela():
    return system('cls')
```

A imagem a seguir apresenta a página inicial do projeto, a qual são dadas as informações pelo usuário, referente ao mês e ano que deseja saber quanto será o seu salário, bem como também é necessário indicar qual é o estado ao qual este funcionário reside para também ser validado se este estado possui algum feriado no mês de referência.

![Página Inicial](https://user-images.githubusercontent.com/115742655/220452942-f7ff9b3c-d656-4d30-98b0-acb176384d50.png)

A imagem abaixo apresenta o retorno das informações prestadas pelo usuário, assim dando como retorno quantos dias serão trabalhados no mês, quantidade de horas, além da informação principal de qual será o seu salário.

![Página Final](https://user-images.githubusercontent.com/115742655/220453099-d1151dad-66df-4c0d-8910-a0be1c1b4d4c.png)

