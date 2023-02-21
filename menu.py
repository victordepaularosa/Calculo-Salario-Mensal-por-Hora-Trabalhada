from os import system

class Menu:

    def menu_inicial(self):
        print('-' * 70)
        print('\033[1m SALÁRIO MENSAL POR HORA \033[0m'.center(70))
        print('-' * 70)
        print('Sistema Cálculo para Verificar o Salário no Mês de Referência'.center(70))
        print('-' * 70)
        print()
    
    def mes_referencia(self):
        self.mes = input('\033[1m Informe o número do mês de referência: \033[0m')
        return self.mes
    
    def ano_referencia(self):
        self.ano = input('\033[1m Informe o ano de referência [YYYY]: \033[0m')
        return self.ano
    
    def estado_referencia(self):
        self.estado = input('\033[1m Informe a sigla do estado de referência: \033[0m')
        return self.ano

    def hora_trabalho_referencia(self):
        self.hora_trabalho = input('\033[1m Informe o valor da sua hora por trabalho: \033[0m')
        return self.hora_trabalho



def limpar_tela():
    return system('cls')
