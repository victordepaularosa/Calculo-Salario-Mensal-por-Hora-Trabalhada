from menu import *
from dias_uteis import *
from salario_mensal import *

# Função para limpar tela
limpar_tela()

# Menu Inicial
menu = Menu()
menu.menu_inicial()
# Informações inseridas pelo Usuário
mes = menu.mes_referencia()
ano = menu.ano_referencia()
estado = menu.estado_referencia()
hora_trabalho = menu.hora_trabalho_referencia()

# Geração do calendário do funcionário
calendario = Calendario_Br(mes, ano, estado)

# Função para limpar tela
limpar_tela()

# Cálculo das horas trabalhadas pelo funcionário no mês
funcionario = Salario_Mensal(hora_trabalho, len(calendario))

# Imprimir as Informações úteis para o usuário
menu.menu_inicial()
calendario.imprime_dias_uteis_mes()
funcionario.imprime_horas_mes()
funcionario.imprime_salario_mensal()
