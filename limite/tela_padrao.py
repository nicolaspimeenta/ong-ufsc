import pickle
import datetime
from abc import ABC

class TelaPadrao(ABC):
    def validaData(self, dia: str, mes: str, ano: str):
        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()): return False
        try: 
            data = datetime.date(int(ano), int(mes), int(dia))
            if data > datetime.date.today(): raise ValueError
            if (data.month == 2 and data.day == 29) and not (data.isocalendar()[1] == 9): raise ValueError
        except:
            return False
        else:
            return True
        
    def salvarDados(self, dados):
        with open('dados.pkl', 'wb') as arquivo:
            pickle.dump(dados, arquivo)
 