```python
pip install pandas==2.2.2 # Instalação da biblioteca pandas.
```

    Collecting pandas==2.2.2
      Using cached pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
    Requirement already satisfied: numpy>=1.23.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from pandas==2.2.2) (2.1.1)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from pandas==2.2.2) (2.9.0.post0)
    Collecting pytz>=2020.1 (from pandas==2.2.2)
      Using cached pytz-2024.2-py2.py3-none-any.whl.metadata (22 kB)
    Collecting tzdata>=2022.7 (from pandas==2.2.2)
      Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
    Requirement already satisfied: six>=1.5 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas==2.2.2) (1.16.0)
    Using cached pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)
    Using cached pytz-2024.2-py2.py3-none-any.whl (508 kB)
    Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
    Installing collected packages: pytz, tzdata, pandas
    Successfully installed pandas-2.2.2 pytz-2024.2 tzdata-2024.1
    Note: you may need to restart the kernel to use updated packages.



```python
import pandas as pd # Importa da biblioteca pandas.
```


```python
# Cria um dataframe com os dados do arquivo "DadosZazzleSemTratamento.csv".
df = pd.read_csv("DadosZazzleSemTratamento.csv")
```


```python
# Visualiza os dados do dataframe.
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
      <th>Original Product Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>Krista - Wellington, FL</td>
      <td>169-81207300-8095920</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>Krista - Wellington, FL</td>
      <td>169-49976541-2896161</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Ann - Edgewood, WA</td>
      <td>169-90893214-5598241</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Ann - Edgewood, WA</td>
      <td>169-74006166-4120061</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Ann - Edgewood, WA</td>
      <td>169-58758080-3397052</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>32389</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-36297848-8052705</td>
      <td>Cartão Elegante</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Erdogan - Ridgefield, NJ</td>
      <td>169-02825211-9211579</td>
      <td>1</td>
      <td>$14.62</td>
      <td>20.0%+</td>
      <td>$2.92 USD</td>
      <td>$2.92</td>
      <td>cleared</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32390</th>
      <td>3/23/2012 5:13:30 PM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Marcello - Lugano, Switzerland</td>
      <td>169-07935009-6598567</td>
      <td>5</td>
      <td>CHF51.55</td>
      <td>25.0%+</td>
      <td>CHF12.25 CHF</td>
      <td>$12.53</td>
      <td>cleared</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32391</th>
      <td>1/25/2012 1:32:32 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - São Paulo, Brazil</td>
      <td>169-89467669-9328923</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
      <td>zazzle_postcard2</td>
    </tr>
    <tr>
      <th>32392</th>
      <td>12/14/2011 4:51:41 AM</td>
      <td>149-99118322-0835239</td>
      <td>Nossa Senhora da Conceição Aparecida</td>
      <td>zazzle_bag</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Neusa - Rio De Janeiro, Brazil</td>
      <td>169-81662931-4781555</td>
      <td>1</td>
      <td>R$26.25</td>
      <td>10.0%</td>
      <td>R$2.63 BRL</td>
      <td>$1.24</td>
      <td>cleared</td>
      <td>No</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32393</th>
      <td>12/10/2011 4:48:28 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - Sao Paulo, Brazil</td>
      <td>169-07034355-9170295</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
      <td>zazzle_postcard2</td>
    </tr>
  </tbody>
</table>
<p>32394 rows × 18 columns</p>
</div>



```python
# Vamos descartar a última coluna ("Original Product Type") pois seus dados não são necessários.
df = df.drop(columns=["Original Product Type"])
```


```python
# Vamos visualizar como ficou o topo da tabela após a exclusão.
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>Krista - Wellington, FL</td>
      <td>169-81207300-8095920</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>Krista - Wellington, FL</td>
      <td>169-49976541-2896161</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Ann - Edgewood, WA</td>
      <td>169-90893214-5598241</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Ann - Edgewood, WA</td>
      <td>169-74006166-4120061</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Ann - Edgewood, WA</td>
      <td>169-58758080-3397052</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Vamos visualizar o fim da tabela após a exclusão.
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32389</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-36297848-8052705</td>
      <td>Cartão Elegante</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Erdogan - Ridgefield, NJ</td>
      <td>169-02825211-9211579</td>
      <td>1</td>
      <td>$14.62</td>
      <td>20.0%+</td>
      <td>$2.92 USD</td>
      <td>$2.92</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32390</th>
      <td>3/23/2012 5:13:30 PM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Marcello - Lugano, Switzerland</td>
      <td>169-07935009-6598567</td>
      <td>5</td>
      <td>CHF51.55</td>
      <td>25.0%+</td>
      <td>CHF12.25 CHF</td>
      <td>$12.53</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32391</th>
      <td>1/25/2012 1:32:32 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - São Paulo, Brazil</td>
      <td>169-89467669-9328923</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32392</th>
      <td>12/14/2011 4:51:41 AM</td>
      <td>149-99118322-0835239</td>
      <td>Nossa Senhora da Conceição Aparecida</td>
      <td>zazzle_bag</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Neusa - Rio De Janeiro, Brazil</td>
      <td>169-81662931-4781555</td>
      <td>1</td>
      <td>R$26.25</td>
      <td>10.0%</td>
      <td>R$2.63 BRL</td>
      <td>$1.24</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32393</th>
      <td>12/10/2011 4:48:28 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - Sao Paulo, Brazil</td>
      <td>169-07034355-9170295</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Buscamos obter a informação do total de vendas por pais. A coluna "Shipped To"
