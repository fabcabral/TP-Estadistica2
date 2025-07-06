import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, ttest_ind, shapiro, levene
from statsmodels.stats.proportion import proportions_ztest

# 1. Carga de datos
df = pd.read_csv('C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/Diatraea.csv')
print(df.head())
print(df.columns)

# 2. Crear variable binaria de daño: dañada si % tallos infestados > 0
# (puedes ajustar el umbral si corresponde)
df['Danada'] = (df['% tallos infestados'] > 0).astype(int)

# Tabla de contingencia: dañada vs no dañada
tab = df['Danada'].value_counts().sort_index()
print('\nTabla de plantas dañadas (0=No, 1=Sí):')
print(tab)

# Test de proporciones: ¿proporción de dañadas difiere de 0.5?
count = tab[1] if 1 in tab else 0
nobs = tab.sum()
stat, pval = proportions_ztest(count, nobs, value=0.5, alternative='two-sided')
print(f'\nTest de proporciones vs 0.5: z = {stat:.4f}, p-valor = {pval:.4f}')

# 3. Comparación de medias de peso entre dañadas y no dañadas
peso_danada = df[df['Danada'] == 1]['peso']
peso_no_danada = df[df['Danada'] == 0]['peso']

# Chequeo de supuestos
print('\nChequeo de normalidad:')
print('Dañada:', shapiro(peso_danada))
print('No dañada:', shapiro(peso_no_danada))
print('\nChequeo de igualdad de varianzas:')
print(levene(peso_danada, peso_no_danada))

# Test t para medias independientes
# H0: peso igual; H1: menor peso en dañadas
stat_t, pval_t = ttest_ind(peso_danada, peso_no_danada, equal_var=True, alternative='less')
print(f'\nTest t: t = {stat_t:.4f}, p-valor = {pval_t:.4f}')

# 4. Visualización
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.bar(['No dañada', 'Dañada'], [tab[0] if 0 in tab else 0, tab[1] if 1 in tab else 0], color=['green','red'])
plt.ylabel('Número de plantas')
plt.title('Plantas dañadas vs no dañadas')
plt.subplot(1,2,2)
plt.boxplot([peso_no_danada, peso_danada], patch_artist=True)
plt.xticks([1,2], ['No dañada', 'Dañada'])
plt.ylabel('Peso (g)')
plt.title('Peso de mazorca según daño')
plt.tight_layout()
plt.show() 