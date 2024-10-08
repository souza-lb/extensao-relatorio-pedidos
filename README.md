<h1> Projeto de Extensão - Relatório de Pedidos</h1>  

<h2>Projeto de Extensão da Disciplina - Tópicos de Big Data em Python - Leonardo Bruno de Souza Silva - 202301011744</h2>

<h3>Repositório Principal do Projeto Relatório de Pedidos</h3>

<h3>O que você econtra aqui?</h3>

* Arquivos Jupyter Notebook ( nos formatos: nativo, pdf e markdown )
* Arquivo ".csv" sem tratamento.
* Arquivo ".csv" com tratamento. (Após análise e tratamento dos dados no Jupyter)
* Arquivo com dependências do projeto. (requisitos.txt)
* Arquivo Logo para adição no relatório.
* Arquivo de Relatório gerado pela aplicação.
* Na pasta "/src" arquivos para rodar o projeto fora do Jupyter.
* Arquivo Python para rodar o projeto em ambiente fora do Jupyter.
* Arquivos de gráficos.
* Script shell para configuração do ambiente do Jupyter Notebook ( Habilita o ambiente virtual, instala e configura tema escuro, organiza as pastas dos notebooks )

<h3>O que este projeto faz?</h3>  

* Trata a base da dados no ambiente Jupyter.
* Utiliza a biblioteca "pandas" e expressões regulares ( regex ) para normalizar os dados.
* Utiliza a biblioteca "plotly" para gerar gráficos dinâmicos.
* Utiliza a biblioteca "reportlab" para gerar relatório em pdf.
* Fornece um arquivo de código python para fora do Jupyter como alternativa se você não desejar usá-lo.



É altamente recomendado o uso do Jupyter para rodar o projeto, pois em seu ambiente é possível interagir com os gráficos  
dinâmicos e acompanhar todo o processo de tratamento dos dados antes da geração do relatório.  
Para criação do mapa de forma adequada foi necessário o tratamento do arquivo "DadosZazzleSemTratamento.csv". Ele inicialmente  
apresntava registros irregulares e sem padronização. Após tratamento adequado com a biblioteca pandas foi gerado o arquivo  
"DadosZazzleComTratamento.csv".

Para instalar as dependências do projeto faça:  

```bash
pip install -r requisitos.txt
```

Jupyter Rodando o Projeto:  

![Jupyter Rodando](/imagens/jupyter-rodando.png)  

Dataframe Alimentado com os Dados do arquivo ".csv":  

![Dataframe](/imagens/dataframe.png)  

Mapa Interativo Gerado pela Aplicação:  

![Mapa Interativo](/imagens/mapa-interativo.png)

Gráfico de Linha Interativo Gerado pela Aplicação:  

![Gráfico Interativo Linha](/imagens/grafico-interativo-linha.png)  

Gráfico de Barras Gerado pela Aplicação:  

![Gráfico Interativo Barras](/imagens/grafico-interativo-barras.png)  

Gráfico Interativo Pizza/ Torta Gerado pela Aplicação:  

![Gráfico Interativo Pizza](/imagens/grafico-interativo-pizza.png)  



Este repositório foi criado por: <b>Leonardo Bruno de Souza Silva</b><br>
<b>Matrícula 202301011744</b><br>
<b>Projeto de Extensão Relatório de Pedidos da Disciplina Tópicos de Big Data em Python</b><br>
202301011744@alunos.estacio.br<br>
<b>souzalb@proton.me</b>
