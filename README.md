
# Cap 6 - Python e Além - Fase 2: Sistema de Monitoramento de Perdas na Colheita de Cana-de-Açúcar

## Integrantes do GRUPO 13

| Nome | RM | Email |
| :--- | :--- | :--- |
| Viviane de Castro | RM567367 | vivi.topproducer@gmail.com |
| GUILHERME FERREIRA SANTOS | RM566833 | gifisi.channel@gmail.com |
| André Pessoa Gaidzakian | RM567877 | andrepgaidzak@gmail.com |
| Erick Prados Pereira | RM566833 | erick.prados.pereira@gmail.com |

-----

## 1\. O Problema do Agronegócio: Perdas na Colheita de Cana

O agronegócio é um pilar da economia brasileira, representando mais de 20% do PIB nacional. Dentro desse vasto setor, a cultura da cana-de-açúcar é uma das mais relevantes, com o Brasil sendo o maior produtor mundial. Na safra 2018/2019, por exemplo, a produção atingiu cerca de 620 milhões de toneladas.

No entanto, um dos maiores desafios enfrentados pelos produtores é a **perda durante o processo de colheita**. Estudos da SOCICANA indicam que as perdas na colheita mecanizada podem chegar a **15% da produção**. Esse percentual, aparentemente pequeno, representa um prejuízo financeiro gigantesco, equivalente à capacidade de aquisição de novas usinas de etanol.

As causas dessas perdas são variadas, incluindo velocidade inadequada das colhedoras, falhas na regulagem dos equipamentos e compactação do solo. Diante desse cenário, o monitoramento preciso e a análise de dados tornam-se ferramentas essenciais para a tomada de decisões estratégicas que visam mitigar esses prejuízos e aumentar a eficiência operacional.

## 2\. Nossa Solução: Uma Ferramenta de Análise e Gestão

Para endereçar este problema, desenvolvemos um sistema em Python que permite ao produtor rural registrar, monitorar e analisar as perdas ocorridas em cada evento de colheita de cana-de-açúcar. A solução visa transformar dados brutos em insights claros, auxiliando na gestão e na melhoria contínua dos processos agrícolas.

### Funcionalidades Principais

1.  **Registro Detalhado de Colheitas:**

      * O usuário pode registrar dados essenciais de cada colheita, como o tipo (manual ou mecânica), a produtividade estimada (em t/ha) e a produtividade real obtida.
      * O sistema solicita o valor da tonelada para calcular o impacto financeiro de forma precisa.

2.  **Cálculo Automático de Perdas e Prejuízos:**

      * Com base nos dados de produtividade, o sistema calcula automaticamente o **percentual de perda** e o **prejuízo financeiro** correspondente em Reais (R$).
      * A data e a hora de cada registro são salvas para garantir a rastreabilidade e análise temporal.

3.  **Lógica Inovadora de Análise de Ganhos:**

      * O sistema foi projetado para focar no problema central: as perdas. Caso a produtividade real seja **maior** que a estimada, a ferramenta parabeniza o usuário pelo **ganho de produtividade** e não armazena o registro, mantendo a base de dados focada exclusivamente em eventos de prejuízo que necessitam de análise.

4.  **Consistência e Validação de Dados:**

      * Para garantir a integridade dos dados, todas as entradas numéricas (produtividade, valor) são validadas para aceitar apenas números, evitando erros que poderiam comprometer as análises futuras.

5.  **Geração de Relatórios Estruturados:**

      * A ferramenta gera dois tipos de relatórios para diferentes finalidades:
          * `relatorio.txt`: Um relatório de fácil leitura, formatado para o entendimento humano. Ele apresenta cada registro de perda de forma detalhada e finaliza com um **sumário executivo** contendo o total de registros, a média de perda percentual e, mais importante, o **prejuízo total acumulado**.
          * `relatorio.json`: Um arquivo com dados estruturados, ideal para a integração com outros sistemas, dashboards de Business Intelligence (BI) ou análises de dados mais avançadas.

### Estrutura do Projeto

O código foi organizado de forma modular para facilitar a manutenção e escalabilidade:

  * `main.py`: Ponto de entrada da aplicação, responsável por exibir o menu principal ao usuário.
  * `banco.py`: Gerencia toda a interação com o banco de dados Oracle, incluindo a conexão, criação da tabela e as operações de inserção e consulta de dados.
  * `colheita.py`: Contém a lógica de negócio para registrar uma nova colheita e calcular as perdas.
  * `relatorios.py`: Responsável por consultar os dados no banco e gerar os arquivos de relatório (`.txt` e `.json`).
  * `utils.py`: Módulo com funções utilitárias, como a validação de inputs do usuário.

## 3\. Como Executar o Projeto

### Pré-requisitos

  * Python 3.x instalado.
  * Acesso a um banco de dados Oracle.
  * Oracle Instant Client configurado no ambiente, com o `PATH` do sistema apontando para seus binários.
  * A biblioteca `cx_Oracle` para a conexão Python-Oracle.

### Instalação

1.  Clone este repositório para a sua máquina local.
2.  Instale a biblioteca `cx_Oracle` usando o pip:
    ```bash
    pip install cx_Oracle
    ```
3.  **Configure a Conexão com o Banco de Dados:**
      * Abra o arquivo `banco.py`.
      * Altere as variáveis `USER`, `PASSWORD` e `DSN` com as suas credenciais do Oracle.
    <!-- end list -->
    ```python
    # Exemplo de configuração em banco.py
    USER = "seu_usuario_oracle"
    PASSWORD = "sua_senha"
    DSN = "localhost/XE" # Ou o DSN correspondente ao seu ambiente
    ```

### Execução

1.  Navegue até o diretório raiz do projeto pelo terminal.

2.  Execute o arquivo `main.py`:

    ```bash
    python main.py
    ```

3.  O menu interativo será exibido no console. Siga as opções para registrar colheitas ou gerar relatórios.

    ```
    === Sistema de Monitoramento de Perdas na Colheita de Cana ===
    1 - Registrar nova colheita
    2 - Gerar relatório
    3 - Sair
    Escolha uma opção:
    ```

## 4\. Conclusão

Este projeto aplica conceitos de programação em Python para criar uma solução prática e relevante para o agronegócio. Ao permitir um monitoramento detalhado das perdas na colheita, a ferramenta oferece aos produtores de cana-de-açúcar uma base sólida para otimizar suas operações, reduzir prejuízos e aumentar a sustentabilidade de seus negócios, alinhando-se às tendências de uma agricultura cada vez mais digital e orientada por dados.