# nos fornece esssa informação. Mas ela necessita de tratamentos.
# Recebi do proprietário a informação de que provavelmente haverá um grande número de pedidos
# dos EUA pois a filial da Zazzle é na Califórnia. (Zazzle é o serviço que a RicardoArtes utiliza
# na confecção dos produtos ). Vou focar inicialmente no tratamento dos pedidos dos EUA.

# Vamos analizar a linha 32389
# Erdogan - Ridgefield, NJ
# Há um padrão que parece repetir (nome_usuario - Distrito - Sigla Estado )
# Ridgefield é um Distrito em New Jersey.
# Se observarmos outras linhas esse padrão repete logo:
```


```python
import  re # Importa a biblioteca de expressões regulares (regex).

# Tratamento dados EUA.
estados_validos = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
    'DC'
]

# Percorre o dataframe verificando o padrão na coluna "Shipped To".
# Se os dois útimos caracteres do padrão representarem um estado válido
# atualiza a coluna com o nome do país.

for i in range(len(df)):
    enviado_para = df.at[i, 'Shipped To']
    match = re.match(r"[^-]+ - [^,]+, ([A-Z]{2})", enviado_para)
    if match:
        estado = match.group(1)
        if estado in estados_validos:
            df.at[i, 'Shipped To'] = 'United States'
```


```python
# Vamos ver como ficou o dataframe.
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-81207300-8095920</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-49976541-2896161</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-90893214-5598241</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-74006166-4120061</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-58758080-3397052</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>32389</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-36297848-8052705</td>
      <td>Cartão Elegante</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-02825211-9211579</td>
      <td>1</td>
      <td>$14.62</td>
      <td>20.0%+</td>
      <td>$2.92 USD</td>
      <td>$2.92</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32390</th>
      <td>3/23/2012 5:13:30 PM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Marcello - Lugano, Switzerland</td>
      <td>169-07935009-6598567</td>
      <td>5</td>
      <td>CHF51.55</td>
      <td>25.0%+</td>
      <td>CHF12.25 CHF</td>
      <td>$12.53</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32391</th>
      <td>1/25/2012 1:32:32 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - São Paulo, Brazil</td>
      <td>169-89467669-9328923</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32392</th>
      <td>12/14/2011 4:51:41 AM</td>
      <td>149-99118322-0835239</td>
      <td>Nossa Senhora da Conceição Aparecida</td>
      <td>zazzle_bag</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Neusa - Rio De Janeiro, Brazil</td>
      <td>169-81662931-4781555</td>
      <td>1</td>
      <td>R$26.25</td>
      <td>10.0%</td>
      <td>R$2.63 BRL</td>
      <td>$1.24</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32393</th>
      <td>12/10/2011 4:48:28 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - Sao Paulo, Brazil</td>
      <td>169-07034355-9170295</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
<p>32394 rows × 17 columns</p>
</div>



