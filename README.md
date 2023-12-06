# SAT-homicidios
SAT - Fundamentos del desarrollo en software y analisis de datos en Python
## Análisis de datos exploratorio (EDA)
### Problemática a analizar
En la Ciudad Autónoma de Buenos Aires (CABA), la tasa de mortalidad relacionada con incidentes viales es un número que se desea reducir teniendo en cuenta que pueden ser situaciones evitables. Es necesario para esto identificar patrones, factores de riesgo y áreas geográficas con mayor incidencia. El objetivo es entender las situaciones de los accidentes viales con el objetivo de implementar medidas efectivas de prevención y mejorar la seguridad vial de la ciudad.

### Exploración del dataset
Se utilizó un dataset de CABA que contiene información de los accidentes viales y sus variables asociadas: temporales, espaciales y participantes. \
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
Primero se explora la cantidad de valores faltantes en cada columna. Las columnas 'Altura' y 'Cruce' tienen 567 y 171 valores faltantes respectivamente por lo que se decide eliminarlas ya que no se consideran significativas al análisis en cuestión.\
Luego se verifica la existencia de filas duplicadas en el dataset y se comprueba que no existen duplicados.\
A continuación se eliminan las filas que contienen valores 'SD' (sin datos) ya que estas introducen información inconsistente al dataset.\
Por ultimo, se convierten las columnas a su tipo de dato correspondiente, por ejemplo las columnas 'VICTIMA', 'PARTICIPANTES', 'ACUSADO', 'TIPO_DE_CALLE' y 'COMUNA' se convierten a variables categóricas ya que solo pueden tomar una cantidad limitada de valores posibles. 
### Análisis y visualización de datos
#### Funciones definidas previo al análisis
Para comenzar con el análisis y visualización de datos, primero se definieron 5 funciones para crear los gráficos correspondientes para el análisis.\
1. `grafico_de_barras`: recibe como parametros la columna con la cual se realiza el gráfico, el color y si se quiere o no que las variables del eje x esten escritas verticales o horizontales (esto dependerá de la cantidad de la cantidad de variables de la columna). Devuelve el gráfico de barras para la columna analizada, realizando un análisis frecuencial de una variable categórica.
2. `grafico_de_tortas`: recibe como parametros la columna con la cual se realiza el gráfico, y los colores que tenga el mismo. La función devuelve el gráfico en cuestión con el porcentaje de cada opción de valor de la columna en cuestión.
3. `analisis_temporal`: esta función se realizó para realizar el analisis temporal de los incidentes mensual y anual. La función recibe como parámetros el dataframe, la fecha (FECHA_MES o FECHA_ANO), M o Y (para realizar el resample) y el color del gráfico. Esta función va a devolver un gráfico con la cantidad de incidentes a lo largo del tiempo (mensual o anual)
4. `relacion_entre_dos_col`: recibe como parametros dos columnas a las cuales se quiere evaluar la relación mediante un heatmap para ver si hay alguna opción de la columna 1 que afecta o se relaciona más o menos con una opción de la columna 2. 
####  Numero de víctimas
Se comenzó con un gráfico de barras para analizar el numero de victimas en los incidentes. Se vio que en la gran mayoria de los casos (648), se tiene una sola víctima en el incidente, en 19 casos hubo 2 víctimas y en un solo caso se tuvo 3 víctimas.
#### Análisis temporal
Al graficar la cantidad de incidentes a lo largo de tiempo agrupando las fechas por mes, se puede visualizar que no hay una tendencia en específica sino que suceden más bien aleatoramiente. Lo que si se puede notar es un pico abrupto en el año 2020, y que los valores más bajos ocurren entre el 2020 y 2021, que justamente en la época de la pandemia del COVID 2019, y el hecho de estar en cuarentena, redujo la cantidad de circulación, reduciendo así los incidentes viales. Esto también puede notarse al agrupar las fechas por año.\ Continuando con un análisis del día de la semana en los cuales ocurren los incidentes, se puede notar que no hay un día de la semana que muestre una mayor cantidad de accidentes significativos. El jueves posee un 13,6% de cantidad de incidentes con el porcentaje mínimo, mientras que el lunes presenta un porcentaje de 15,3% de incidentes dicho día como porcentaje máximo. Se podría esperar que la mayor parte de los incidentes ocurra durante los fines de semana, pero los datos muestran que los incidentes ocurren independientmente del dia de la semana.\
Se decidió agrupar también los incidentes por grupo horario para evaluar si hay una cierta franja horaria donde ocurren los incidentes. Para eso se agruparon los horarios en 4 grupos:
1. De 24hs-7hs (Madrugada)
2. De 7hs-13hs (Mañana)
3. De 13hs-19hs (Tarde)
4. De 19hs-24hs (Noche)
Los resultados fueron que en la mayor parte de los casos (32,48%), los accidentes ocurren entre las 24hs y 7hs, en segundo lugar con un (26,34%) en la franja horaria de la tarde, luego la franja horaria de la mañana (25%) y por último la franja de noche (16%). Cabe destacar que la diferencia no es tan significativa, pero tiene sentido pensar que en la franja horaria de la noche las personas ya terminaron su día, se encuentran en sus casas y por ende hay menos circulación de autos dando a lugar a menos indicdentes viales.
### Conclusiones
