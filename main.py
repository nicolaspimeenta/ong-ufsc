import os
import pickle
from entidade.dados import Dados
from controle.controlador_inicial import ControladorInicial

if __name__ == "__main__":
    
    if not os.path.exists('dados.pkl'):
        with open('dados.pkl', 'wb') as arquivo:
            pickle.dump(Dados(), arquivo)

    ControladorInicial().iniciar()