```python
# Vamos ver as 15 primeiras linhas.
df.head(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-81207300-8095920</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-49976541-2896161</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-90893214-5598241</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-74006166-4120061</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-58758080-3397052</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>5</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-61178968-9587070</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>6</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-54099369-9337645</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-08265809-1186820</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9/10/2024 10:44:52 AM</td>
      <td>256-10893432-1682747</td>
      <td>Professional Chic Elegant Plain and Monogram</td>
      <td>visualpromotions_folder</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-03838267-3563825</td>
      <td>1</td>
      <td>$21.55</td>
      <td>10.0%</td>
      <td>$2.16 USD</td>
      <td>$2.16</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9/10/2024 1:29:07 AM</td>
      <td>240-71784709-9740850</td>
      <td>Elegant Minimal Plain Professional Black</td>
      <td>zazzle_businesscard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Daniela - Stadl-paura, Austria</td>
      <td>169-56003445-6055249</td>
      <td>1</td>
      <td>€20.01</td>
      <td>10.0%</td>
      <td>€1.60 EUR++ at</td>
      <td>$1.67**</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-03814505-1489444</td>
      <td>3</td>
      <td>$20.10</td>
      <td>10.0%</td>
      <td>$2.07 USD</td>
      <td>$2.07</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>11</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-03814505-1489444</td>
      <td>3</td>
      <td>$1.20</td>
      <td>5.0%</td>
      <td>See Above</td>
      <td>See Above</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-07678231-6056679</td>
      <td>1</td>
      <td>$6.70</td>
      <td>10.0%</td>
      <td>$0.69 USD</td>
      <td>$0.69</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-07678231-6056679</td>
      <td>1</td>
      <td>$0.40</td>
      <td>5.0%</td>
      <td>See Above</td>
      <td>See Above</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>14</th>
      <td>9/9/2024 6:35:20 PM</td>
      <td>240-71198261-7218569</td>
      <td>Minimalist Modern Elegant Loyalty Discount</td>
      <td>zazzle_flatloyaltycard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>Stacey - Banksia Beach, Australia</td>
      <td>169-05198520-5009191</td>
      <td>3</td>
      <td>$73.71</td>
      <td>10.0%</td>
      <td>$4.74 AUD++</td>
      <td>$2.99**</td>
      <td>pending</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Agora as 15 linhas finais.
df.tail(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32379</th>
      <td>10/5/2012 3:11:06 AM</td>
      <td>240-99921669-9837741</td>
      <td>Elegante 2</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Peter - Waldbröl, Germany</td>
      <td>169-42732429-6459387</td>
      <td>1</td>
      <td>€23.90</td>
      <td>20.0%+</td>
      <td>€4.78 EUR de</td>
      <td>$5.99</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32380</th>
      <td>9/29/2012 7:23:14 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Judith - Berlin, Germany</td>
      <td>169-55460700-1242458</td>
      <td>1</td>
      <td>€13.70</td>
      <td>21.7%+</td>
      <td>€2.82 EUR de</td>
      <td>$3.53</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32381</th>
      <td>9/29/2012 7:23:14 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Judith - Berlin, Germany</td>
      <td>169-26723724-9072562</td>
      <td>1</td>
      <td>€13.70</td>
      <td>21.7%+</td>
      <td>€2.82 EUR de</td>
      <td>$3.53</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32382</th>
      <td>9/28/2012 9:30:49 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Enis - Hildrizhausen, Germany</td>
      <td>169-49495972-3022464</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32383</th>
      <td>9/27/2012 11:33:40 PM</td>
      <td>240-96436692-6877736</td>
      <td>Verde Nouveau</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Sonja - Gießen, Germany</td>
      <td>169-21093046-5755614</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32384</th>
      <td>9/12/2012 6:00:45 PM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Mike - Dachau, Germany</td>
      <td>169-03228966-4552669</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32385</th>
      <td>9/7/2012 8:39:04 PM</td>
      <td>240-99921669-9837741</td>
      <td>Elegante 2</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-82393615-4974728</td>
      <td>1</td>
      <td>$21.35</td>
      <td>20.0%+</td>
      <td>$4.27 USD</td>
      <td>$4.27</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32386</th>
      <td>8/21/2012 3:38:54 PM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Nasser - Zürich, Switzerland</td>
      <td>169-29930272-7692397</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32387</th>
      <td>7/20/2012 8:29:12 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-85679716-9837316</td>
      <td>1</td>
      <td>$19.50</td>
      <td>21.7%+</td>
      <td>$3.17 USD</td>
      <td>$3.17</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32388</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-26501880-2522478</td>
      <td>1</td>
      <td>$5.37</td>
      <td>25.0%+</td>
      <td>$1.27 USD</td>
      <td>$1.27</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32389</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-36297848-8052705</td>
      <td>Cartão Elegante</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-02825211-9211579</td>
      <td>1</td>
      <td>$14.62</td>
      <td>20.0%+</td>
      <td>$2.92 USD</td>
      <td>$2.92</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32390</th>
      <td>3/23/2012 5:13:30 PM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Marcello - Lugano, Switzerland</td>
      <td>169-07935009-6598567</td>
      <td>5</td>
      <td>CHF51.55</td>
      <td>25.0%+</td>
      <td>CHF12.25 CHF</td>
      <td>$12.53</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32391</th>
      <td>1/25/2012 1:32:32 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - São Paulo, Brazil</td>
      <td>169-89467669-9328923</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32392</th>
      <td>12/14/2011 4:51:41 AM</td>
      <td>149-99118322-0835239</td>
      <td>Nossa Senhora da Conceição Aparecida</td>
      <td>zazzle_bag</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Neusa - Rio De Janeiro, Brazil</td>
      <td>169-81662931-4781555</td>
      <td>1</td>
      <td>R$26.25</td>
      <td>10.0%</td>
      <td>R$2.63 BRL</td>
      <td>$1.24</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32393</th>
      <td>12/10/2011 4:48:28 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Adriana - Sao Paulo, Brazil</td>
      <td>169-07034355-9170295</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Vamos tratar os dados dos demais países.
# Aqui mais um padrão ocorre:
# Adriana - Sao Paulo, Brazil
# Em alguns casos o nome do usuário não é informado:
# - Japan
# Há sempre uma constante: O nome do país é informado.
# Podemos comparar o texto da célula e verificar se ele informa um país válido em algum ponto.
# Se for localizado podemos substituir o valor da célula com o nome do país.
```


