import pandas as pd
import re
import asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
from bs4 import BeautifulSoup

from .config import Config
from .log import Log

# todo: trocar para o django orm
from .data import Avaliacao, Disciplina

class Avaliacao:
    def __init__(self, descricao, data, nota):
        self.descricao = descricao
        self.data = data
        self.nota = nota


class Disciplina:
    def __init__(self, codigo, descricao, faltas, frequencia, media):
        self.codigo = codigo
        self.descricao = descricao
        self.faltas = faltas
        self.frequencia = frequencia
        self.media = media
        self.avaliacoes = []

    def adicionar(self, avaliacao):
        self.avaliacoes.append(avaliacao)
        pass


class Disciplinas:
    def __init__(self) -> None:
        self.disciplinas = []

    def adicionar(self, disciplina):
        self.disciplinas.append(disciplina)
        pass

    def obter(self):
        return self.disciplinas


class Siga:
    def __init__(self, headless = True) -> None:
        self.dados = Disciplinas()
        self.options = Options()
        self.options.headless = headless
        self.driver = webdriver.Firefox(options=self.options)
        # Log(f'Options: {self.options}')
    
    def autenticar(self, usuario, senha):
        self.driver.get(Config.SIGAURL_LOGIN)
        sleep(1)
        self.driver.find_element(By.ID, 'vSIS_USUARIOID').send_keys(usuario)
        self.driver.find_element(By.ID, 'vSIS_USUARIOSENHA').send_keys(senha)
        self.driver.find_element(By.NAME, 'BTCONFIRMA').click()
        sleep(1)
    
    def requisitar(self) -> Disciplinas:
        try:
            self.driver.get(Config.SIGAURL_NOTAS)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # disciplinas
            disciplinas_html = soup.find_all('tr', {'id': re.compile(r'Grid4ContainerRow_\d+')})
            disciplina_id = 0
            for disciplina_html in disciplinas_html:
                disciplina_id +=1
                codigo = disciplina_html.find('span', {
                    'id': re.compile(r'span_vACD_DISCIPLINASIGLA_\d+')
                }).text.strip()
                descricao = disciplina_html.find('span', {
                        'id': re.compile(r'span_vACD_DISCIPLINANOME_\d+')
                }).text.strip()
                media = disciplina_html.find('span', {
                    'id': re.compile(r'span_vACD_ALUNOHISTORICOITEMMEDIAFINAL_\d+')
                }).text.strip()
                faltas = disciplina_html.find('span', {
                    'id': re.compile(r'span_vACD_ALUNOHISTORICOITEMQTDFALTAS_\d+')
                }).text.strip()
                frequencia = disciplina_html.find('span', {
                        'id': re.compile(r'span_vACD_ALUNOHISTORICOITEMFREQUENCIA_\d+')
                }).text.strip()                

                disciplina = Disciplina(codigo, descricao, faltas, frequencia, media)
                self.dados.adicionar(disciplina)

                # avaliações
                avaliacoes_html = soup.find_all('tr', {
                    'id': re.compile(r'Grid1Container_{}Row_\d+'.format(str(disciplina_id).zfill(4)))
                })
                avaliacao_id = 0
                for avaliacao_html in avaliacoes_html:
                    avaliacao_id +=1
                    descricao = avaliacao_html.find('span', {
                        'id': 'span_vACD_PLANOENSINOAVALIACAOTITULO_{}{}'
                            .format(str(avaliacao_id).zfill(4), str(disciplina_id).zfill(4))
                    }).text.strip()
                    data = avaliacao_html.find('span', {
                        'id': 'span_vACD_PLANOENSINOAVALIACAOPARCIALDATALANCAMENTO_{}{}'
                            .format(str(avaliacao_id).zfill(4), str(disciplina_id).zfill(4))
                    }).text.strip()
                    nota = avaliacao_html.find('span', {
                        'id': 'span_vACD_PLANOENSINOAVALIACAOPARCIALNOTA_{}{}'
                            .format(str(avaliacao_id).zfill(4), str(disciplina_id).zfill(4))
                    }).text.strip()

                    if descricao == None: descricao = ''
                    if data == None: data = ''
                    if nota == None: nota = ''

                    avaliacao = Avaliacao(descricao, data, nota)
                    disciplina.adicionar(avaliacao)
            pass
        finally:
            self.driver.quit()
            pass

        return self.dados
