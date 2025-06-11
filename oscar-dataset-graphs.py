#Primeiro gráfico - colunas

#importando bibliotecas

import matplotlib.pyplot as plt;
import numpy as np

#importando dados

nomes = ('Meryl Streep','Katharine Hepburn','Bette Davis','Spencer Trazy','Paul Newman',
         "Peter O'Toole",'Laurence Olivier','Jack Nicholson','Jack Lemmon','Greer Garson')
indice = np.arange(len(nomes))
indicações = [17,12,11,9,8,8,8,8,7,7]

#plotando arquivos

plt.bar(indice,indicações, color = 'gold')
plt.xticks(indice,nomes , rotation=45)
plt.ylabel('Indicações')
plt.title('10 atores com mais indicações ao Oscar de Melhor Ator')

plt.show()

#Segundo gráfico - pizza

labels = 'Feminino','Masculino'
sizes = [6,4]
colors = ['Red','Blue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle = 90)

plt.axis('equal')
plt.title('Gênero dos 10 Atores com Mais Vitórias no Oscar')

plt.show()

#Terceiro gráfico - linha

from pandas import read_csv
from matplotlib.pyplot as plt

series = read_csv(r"C:\Users\Raquel\Documents\Aula de visualização de dados\trabalho\csv grafico de linha\Quantidade de Categorias do Oscar ao Longo da História.csv",
                  header=0, 
                  index_col=0, )

series.plot()
plt.title('Quantidade de Filmes Indicados ao Oscar por Ano')
plt.show()