```python
# Lista de países

paises_validos = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
    "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
    "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North",
    "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
    "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
    "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

dicionario_paises = {pais: pais for pais in paises_validos}

for index, row in df.iterrows():
    enviado_para = row['Shipped To']
    for pais in dicionario_paises:
        if pais in enviado_para:
            df.at[index, 'Shipped To'] = pais
            break
```


```python
# Vamos analisar o topo do dataframe após o processamento.
df.head(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-81207300-8095920</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/10/2024 2:13:06 PM</td>
      <td>217-02854107-2295764</td>
      <td>Modern Minimalist Real Estate Black</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-49976541-2896161</td>
      <td>1</td>
      <td>$6.76</td>
      <td>10.0%</td>
      <td>$0.54 USD</td>
      <td>$0.54</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-90893214-5598241</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-74006166-4120061</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-58758080-3397052</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>5</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-61178968-9587070</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>6</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-54099369-9337645</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9/10/2024 2:01:50 PM</td>
      <td>256-50771486-3204370</td>
      <td>Personalized Teacher Name</td>
      <td>hamptontech_selfinkingstamp</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-08265809-1186820</td>
      <td>1</td>
      <td>$11.18</td>
      <td>10.0%</td>
      <td>$1.12 USD</td>
      <td>$1.12</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9/10/2024 10:44:52 AM</td>
      <td>256-10893432-1682747</td>
      <td>Professional Chic Elegant Plain and Monogram</td>
      <td>visualpromotions_folder</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-03838267-3563825</td>
      <td>1</td>
      <td>$21.55</td>
      <td>10.0%</td>
      <td>$2.16 USD</td>
      <td>$2.16</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9/10/2024 1:29:07 AM</td>
      <td>240-71784709-9740850</td>
      <td>Elegant Minimal Plain Professional Black</td>
      <td>zazzle_businesscard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>169-56003445-6055249</td>
      <td>1</td>
      <td>€20.01</td>
      <td>10.0%</td>
      <td>€1.60 EUR++ at</td>
      <td>$1.67**</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-03814505-1489444</td>
      <td>3</td>
      <td>$20.10</td>
      <td>10.0%</td>
      <td>$2.07 USD</td>
      <td>$2.07</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>11</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-03814505-1489444</td>
      <td>3</td>
      <td>$1.20</td>
      <td>5.0%</td>
      <td>See Above</td>
      <td>See Above</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-07678231-6056679</td>
      <td>1</td>
      <td>$6.70</td>
      <td>10.0%</td>
      <td>$0.69 USD</td>
      <td>$0.69</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9/9/2024 11:53:50 PM</td>
      <td>217-86366175-7539770</td>
      <td>Round Custom Your Company Logo</td>
      <td>zazzle_sticker</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-07678231-6056679</td>
      <td>1</td>
      <td>$0.40</td>
      <td>5.0%</td>
      <td>See Above</td>
      <td>See Above</td>
      <td>pending</td>
      <td>No</td>
    </tr>
    <tr>
      <th>14</th>
      <td>9/9/2024 6:35:20 PM</td>
      <td>240-71198261-7218569</td>
      <td>Minimalist Modern Elegant Loyalty Discount</td>
      <td>zazzle_flatloyaltycard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>Australia</td>
      <td>169-05198520-5009191</td>
      <td>3</td>
      <td>$73.71</td>
      <td>10.0%</td>
      <td>$4.74 AUD++</td>
      <td>$2.99**</td>
      <td>pending</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Vamos analisar o final do dataframe.
df.tail(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product ID</th>
      <th>Product Title</th>
      <th>Product Type</th>
      <th>Is Customized</th>
      <th>Is Canceled</th>
      <th>Store</th>
      <th>Referred</th>
      <th>Shipped To</th>
      <th>Order Item ID</th>
      <th>Quantity</th>
      <th>Subtotal</th>
      <th>Royalty Rate</th>
      <th>Royalty</th>
      <th>Royalty (USD)</th>
      <th>Status</th>
      <th>Is Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32379</th>
      <td>10/5/2012 3:11:06 AM</td>
      <td>240-99921669-9837741</td>
      <td>Elegante 2</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>169-42732429-6459387</td>
      <td>1</td>
      <td>€23.90</td>
      <td>20.0%+</td>
      <td>€4.78 EUR de</td>
      <td>$5.99</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32380</th>
      <td>9/29/2012 7:23:14 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>169-55460700-1242458</td>
      <td>1</td>
      <td>€13.70</td>
      <td>21.7%+</td>
      <td>€2.82 EUR de</td>
      <td>$3.53</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32381</th>
      <td>9/29/2012 7:23:14 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>169-26723724-9072562</td>
      <td>1</td>
      <td>€13.70</td>
      <td>21.7%+</td>
      <td>€2.82 EUR de</td>
      <td>$3.53</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32382</th>
      <td>9/28/2012 9:30:49 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>169-49495972-3022464</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32383</th>
      <td>9/27/2012 11:33:40 PM</td>
      <td>240-96436692-6877736</td>
      <td>Verde Nouveau</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>169-21093046-5755614</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32384</th>
      <td>9/12/2012 6:00:45 PM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>169-03228966-4552669</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32385</th>
      <td>9/7/2012 8:39:04 PM</td>
      <td>240-99921669-9837741</td>
      <td>Elegante 2</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-82393615-4974728</td>
      <td>1</td>
      <td>$21.35</td>
      <td>20.0%+</td>
      <td>$4.27 USD</td>
      <td>$4.27</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32386</th>
      <td>8/21/2012 3:38:54 PM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Switzerland</td>
      <td>169-29930272-7692397</td>
      <td>1</td>
      <td>€15.85</td>
      <td>21.7%+</td>
      <td>€3.27 EUR de</td>
      <td>$4.09</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32387</th>
      <td>7/20/2012 8:29:12 AM</td>
      <td>240-27050935-7725549</td>
      <td>Nouveau graphite</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>3rd Party</td>
      <td>United States</td>
      <td>169-85679716-9837316</td>
      <td>1</td>
      <td>$19.50</td>
      <td>21.7%+</td>
      <td>$3.17 USD</td>
      <td>$3.17</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32388</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-26501880-2522478</td>
      <td>1</td>
      <td>$5.37</td>
      <td>25.0%+</td>
      <td>$1.27 USD</td>
      <td>$1.27</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32389</th>
      <td>6/21/2012 9:51:00 AM</td>
      <td>240-36297848-8052705</td>
      <td>Cartão Elegante</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>United States</td>
      <td>169-02825211-9211579</td>
      <td>1</td>
      <td>$14.62</td>
      <td>20.0%+</td>
      <td>$2.92 USD</td>
      <td>$2.92</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32390</th>
      <td>3/23/2012 5:13:30 PM</td>
      <td>240-48013704-5084466</td>
      <td>Grécia Contemporânea</td>
      <td>zazzle_profilecard</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Switzerland</td>
      <td>169-07935009-6598567</td>
      <td>5</td>
      <td>CHF51.55</td>
      <td>25.0%+</td>
      <td>CHF12.25 CHF</td>
      <td>$12.53</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32391</th>
      <td>1/25/2012 1:32:32 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Brazil</td>
      <td>169-89467669-9328923</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32392</th>
      <td>12/14/2011 4:51:41 AM</td>
      <td>149-99118322-0835239</td>
      <td>Nossa Senhora da Conceição Aparecida</td>
      <td>zazzle_bag</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Brazil</td>
      <td>169-81662931-4781555</td>
      <td>1</td>
      <td>R$26.25</td>
      <td>10.0%</td>
      <td>R$2.63 BRL</td>
      <td>$1.24</td>
      <td>cleared</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32393</th>
      <td>12/10/2011 4:48:28 PM</td>
      <td>239-89217540-7970094</td>
      <td>Aparecida do Norte</td>
      <td>zazzle_postcard</td>
      <td>Yes</td>
      <td>No</td>
      <td>RicardoArtes</td>
      <td>NaN</td>
      <td>Brazil</td>
      <td>169-07034355-9170295</td>
      <td>2</td>
      <td>R$4.80</td>
      <td>20.0%+</td>
      <td>R$0.96 BRL</td>
      <td>$0.45</td>
      <td>cleared</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Vamos fazer o tratamento do restante dos dados. Com informações que tenho até aqui os dados
# em sua grande maioria foram tratados.
# Vamos automatizar a verificação do restante dos dados para constatar o estado atual:
# Eu desejo preliminarmente obter uma lista de países que ocorrem nos meus dados
# e a quantidade de linhas com erros.
```


