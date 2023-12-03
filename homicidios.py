import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Lectura del archivo
file = pd.ExcelFile('./homicidios.xlsx')
df = pd.read_excel(file, 'HECHOS')

# Generalidades
print("HEAD")
print(df.head())

print("COLUMNS")
columnas = df.columns.to_list()
print(columnas)

print("DESCRIBE")
print(df.describe().T)

print("SHAPE")
print(df.shape)

#Limpieza y depuración
print("IS NULL")
print(df.isna().sum)

df = df.drop_duplicates(subset=['ID'])
df = df.drop_duplicates(subset = None, keep = 'first')
print(df.shape)

#Analisis y visualizacion

# Gráfico de barras de PARTICIPANTES
plt.figure(figsize=(10, 6))
df['PARTICIPANTES'].value_counts().plot(kind='bar', color='green')
plt.title('Gráfico de barras de PARTICIPANTES')
plt.xlabel('Número de Participantes')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de barras de VICTIMAS
plt.figure(figsize=(10, 6))
df['VICTIMA'].value_counts().plot(kind='bar', color='lightblue')
plt.title('Gráfico de barras de VICTIMAS')
plt.xlabel('Número de Victimas')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de barras de ACUSADO
plt.figure(figsize=(10, 6))
df['ACUSADO'].value_counts().plot(kind='bar', color='coral')
plt.title('Gráfico de barras de ACUSADO')
plt.xlabel('Número de Acusado')
plt.ylabel('Frecuencia')
plt.show()

# Distribución de n victimas (Histograma)
plt.figure(figsize=(10, 6))
sns.histplot(df['N_VICTIMAS'], bins=30, kde=True, color='skyblue')
plt.title('Distribución de Número de Víctimas')
plt.xlabel('Número de Víctimas')
plt.ylabel('Frecuencia')
plt.show()

# Distribución de casos por comunas (Gráfico de Barras)
plt.figure(figsize=(12, 6))
sns.countplot(x='COMUNA', data=df, order=df['COMUNA'].value_counts().index, color='pink')
plt.title('Distribución de Incidentes por Comuna')
plt.xlabel('Comuna')
plt.ylabel('Número de Incidentes')
plt.show()

# Análisis temporal (cdad incidentes a lo largo del tiempo)
df['FECHA'] = pd.to_datetime(df['FECHA'])
df.set_index('FECHA', inplace=True)
incidentes_temporales = df.resample('M').size() #Reagrupo por mes
plt.figure(figsize=(12, 6))
incidentes_temporales.plot(title='Cantidad de incidentes a lo largo del tiempo', color='orange')
plt.xlabel('Fecha')
plt.ylabel('Número de Incidentes')
plt.show()

# Mapa de Calor de Participantes vs. Número de Víctimas
plt.figure(figsize=(10, 8))
sns.heatmap(pd.crosstab(df['PARTICIPANTES'], df['N_VICTIMAS']), cmap='Blues', annot=True, fmt='d')
plt.title('Mapa de Calor de Participantes vs. Número de Víctimas')
plt.xlabel('Número de Víctimas')
plt.ylabel('Número de Participantes')
plt.show()
