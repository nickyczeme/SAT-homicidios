# SAT-homicidios
Entrega del SAT - Fundamentos del desarrollo en software y analisis de datos en Python

## Problemática a analizar
En la Ciudad Autónoma de Buenos Aires (CABA), la tasa de mortalidad relacionada con incidentes viales es un número que se desea reducir teniendo en cuenta que pueden ser situaciones evitables. Es necesario para esto identificar patrones, factores de riesgo y áreas geográficas con mayor incidencia. El objetivo es entender las situaciones de los accidentes viales con el objetivo de implementar medidas efectivas de prevención y mejorar la seguridad vial de la ciudad.

## Análisis de datos
### Exploración del dataset
Se utilizo un dataset de CABA que contiene información de los accidentes viales y sus variables asociadas: temporales, espaciales y participantes. \
Este dataset contiene 696 filas y 21 columnas. Estas columnas son:\
* ID
* N_VICTIMAS
* FECHA
* AAAA
* MM
* DD
* HORA
* HH
* LUGAR_DEL_HECHO
* TIPO_DE_CALLE
* Calle
* Altura
* Cruce
* Dirección Normalizada
* COMUNA
* XY (CABA)
* pos x
* pos y
* PARTICIPANTES
* VICTIMA
* ACUSADO

### Limpieza y preparación del dataset
Primero se explora la cantidad de valores faltantes en cada columna. Las columnas 'Altura' y 'Cruce' tienen 567 y 171 valores faltantes respectivamente por lo que se decide eliminarlas ya que no se consideran significativas al análisis.\
Luego se verifica la existencia de filas duplicadas en el dataset y se comprueba que no existen duplicados.\
A continuación se eliminan las filas que contienen valores 'SD' (sin datos) ya que estas introducen información inconsistente al dataset.\
Por ultimo, se convierten las columnas a su tipo de dato correspondiente, por ejemplo las columnas 'VICTIMA', 'PARTICIPANTES', 'ACUSADO', 'TIPO_DE_CALLE' y 'COMUNA' se convierten a variables categóricas ya que solo pueden tomar una cantidad limitada de valores posibles.
### Análisis y visualización de datos
### Conclusiones
