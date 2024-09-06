import pandas as pd
import matplotlib.pyplot as plt

# Criando DataFrame:
dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
venda = [5.11, 4.99, 5.02, 5.21, 5.07, 5.09, 5.13, 5.12, 4.94, 5.03]
gasolina = pd.DataFrame({'Dias': dias, 'Vendas': venda })

# Criando arquivo CSV:
gasolina.to_csv('gasolina.csv', index=False)

# Criando gráfico:
dados = pd.read_csv('gasolina.csv')
grafico = dados.plot(kind= 'line', x='Dias', y='Vendas', title='Preço da gasolina')
plt.show()

# Salvando grafico em PNG
grafico.figure.savefig('gasolina.png', dpi=300)