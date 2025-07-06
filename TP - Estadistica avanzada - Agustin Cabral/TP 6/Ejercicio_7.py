import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar datos
datos = pd.read_csv(r'C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/latinoam.csv')

# 1. Descripción univariada
describe = datos.describe(include='all')
print('Descripción univariada:')
print(describe)
print('\n¿Hay datos faltantes?')
print(datos.isnull().any())
print('Cantidad de datos faltantes por columna:')
print(datos.isnull().sum())

# 2. Matriz de correlación
print('\nMatriz de correlación:')
cor_matrix = datos.corr(numeric_only=True)
print(cor_matrix)

# 2. Matriz de diagramas de dispersión (solo las 4 primeras variables numéricas)
num_cols = list(datos.select_dtypes(include=[np.number]).columns[:4])
print(f'Generando pairplot solo para las variables: {num_cols}')
sns.pairplot(datos[num_cols])
plt.suptitle('Matriz de diagramas de dispersión (variables seleccionadas)', y=1.02)
plt.show()

# 3. Variables más asociadas
print('\nVariables más asociadas (correlaciones más altas en valor absoluto):')
cor_abs = cor_matrix.abs().where(~np.eye(cor_matrix.shape[0],dtype=bool))
max_corr = cor_abs.unstack().order(ascending=False).dropna().head(5) if hasattr(cor_abs.unstack(), 'order') else cor_abs.unstack().sort_values(ascending=False).dropna().head(5)
print(max_corr)

# 4. Outliers bivariados
print('\nPara identificar outliers bivariados, revisar visualmente los gráficos de dispersión generados arriba.') 