```python
# Verificar o dataframe para checar quais linhas ainda apresentam erro.
# E verificar de vale a pena tratá-las.

# Armazena países válidos localizados.
paises_encontrados = set()
# Armazena as linhas que apresentam erros.
linhas_erro = []

for index, row in df.iterrows():
    pais = row['Shipped To']
    if pais in paises_validos:
        paises_encontrados.add(pais)
    else:
        linhas_erro.append(index)

# Numero de países válidos encontrados.
quantidade_paises_validos = len(paises_encontrados)
quantidade_linhas_erro = len(linhas_erro)

# Exibir resultados
print("Quantidade de países diferentes e válidos encontrados:", quantidade_paises_validos)
print("Quantidade de linhas com erros:", quantidade_linhas_erro)
print("Linhas que apresentam erro:", linhas_erro)

# Exibir lista com países válidos encontrados no dataframe.
print(" Países válidos econtrados no DataFrame:")
print(sorted(paises_encontrados))
```

    Quantidade de países diferentes e válidos encontrados: 47
    Quantidade de linhas com erros: 155
    Linhas que apresentam erro: [69, 108, 439, 773, 1033, 1322, 1591, 1760, 3119, 4088, 5207, 5208, 5209, 5210, 7763, 7802, 8515, 8729, 9219, 9567, 9568, 9569, 9570, 9571, 9572, 9573, 9579, 10444, 10573, 10698, 10785, 10904, 10905, 11080, 11285, 12089, 12182, 12848, 13084, 14275, 14446, 14447, 14449, 14693, 14958, 15140, 15169, 15324, 15496, 15566, 15568, 15569, 15597, 15769, 15770, 16418, 16958, 17132, 17327, 17328, 17553, 18573, 18885, 20154, 20262, 21467, 21923, 22264, 23018, 23100, 23259, 23260, 23261, 23262, 23263, 23264, 23265, 23266, 23267, 23856, 24022, 24069, 24593, 24623, 24670, 24824, 24825, 24826, 24827, 24828, 24829, 24830, 24831, 24832, 24833, 24834, 24835, 24836, 24837, 24838, 24839, 24840, 24841, 24842, 25518, 25743, 26021, 26022, 26023, 26024, 26216, 26217, 26959, 27584, 27585, 27586, 27587, 27588, 27589, 27590, 27591, 27592, 27593, 27594, 27595, 27596, 27597, 28025, 28118, 28127, 29714, 29911, 29912, 30272, 30377, 30467, 30488, 30611, 30640, 30684, 30726, 30745, 30746, 30858, 30958, 30961, 30987, 31094, 31614, 31615, 31634, 31709, 31970, 32225, 32261]
     Países válidos econtrados no DataFrame:
    ['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Croatia', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kenya', 'Kuwait', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mali', 'Mexico', 'Monaco', 'Morocco', 'Netherlands', 'New Zealand', 'Norway', 'Peru', 'Philippines', 'Portugal', 'Qatar', 'Singapore', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'United Arab Emirates', 'United Kingdom', 'United States']



