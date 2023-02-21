import datetime as dt
from workadays import workdays as wd

class Calendario_Br:

    def __init__(self, mes, ano, estado) -> None:
        self.mes = int(mes)
        self.ano = int(ano)
        self.estado = estado.strip().upper()

    def dias_feriados(self):
        self.feriados = []
        for date in wd.get_holidays(country='BR', state=self.estado, years=self.ano):
            if date.month == self.mes:
                self.feriados.append(date) 
        return self.feriados

    def qtd_dias_mes(self):
        self.data_comeco = dt.date(self.ano, self.mes, 1)
        self.data_fim = self._validador_fim_do_mes()
        qtd_dias = self.data_fim - self.data_comeco
        return qtd_dias.days
    
    def _validador_fim_do_mes(self):
        if self.mes == 12:
            data_fim = dt.date(self.ano + 1, 1, 1)
        else:
            data_fim = dt.date(self.ano, self.mes + 1, 1)
        return data_fim

    def dias_mes(self):
        lista_datas = []
        for i in range(self.qtd_dias_mes()):
            day = self.data_comeco + dt.timedelta(days=i)
            lista_datas.append(day)
        return lista_datas

    def dias_uteis_mes(self):
        lista_dias_uteis = []
        for dia in self.dias_mes():
            if dia.weekday() in [5, 6] or dia in self.dias_feriados():
                pass
            else:
                lista_dias_uteis.append(dia)
        return lista_dias_uteis
    
    def __len__(self):
        return len(self.dias_uteis_mes())

    def imprime_dias_uteis_mes(self):
        print(f'A quantidade de dias trabalhados no mês {self.mes}/{self.ano} é de:' f'\033[1m {len(self.dias_uteis_mes())} dias \033[0m')
        print()
