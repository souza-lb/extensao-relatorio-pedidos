# Importa as bibliotecas que vamos usar.
import pandas as pd
import plotly.express as px
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Image, Table, TableStyle, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas

# Gera o dataframe.
df = pd.read_csv("DadosZazzleComTratamento.csv")

# Efetua a contagem do número de pedidos por pais.
contagem_paises = df['Shipped To'].value_counts().reset_index()
# Troca os nomes das colunas do novo dataframe.
contagem_paises.columns = ['Pais', 'Pedidos']

# Gera o gráfico interativo.
fig = px.choropleth(contagem_paises,
                    locations='Pais',
                    locationmode='country names',
                    color='Pedidos',
                    title='Número de Pedidos por País',
                    color_continuous_scale='Rainbow')

# Conversão do gráfico para imagem estática.
fig.write_image('mapa.png', engine='kaleido')

# Gráfico de barras.
# Efetua a contagem do pedido.
# Poderia utilizar tambem os dados da célula acima.
contagem_paises = df['Shipped To'].value_counts().reset_index()
contagem_paises.columns = ['Pais', 'Pedidos']

# Obtém os 10 países com mais pedidos.
top_10_paises = contagem_paises.head(10)

# Gera o gráfico de barras
fig = px.bar(top_10_paises, 
             x='Pais', 
             y='Pedidos', 
             color='Pedidos',
             title='Top 10 Países com Mais Pedidos',
             color_continuous_scale='Rainbow')  # Usando uma escala de cores mais viva

# Ajustar o layout do gráfico
fig.update_layout(xaxis_title='País',
                  yaxis_title='Número de Pedidos',
                  xaxis_tickangle=-45)  # Rotaciona os rótulos do eixo x para melhor legibilidade

fig.write_image('barras.png', engine='kaleido')

# Geração do gráfico de pizza.

# Contagem de número de pedidos por país.
contagem_paises = df['Shipped To'].value_counts().reset_index()
contagem_paises.columns = ['Pais', 'Pedidos']

# Selecionar os 10 países com mais pedidos
top_5_paises = contagem_paises.head(5)

# Gera o gráfico
fig = px.pie(top_5_paises, 
             names='Pais', 
             values='Pedidos', 
             title='Top 5 Países com Mais Pedidos',
             color='Pais',  # Cada fatia representa um país com uma cor.
             color_discrete_sequence=px.colors.qualitative.Plotly)  # Define escala de cores qualitativa

fig.write_image('pizza.png', engine='kaleido')

# Gráfico de linha.

# Converter a coluna 'Date' para o tipo datetime especificando o formato
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')

# Extrair o ano da coluna 'Date'
df['Ano'] = df['Date'].dt.year

# Contar o número de pedidos por ano
pedidos_por_ano = df.groupby('Ano').size().reset_index(name='Pedidos')

# Criar o gráfico de linha com plotly
fig = px.line(pedidos_por_ano,
              x='Ano',
              y='Pedidos',
              title='Número de Pedidos por Ano',
              markers=True)  # Adiciona marcadores aos pontos de dados

# Ajustar o layout do gráfico
fig.update_layout(xaxis_title='Ano',
                  yaxis_title='Número de Pedidos',
                  xaxis=dict(tickmode='linear'))  # Define o modo de ticks do eixo x como linear

fig.write_image('linha.png', engine='kaleido')

# Bloco de geração do PDF.
arquivo_pdf = "Relatorio.pdf"
# Define o nome de arquivo e formato de página.
doc = SimpleDocTemplate(arquivo_pdf, pagesize=A4)
elements = []

# Adição da folha de rosto.
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Title'],
    alignment=TA_CENTER,
    fontSize=24,
    spaceAfter=12
)

logo_style = ParagraphStyle(
    'LogoStyle',
    parent=styles['Normal'],
    alignment=TA_CENTER,
    spaceAfter=12
)

title = Paragraph("Relatório de Pedidos (2011 - 2024)", title_style)
logo = Image("LogoLoja.jpeg", width=150, height=150)

# Adição da folha de rosto centralizada.
width, height = A4

# Espaçamento para centralizar verticalmente.
content_height = height - 2 * inch
title_height = 24
logo_height = 150

# Espaços verticais para centralização
space_before_title = (content_height - title_height - logo_height) / 2
space_after_title = 0.5 * inch

elements.append(Paragraph("<br/>" * int(space_before_title /12), styles['Normal']))
elements.append(title)
#elements.append(Paragraph("<br/>" * int(space_before_title /12), styles['Normal']))
elements.append(logo)
elements.append(Paragraph("<br/><br/>", styles['Normal']))

# Adiciona uma qebra de página.
elements.append(PageBreak())

# Função para adição das imagens ao PDF.
def adiciona_imagem_pdf(caminho_imagem, width=6*inch, height=4*inch):
    imagem = Image(caminho_imagem, width=width, height=height)
    elements.append(imagem)
    elements.append(Paragraph("<br/>", styles['Normal'])) # Espaço após adição de imagem.

# Chama a função e adiciona todas as imagens ao PDF.
for arquivo_imagem in ['mapa.png', 'barras.png', 'pizza.png', 'linha.png']:adiciona_imagem_pdf(arquivo_imagem)

# Adicona rodapé e numração das páginas.
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.drawString(1*inch, 0.75*inch, "Gerado Por: Leonardo Bruno / 202301011744 / 202301011744@alunos.estacio.br / souzalb@proton.me / TADS")
    canvas.drawRightString(A4[0] - 1*inch, 0.75*inch, str(doc.page))
    canvas.restoreState()
    
doc.build(elements, onFirstPage=footer, onLaterPages=footer)

print("Relatório Gerado.")