```python
# Constatamos acima que possuímos uma lista de 47 países diferentes nos nossos dados.
# Constamos também que há um total de 155 linhas com erros.
# Vamos analizar se o custo de tratamento destas linhas restantes é viável.

# Informaçẽos sobre o dataframe.
df.shape
```




    (32394, 17)




```python
# Nossos dados apresentam um total de 32394 registros 
# Porcentagem=(155/32394)×100
# Logo :
# 0.478
# Então, 155 é aproximadamente 0.478% de 32.394 o que não representa
# um valor significativo para o total de registros.
# Logo, com o consentimento do gestor tomei a iniciativa de descartar esses dados da análise.
```


```python
# Processo de eliminação das linhas com erro:
# Vamos aproveitar aquela lista de linhas que apresentaram defeito.

indices_remocao = [69, 108, 439, 773, 1033, 1322, 1591, 1760, 3119, 4088, 5207, 5208, 5209, 5210, 7763, 7802, 8515, 8729, 9219, 9567, 9568, 9569, 9570, 9571, 9572, 9573, 9579, 10444, 10573, 10698, 10785, 10904, 10905, 11080, 11285, 12089, 12182, 12848, 13084, 14275, 14446, 14447, 14449, 14693, 14958, 15140, 15169, 15324, 15496, 15566, 15568, 15569, 15597, 15769, 15770, 16418, 16958, 17132, 17327, 17328, 17553, 18573, 18885, 20154, 20262, 21467, 21923, 22264, 23018, 23100, 23259, 23260, 23261, 23262, 23263, 23264, 23265, 23266, 23267, 23856, 24022, 24069, 24593, 24623, 24670, 24824, 24825, 24826, 24827, 24828, 24829, 24830, 24831, 24832, 24833, 24834, 24835, 24836, 24837, 24838, 24839, 24840, 24841, 24842, 25518, 25743, 26021, 26022, 26023, 26024, 26216, 26217, 26959, 27584, 27585, 27586, 27587, 27588, 27589, 27590, 27591, 27592, 27593, 27594, 27595, 27596, 27597, 28025, 28118, 28127, 29714, 29911, 29912, 30272, 30377, 30467, 30488, 30611, 30640, 30684, 30726, 30745, 30746, 30858, 30958, 30961, 30987, 31094, 31614, 31615, 31634, 31709, 31970, 32225, 32261]

# Remover as linhas indesejadas do dataframe e armazenar em um novo.
df_limpo = df.drop(indices_remocao, errors='ignore')
```


```python
# Vamos comparar os dados antes e após a remoção:
```


```python
# Antes da remoção:
df.shape
```




    (32394, 17)




```python
# Após a remocação:
df_limpo.shape
```




    (32239, 17)




```python
# Logo
# 32394 - 32239 = 155
# As 155 linhas com erros foram descartadas.
```


