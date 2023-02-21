class Salario_mensal:

    def __init__(self, hora_trabalho, qtd_dias_uteis) -> None:
        self.hora_trabalho = float(hora_trabalho)
        self.qtd_dias_uteis = qtd_dias_uteis
        self.hora_dia = 8

    def salario_mensal_funcionario(self):
        valor_salario = self.hora_trabalho * int(self.qtd_horas_mes())
        return valor_salario

    def qtd_horas_mes(self):
        horas_mes = self.qtd_dias_uteis * self.hora_dia
        return horas_mes

    def imprime_horas_mes(self):
        print('A quantidade de horas trabalhadas no mês de referência:' f'\033[1m {self.qtd_horas_mes()} hrs \033[0m')
        print()

    def imprime_salario_mensal(self):
        print('O seu salário no mês de referência: R$' f'\033[1m {self.salario_mensal_funcionario():.2f} \033[0m')
        print()
