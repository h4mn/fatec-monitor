from django.shortcuts import render

from .models import Disciplina, Avaliacao
from .utils.siga import Siga
from .utils.config import Config
from .utils.log import Log

# Imports locais
# from utils.siga import Siga
# from utils.config import Config


app = 'Fatec Monitor'
titulo = 'Fatec Monitor'

def login(request):
    # contexto
    contexto = {
        'app': app,
        'atual': 'Autenticar',
        'descricao': 'Utilitário para acompanhamento de notas, estatísticas e relatórios gerando motivação e melhorando o desempenho acadêmico.'
    }
    return render(request, 'autenticar.html', contexto)

def index(request):
    # contexto
    contexto = {
        'app': app,
        'atual': 'Home',
        'descricao': 'Utilitário para acompanhamento de notas, estatísticas e relatórios gerando motivação e melhorando o desempenho acadêmico.'
    }
    return render(request, 'home.html', contexto)

def disciplinas(request):
    # salva a disciplina
    # registro = Disciplina()
    # registro.codigo = request.POST.get('codigo')
    # registro.descricao = request.POST.get('descricao')
    # registro.save()

    # contexto
    contexto = {
        'app': app,
        'atual': 'Disciplinas',
        'disciplinas': Disciplina.objects.all()
    }
    return render(request, 'disciplinas.html', contexto)

def graficos(request):
    # contexto
    contexto = {
        'app': app,
        'atual': 'Gráficos',
        'descricao': 'Utilitário para acompanhamento de notas, estatísticas e relatórios gerando motivação e melhorando o desempenho acadêmico.'
    }
    return render(request, 'graficos.html', contexto)

def sincronizar(request):
    # Log(f'Config: {Config.SISTEMA_EMPRODUCAO}')
    # Log(f'Usuario: {Config.SIGA_USUARIO}')
    siga = Siga(Config.SISTEMA_EMPRODUCAO)

    Log(f'Teste: {app}')
    Log(f'Usuario: {Config.SIGA_USUARIO}')
    siga.autenticar(Config.SIGA_USUARIO, Config.SIGA_SENHA)

    dados = siga.requisitar()
    Log(f'Dados: {dados}')

    disciplinas = dados.obter()
    
    # Prepara o contexto
    disciplinas_context = []
    for disciplina in disciplinas:
        disciplinas_context.append({
            'codigo': disciplina.codigo,
            'descricao': disciplina.descricao,
            'faltas': disciplina.faltas,
            'frequencia': disciplina.frequencia,
            'media': disciplina.media,
            'avaliacoes': [
                {
                    'descricao': avaliacao.descricao,
                    'data': avaliacao.data,
                    'nota': avaliacao.nota
                }
                for avaliacao in disciplina.avaliacoes
            ],
        })
    context = {
        'app': app,
        'atual': 'Sincronizar',
        'descricao': 'Utilitário para acompanhamento de notas, estatísticas e relatórios gerando motivação e melhorando o desempenho acadêmico.',
        'disciplinas': disciplinas_context
    }

    # Renderiza o template
    print(context)
    return render(request, 'home.html', context)

def sincronizar_antigo():
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


# sincronizar(None)