```python
# Vamos armazenar o novo dataframe em um arquivo diferente para trabalhar com ele mais a frente:
df_limpo.to_csv("DadosZazzleComTratamento.csv")
```


```python
# Vamos capturar os dados do novo arquivo para um dataframe.
df = pd.read_csv("DadosZazzleComTratamento.csv")
```


```python
# Vamos visulizar as linhas deste dataframe.
df.shape
```




    (32239, 18)




```python
pip install plotly==5.24.1 # Biblioteca para gerar gráficos.
```

    Collecting plotly==5.24.1
      Using cached plotly-5.24.1-py3-none-any.whl.metadata (7.3 kB)
    Collecting tenacity>=6.2.0 (from plotly==5.24.1)
      Using cached tenacity-9.0.0-py3-none-any.whl.metadata (1.2 kB)
    Requirement already satisfied: packaging in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from plotly==5.24.1) (24.1)
    Using cached plotly-5.24.1-py3-none-any.whl (19.1 MB)
    Using cached tenacity-9.0.0-py3-none-any.whl (28 kB)
    Installing collected packages: tenacity, plotly
    Successfully installed plotly-5.24.1 tenacity-9.0.0
    Note: you may need to restart the kernel to use updated packages.



```python
# Geração do mapa global.
# Importa as bibliotecas que vamos usar.
import pandas as pd
import plotly.express as px

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
# Exibe o gráfico.
fig.show()
```


