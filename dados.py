import pandas as pd
import numpy as np

df = pd.read_excel('dataset.xlsx')

print(df.to_string())

filtro = df[df['Site'] == "SCTIO05"]
print(filtro)

#df['Status'] = 'NaN'
#print(df)

df['Staus'] = np.where(df['Quality'] >=  75, 'OK', 'NOK' )
#print(df)

# converter a coluna Data para o tipo de dados datetime
df['Date'] = pd.to_datetime(df['Date'])
 
# ordenar pela coluna Data em ordem decrescente
df.sort_values('Date', ascending=False, inplace=True)
print("Ordenado")
print(df)

#resultado = titanic[[]]

df.to_excel('relatorio_qualidade.xlsx')