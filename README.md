# SAT-homicidios
SAT - Fundamentos del desarrollo en software y analisis de datos en Python
## Análisis de datos exploratorio (EDA)
### Problemática a analizar
En la Ciudad Autónoma de Buenos Aires (CABA), la tasa de mortalidad relacionada con incidentes viales es un número que se desea reducir teniendo en cuenta que pueden ser situaciones evitables. Es necesario para esto identificar patrones, factores de riesgo y áreas geográficas con mayor incidencia. El objetivo es entender las situaciones de los accidentes viales con el objetivo de implementar medidas efectivas de prevención y mejorar la seguridad vial de la ciudad.

### Exploración del dataset
Se utilizó un dataset de CABA que contiene información de los accidentes viales y sus variables asociadas: temporales, espaciales y participantes. \
Este dataset contiene 696 filas y 21 columnas. Estas columnas son:
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

Aclaración:
'PASAJEROS' hace referencia unicamente a personas lesionadas que se encuentran dentro, descendiendo o ascendiendo de las unidades de autotrasporte público de pasajeros/as y ómnibus de larga distancia.

### Limpieza y preparación del dataset
Primero se explora la cantidad de valores faltantes en cada columna. Las columnas 'Altura' y 'Cruce' tienen 567 y 171 valores faltantes respectivamente por lo que se decide eliminarlas ya que no se consideran significativas al análisis en cuestión.\
Luego se verifica la existencia de filas duplicadas en el dataset y se comprueba que no existen duplicados.\
A continuación se eliminan las filas que contienen valores 'SD' (sin datos) ya que estas introducen información inconsistente al dataset.\
Por ultimo, se convierten las columnas a su tipo de dato correspondiente, ya que una gran parte de ellas tenian 'object; como data type. Por esto se realizaron las siguientes conversiones:
* Las columnas 'VICTIMA', 'PARTICIPANTES', 'ACUSADO', 'TIPO_DE_CALLE' y 'COMUNA' se convierten a variables categóricas ya que solo pueden tomar una cantidad limitada de valores posibles.
* La columna 'HH' fue convertida a variable de tipo entero
* Las columnas 'Calle', 'LUGAR_DEL_HECHO' y 'Dirección Normalizada' fueron convertidas a variables de tipo string
* Las columnas 'pos x' y 'pos y' fueron convertidas a variables de tipo float
### Análisis y visualización de datos
#### Funciones definidas previo al análisis
Para comenzar con el análisis y visualización de datos, primero se definieron 5 funciones para crear los gráficos correspondientes para el análisis.\
1. `grafico_de_barras`: recibe como parametros la columna con la cual se realiza el gráfico, el color y si se quiere o no que las variables del eje x esten escritas verticales o horizontales (esto dependerá de la cantidad de la cantidad de variables de la columna). Devuelve el gráfico de barras para la columna analizada, realizando un análisis frecuencial de una variable categórica.
2. `grafico_de_tortas`: recibe como parametros la columna con la cual se realiza el gráfico, y los colores que tenga el mismo. La función devuelve el gráfico en cuestión con el porcentaje de cada opción de valor de la columna en cuestión.
3. `analisis_temporal`: esta función se realizó para realizar el analisis temporal de los incidentes mensual y anual. La función recibe como parámetros el dataframe, la fecha (FECHA_MES o FECHA_ANO), M o Y (para realizar el resample) y el color del gráfico. Esta función va a devolver un gráfico con la cantidad de incidentes a lo largo del tiempo (mensual o anual)
4. `relacion_entre_dos_col`: recibe como parametros dos columnas a las cuales se quiere evaluar la relación mediante un heatmap para ver si hay alguna opción de la columna 1 que afecta o se relaciona más o menos con una opción de la columna 2.
#### Análisis temporal
Al graficar la cantidad de incidentes a lo largo de tiempo agrupando las fechas por mes, se puede visualizar que no hay una tendencia en específica sino que suceden más bien aleatoramiente. Lo que si se puede notar es un pico abrupto en el año 2020, y que los valores más bajos ocurren entre el 2020 y 2021, que justamente en la época de la pandemia del COVID 2019, y el hecho de estar en cuarentena, redujo la cantidad de circulación, reduciendo así los incidentes viales. Esto también puede notarse al agrupar las fechas por año.\ Continuando con un análisis del día de la semana en los cuales ocurren los incidentes, se puede notar que no hay un día de la semana que muestre una mayor cantidad de accidentes significativos. El jueves posee un 13,6% de cantidad de incidentes con el porcentaje mínimo, mientras que el lunes presenta un porcentaje de 15,3% de incidentes dicho día como porcentaje máximo. Se podría esperar que la mayor parte de los incidentes ocurra durante los fines de semana, pero los datos muestran que los incidentes ocurren independientmente del dia de la semana.\
Se decidió agrupar también los incidentes por grupo horario para evaluar si hay una cierta franja horaria donde ocurren los incidentes. Para eso se agruparon los horarios en 4 grupos:
1. De 24hs-7hs (Madrugada)
2. De 7hs-13hs (Mañana)
3. De 13hs-19hs (Tarde)
4. De 19hs-24hs (Noche).\
\
Los resultados fueron que en la mayor parte de los casos (32,48%), los accidentes ocurren entre las 24hs y 7hs, en segundo lugar con un (26,34%) en la franja horaria de la tarde, luego la franja horaria de la mañana (25%) y por último la franja de noche (16%).
#### Análisis espacial
##### Tipo de calle
Se realizó un gráfico de tipo torta para evaluar la distribución de los accidentes en los tipos de calle, siendo los valores posibles: 'Avenida', 'General Paz', 'Calle' y 'Autopista'.\
Como resultado se pudo observar que una gran mayoria de los accidentes (62.6%) suceden en avenidas, seguido en mucho menor medida por calle, autopista y general paz.
##### Comuna
Se decidió tambien investigar que comuna de CABA tuvo la mayor frecuencia de accidentes viales. Realizando un gráfico de barras se observó que las comunas con mayor frecuencia de incidentes son la 1 (Puerto Madero, Retiro, Montserrat, Constitución), 4 (Parque Patricios y Barracas) y 9 (Mataderos). La comuna con mayor frecuencia es la comuna 6, compuesta por el barrio de Caballito.\
Se agregó un mapa de las comunas para mayor claridad.
#### Análisis de involucrados
##### Participantes
Se realizó un gráfico de barras para observar quienes eran los participantes mas frecuentes de los accidentes viales. Estos son en primer lugar peaton y pasajeros, en segundo lugar moto y auto y en tercer lugar moto y cargas (camión de cargas).
##### Víctimas
Se utilizó un gráfico de barras para ver las víctimas más frecuentes de los accidentes viales en el dataset. Estos son en primer lugar moto, luego peatón y en tercer lugar auto.
##### Acusado
Luego se analizó la columna 'ACUSADO' descrita como 'Vehículo que ocupaba quien resultó acusado/a del hecho, sin implicar culpabilidad legal'. Esta resulto ser en primer lugar auto, en segundo lugar pasajero y en tercer lugar cargas.
#####  Numero de víctimas
Se comenzó con un gráfico de barras para analizar el numero de victimas en los incidentes. Se vio que en la gran mayoria de los casos (648), se tiene una sola víctima en el incidente, en 19 casos hubo 2 víctimas y en un solo caso se tuvo 3 víctimas.
### Conclusiones
Una vez realizado el análisis y la visualización de los datos, se procede a extraer conclusiones con el fin de abordar la problemática planteada. \
Con respecto al análisis temporal, no se identificó una tendencia clara en la frecuencia de incidentes a lo largo del tiempo, pero se destacó un pico abrupto en el año 2020, posiblemente relacionado con las restricciones de movilidad durante la pandemia de COVID-19. Tampoco se encontró una tendencia para ningun dia particular de la semana. Con respecto al análisis por franjas horarias, hubo una distribución bastante homogenea entre todas. La menor frecuencia se dio en la franja horaria de 19-24. Cabe destacar que la diferencia no es tan significativa, pero tiene sentido pensar que en la franja horaria de la noche las personas ya terminaron su día, se encuentran en sus casas y por ende hay menos circulación de autos dando a lugar a menos indicdentes viales. Hubo una frecuencia levemente mayor para el horario de madrugada, lo que puede sugerir la posibilidad de comportamientos de riesgo asociados, como la influencia de sustancias o la fatiga. Para esto se propone un aumento de controles en estas horas. Es un enfoque preventivo que puede ayudar a la disminución de siniestros viales.\
Luego se realizó el análisis espacial, que dio lugar a una serie de descubrimientos. En primer lugar, en más de la mitad de los casos los accidentes se dieron en autopistas. La siguiente es calle, con una diferencia significativa. Además, se observó que las cimunas con mayor incidencia de accidentes son la 1 la 4 y la 9. Se podría proponer entonces una mayor cantidad de camarás de velocidad en las avenidas, con el fin de que los conductores se vieran obligados a reducir la velocidad y se eviten accidentes. Es necesario un análisis más profundo para evaluar la razón porque las comunas 1, 4 y 9 tienen mayor frecuencia de accidentes, pero es posible que el aumento de controles de transito ayude a evitar accidentes. \
Por último, se analizó a los individuos involucrados en estos accidentes. Es interesante observar que las víctimas más frecuentes son los individuos en motos, ya que no se corresponden con los participantes más frecuentes (que son pasajeros y peatón). Por esto es necesario reforzar las medidas de seguridad para los individuos que utilizan motos, por ejemplo implementando un control estricto en el uso de cascos y la utilización de un carril de la calle y no el manejo entre estos.
