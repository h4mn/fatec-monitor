from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path)

class Config:
    OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
    SIGAURL_LOGIN = os.getenv('SIGAURL_LOGIN')
    SIGAURL_NOTAS = os.getenv('SIGAURL_NOTAS')
    SIGA_USUARIO = os.getenv('SIGA_USUARIO')
    SIGA_SENHA = os.getenv('SIGA_SENHA')
    SISTEMA_EMPRODUCAO = False