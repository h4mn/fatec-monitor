import datetime

class Log:
    def __new__(self, mensagem):
        dth = datetime.datetime.now().strftime('%Y%m%d.%H%M%S')
        print(f'[{dth}] LOG: {mensagem}')
        pass

# Log('Iniciando o sistema')