<div>                            <div id="a55fd864-bdb1-4bb0-9d74-9a677e8e4e9a" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("a55fd864-bdb1-4bb0-9d74-9a677e8e4e9a")) {                    Plotly.newPlot(                        "a55fd864-bdb1-4bb0-9d74-9a677e8e4e9a",                        [{"coloraxis":"coloraxis","geo":"geo","hovertemplate":"Pais=%{location}\u003cbr\u003ePedidos=%{z}\u003cextra\u003e\u003c\u002fextra\u003e","locationmode":"country names","locations":["United States","Australia","Germany","Canada","Japan","United Kingdom","Netherlands","France","Belgium","Switzerland","Spain","Austria","Sweden","Brazil","New Zealand","Portugal","Italy","Singapore","Ireland","Luxembourg","Norway","Mexico","Hungary","United Arab Emirates","Peru","Israel","Greece","Malaysia","Monaco","Croatia","Argentina","Slovenia","Chile","Liechtenstein","Morocco","Jordan","Taiwan","Qatar","Kuwait","Finland","Colombia","Lithuania","Mali","Denmark","Egypt","Philippines","Kenya"],"name":"","z":[23692,1624,1368,1044,1010,770,548,492,475,302,258,177,131,111,79,25,25,20,16,10,7,7,5,5,3,3,3,3,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1],"type":"choropleth"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"geo":{"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"center":{}},"coloraxis":{"colorbar":{"title":{"text":"Pedidos"}},"colorscale":[[0.0,"rgb(150,0,90)"],[0.125,"rgb(0,0,200)"],[0.25,"rgb(0,25,255)"],[0.375,"rgb(0,152,255)"],[0.5,"rgb(44,255,150)"],[0.625,"rgb(151,255,0)"],[0.75,"rgb(255,234,0)"],[0.875,"rgb(255,111,0)"],[1.0,"rgb(255,0,0)"]]},"legend":{"tracegroupgap":0},"title":{"text":"N\u00famero de Pedidos por Pa\u00eds"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('a55fd864-bdb1-4bb0-9d74-9a677e8e4e9a');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
# Importa as bibliotecas que preciso para o gráfico.
import pandas as pd
import plotly.express as px

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

# Mostrar o gráfico
fig.show()

```


<div>                            <div id="bc58add3-7639-4017-9a62-dede18253fe5" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("bc58add3-7639-4017-9a62-dede18253fe5")) {                    Plotly.newPlot(                        "bc58add3-7639-4017-9a62-dede18253fe5",                        [{"alignmentgroup":"True","hovertemplate":"Pais=%{x}\u003cbr\u003ePedidos=%{marker.color}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"","marker":{"color":[23692,1624,1368,1044,1010,770,548,492,475,302],"coloraxis":"coloraxis","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"textposition":"auto","x":["United States","Australia","Germany","Canada","Japan","United Kingdom","Netherlands","France","Belgium","Switzerland"],"xaxis":"x","y":[23692,1624,1368,1044,1010,770,548,492,475,302],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Pa\u00eds"},"tickangle":-45},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"N\u00famero de Pedidos"}},"coloraxis":{"colorbar":{"title":{"text":"Pedidos"}},"colorscale":[[0.0,"rgb(150,0,90)"],[0.125,"rgb(0,0,200)"],[0.25,"rgb(0,25,255)"],[0.375,"rgb(0,152,255)"],[0.5,"rgb(44,255,150)"],[0.625,"rgb(151,255,0)"],[0.75,"rgb(255,234,0)"],[0.875,"rgb(255,111,0)"],[1.0,"rgb(255,0,0)"]]},"legend":{"tracegroupgap":0},"title":{"text":"Top 10 Pa\u00edses com Mais Pedidos"},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('bc58add3-7639-4017-9a62-dede18253fe5');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
# Geração do gráfico de pizza.

# Importa as bibliotecas que usaremos.
import pandas as pd
import plotly.express as px

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

# Exibe o gráfico.
fig.show()

```


<div>                            <div id="40093fec-8d63-4e37-a047-41d9cef7d9fd" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("40093fec-8d63-4e37-a047-41d9cef7d9fd")) {                    Plotly.newPlot(                        "40093fec-8d63-4e37-a047-41d9cef7d9fd",                        [{"customdata":[["United States"],["Australia"],["Germany"],["Canada"],["Japan"]],"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"hovertemplate":"Pais=%{customdata[0]}\u003cbr\u003ePedidos=%{value}\u003cextra\u003e\u003c\u002fextra\u003e","labels":["United States","Australia","Germany","Canada","Japan"],"legendgroup":"","marker":{"colors":["#636EFA","#EF553B","#00CC96","#AB63FA","#FFA15A"]},"name":"","showlegend":true,"values":[23692,1624,1368,1044,1010],"type":"pie"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"legend":{"tracegroupgap":0},"title":{"text":"Top 5 Pa\u00edses com Mais Pedidos"},"piecolorway":["#636EFA","#EF553B","#00CC96","#AB63FA","#FFA15A","#19D3F3","#FF6692","#B6E880","#FF97FF","#FECB52"]},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('40093fec-8d63-4e37-a047-41d9cef7d9fd');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
# Importar as bibliotecas necessárias
import pandas as pd
import plotly.express as px

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

# Mostrar o gráfico
fig.show()
```


<div>                            <div id="65531eb7-8645-4173-b56d-45c3e536b2be" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("65531eb7-8645-4173-b56d-45c3e536b2be")) {                    Plotly.newPlot(                        "65531eb7-8645-4173-b56d-45c3e536b2be",                        [{"hovertemplate":"Ano=%{x}\u003cbr\u003ePedidos=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"","line":{"color":"#636efa","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines+markers","name":"","orientation":"v","showlegend":false,"x":[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],"xaxis":"x","y":[2,47,638,1266,2403,3883,2830,3658,4999,3701,3596,3486,1288,442],"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Ano"},"tickmode":"linear"},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"N\u00famero de Pedidos"}},"legend":{"tracegroupgap":0},"title":{"text":"N\u00famero de Pedidos por Ano"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('65531eb7-8645-4173-b56d-45c3e536b2be');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
# Geração de relatório. Instale as bibliotecas abaixo para a geração do arquivo pdf.
```


```python
pip install pandas==2.2.2 plotly==5.24.1 reportlab==4.2.2 kaleido==0.2.1 # Instalação da biblioteca.
```

    Requirement already satisfied: pandas==2.2.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (2.2.2)
    Requirement already satisfied: plotly==5.24.1 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (5.24.1)
    Requirement already satisfied: matplotlib==3.9.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (3.9.2)
    Requirement already satisfied: reportlab==4.2.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (4.2.2)
    Requirement already satisfied: kaleido==0.2.1 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (0.2.1)
    Requirement already satisfied: numpy>=1.23.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from pandas==2.2.2) (2.1.1)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from pandas==2.2.2) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from pandas==2.2.2) (2024.2)
    Requirement already satisfied: tzdata>=2022.7 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from pandas==2.2.2) (2024.1)
    Requirement already satisfied: tenacity>=6.2.0 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from plotly==5.24.1) (9.0.0)
    Requirement already satisfied: packaging in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from plotly==5.24.1) (24.1)
    Requirement already satisfied: contourpy>=1.0.1 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from matplotlib==3.9.2) (1.3.0)
    Requirement already satisfied: cycler>=0.10 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from matplotlib==3.9.2) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from matplotlib==3.9.2) (4.53.1)
    Requirement already satisfied: kiwisolver>=1.3.1 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from matplotlib==3.9.2) (1.4.7)
    Requirement already satisfied: pillow>=8 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from matplotlib==3.9.2) (10.4.0)
    Requirement already satisfied: pyparsing>=2.3.1 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from matplotlib==3.9.2) (3.1.4)
    Requirement already satisfied: chardet in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from reportlab==4.2.2) (5.2.0)
    Requirement already satisfied: six>=1.5 in /home/leonardo/Jupyter/ambientes/padrao/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas==2.2.2) (1.16.0)
    Note: you may need to restart the kernel to use updated packages.



```python
import pandas as pd
df = pd.read_csv("DadosZazzleComTratamento.csv")
```


```python
# Geração do relatório
```


```python
# Geração do mapa global.
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
```

    Relatório Gerado.



```python

```


```python

```
