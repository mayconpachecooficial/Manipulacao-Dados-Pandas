# 1. Importar a biblioteca pandas
import pandas as pd

# 2. Carregar os dados
# Substitua 'caminho_para_seu_arquivo.csv' pelo caminho real do seu arquivo
df = pd.read_csv('caminho_para_seu_arquivo.csv')

# 3. Manipular dados
# Por exemplo, selecionar colunas específicas e renomear uma coluna
df_selecionado = df[['Coluna1', 'Coluna2']].rename(columns={'Coluna1': 'NovaColuna1'})

# Tratar dados faltantes (exemplo: preencher valores faltantes com 0)
df_selecionado.fillna(0, inplace=True)

# 4. Combinar dados (se necessário)
# Se você tiver outro DataFrame df2 que deseja combinar com df_selecionado
# df_combinado = pd.merge(df_selecionado, df2, on='coluna_comum', how='inner')

# 5. Outras funções úteis
# Agrupamento de dados por 'NovaColuna1' e cálculo da média de 'Coluna2'
resultado_agrupamento = df_selecionado.groupby('NovaColuna1')['Coluna2'].mean()

# Exibir o resultado do agrupamento
print(resultado_agrupamento)
