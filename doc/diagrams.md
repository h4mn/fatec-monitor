# Diagramas do Fatec-Monitor

## 1. Tabela de Requisitos

| Requisito | Grupo | Descrição | Concluído |
| --: | :-: | :-- | :-: |
| In1 | Interface | Interface para navegação dos recursos básicos | - |
| Re1 | Registro | Automatizar Obtenção de Dados do SIGA | :white_check_mark: |
| Re2 | Registro | Registrar nota em disciplinas do curso | - |
| Re3 | Registro | Armazenamento seguro e persistente das informações | - |
| Re4 | Registro | Suporte para múltiplos cursos e semestres | - |
| Ca1 | Cálculo | Cálculo de média por disciplina | - |
| Ca2 | Cálculo | Cálculo de média geral do curso | - |
| Cl1 | Calendário | Notificações ou lembretes para prazos e atividades importantes | - |
| Cl2 | Calendário | Integração com calendário acadêmico para monitorar prazos de projetos e provas | - |
| Pr1 | Progresso | Acompanhamento do desempenho acadêmico ao longo do tempo | - |
| Pr2 | Progresso | Geração de estatísticas, como média, desvio padrão, etc. | - |
| An1 | Análise | Geração de relatórios personalizados | - |
| An2 | Análise | Visualização de gráficos e representações visuais dos dados | - |
| Q1 | Qualidade | Tratamento de exceções e validação de entrada de dados | - |
| M1 | Metas | Capacidade de definir metas de desempenho e rastrear o progresso em relação a elas | - |
| Ia1 | Inteligência | Funcionalidade de Feedback e sugestões baseados nas informações extraídas e submetidas ao GPT| - |
| Op1 | Opcional | Interface amigável e intuitiva | :x: |
| Op2 | Opcional | Configurações personalizáveis, como pesos de notas, critérios de aprovação, etc. | - |
| Op3 | Opcional | Importação e exportação de dados em formatos comuns (CSV, por exemplo) | - |
| Op4 | Opcional | Compatibilidade multiplataforma, incluindo web, desktop e dispositivos móveis | - |
| Op5 | Opcional | Suporte a diferentes sistemas de avaliação, como notas numéricas, conceituais, etc. | - |
| Op6 | Opcional | Suporte a disciplinas optativas, eletivas e obrigatórias | - |
| Op7 | Opcional | Backup e recuperação de dados | - |

## 2. Casos de Uso

```mermaid
graph TD
    U[Usuário] ---|Navegar| R10[Interface para navegação]
    R2 ---|Persistir| BD[Banco de Dados]
    I1[GPT] ---|Analisar| R5
    subgraph "G1"
        R1[Obtenção de Dados do SIGA]
        R2[Notas e Disciplinas]
        R3[Relatórios e Gráficos]

        R10 -->|Automatizar| R1
        R10 -->|Registrar| R2
        R10 -->|Visualizar| R3        
    end

    R3 --- R31
    subgraph "G2"
        R31[Estatísticas]
        R20[Definição de Metas]
        R8[Relatórios e Gráficos]
        R5[Desempenho]

        R31 -->|Configurar| R20
        R31 -->|Visualizar| R8
        R5 -->|Visualizar| R8
        R31 -->|Gerar| R5
    end

```

### 2.1. Automatizar Obtenção de Dados do SIGA

Este caso de uso descreve o processo de automação para obtenção dos dados das notas e disciplinas a partir do sistema SIGA.

#### Atores

- Usuário

#### Pré-condições

- O usuário deve estar autenticado no sistema;
- O usuário deve estar na página de registro de notas;

#### Pós-condições

- As notas são registradas no sistema;
- As informações obtidas do SIGA são armazenadas para referência futura;

#### Fluxo do Caso de Uso

```mermaid
sequenceDiagram
    participant Usuario
    participant Sistema
    participant SIGA

    Usuario->>Sistema: Seleciona opção de automação
    Sistema->>Sistema: Solicita credenciais do SIGA
    Sistema->>Usuario: Solicita inserção de credenciais
    Usuario->>Sistema: Insere credenciais e confirma
    Sistema->>SIGA: Realiza automação de login

    alt Login bem-sucedido
        SIGA-->>Sistema: Dados das notas e disciplinas
        Sistema->>Sistema: Preenche campos de registro
        Sistema->>Usuario: Exibe informações preenchidas
        Usuario->>Sistema: Revisão e edição (se necessário)
        Sistema->>Usuario: Confirma registro de notas
        Sistema->>Sistema: Salva notas registradas
    else Login falhou
        SIGA--x Sistema: Falha no login
        Sistema->>Usuario: Exibe mensagem de erro
    end

```

## 3. Classes

```mermaid
classDiagram
    class Sistema {
        +Autenticar(usuario, senha)
        +Registrar(Dados)
        +exibeInformacoesPreenchidas()
        +salvaNotasRegistradas()
    }

    class Config {
        + url_login: str
        + url_notas: str
        + usuario: str
        + senha: str
    }

    class Siga {
        - config: Config
        - dados: Dados
        - driver: WebDriver
        + autenticar(usuario: str, senha: str): void
        + requisitar(): Dados
    }

    class WebDriver {
        // Implementação do Selenium
    }

    class Avaliacao {
        + descricao: str
        + data: str
        + nota: str
    }

    class Disciplina {
        + codigo: str
        + descricao: str
        + faltas: str
        + frequencia: str
        + media: str
        - avaliacoes: list[Avaliacao]
        + adicionar(avaliacao: Avaliacao): void
    }

    class Dados {
        - disciplinas: list[Disciplina]
        + adicionar(disciplina: Disciplina): void
        + obter(): list[Disciplina]
    }

    Sistema -- Siga : obtem dados
    Siga "1" -- "1" Config : utiliza
    Siga "1" -- "1" WebDriver : utiliza
    Siga "1" -- "1" Dados : utiliza
    Dados "1" -- "*" Disciplina : contém
    Disciplina "1" -- "*" Avaliacao : possui

```

## 4. Modelo ER

```mermaid
erDiagram
    DISCIPLINA {
        int ID
        string Codigo
        string Descricao
        int Faltas
        float Frequencia
        float Media
        date Importado
    }
    AVALIACAO {
        int ID
        string Descricao
        date Avaliado
        float Nota
        date Importado
        int DisciplinaID
    }
    DISCIPLINA ||--o{ AVALIACAO : "contém"

```
