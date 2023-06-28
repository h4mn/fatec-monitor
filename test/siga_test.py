import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from config import Config
from siga import Siga

siga = Siga(Config.SISTEMA_EMPRODUCAO)
siga.autenticar(Config.SIGA_USUARIO, Config.SIGA_SENHA)
dados = siga.requisitar()
disciplinas = dados.obter()
print()
print('==================================================')
for disciplina in disciplinas:
    print(f'Disciplina: {disciplina.codigo} - {disciplina.descricao}')
    print(f'Faltas      : {disciplina.faltas}')
    print(f'Frequência  : {disciplina.frequencia}')
    print(f'Média       : {disciplina.media}')
    print()
    print('Avaliações:')
    for avaliacao in disciplina.avaliacoes:
        print(f'| Descricao | Data | Nota |')
        print(f'| {avaliacao.descricao} | {avaliacao.data} | {avaliacao.nota} |')
        print()
    print()
print('==================================================')