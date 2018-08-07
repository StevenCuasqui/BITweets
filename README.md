## Participantes

- Steven Cuasqui
- Andrés Velasco

## Método

* Adquisición de datos

La adquisición de los datos para el presente trabajo se realizó utilizando un cosechador de tweets con las credenciales de desarrollador en Twitter desarrollado en Python y entregado por medio del aula virtual. Los tweets se almacenan en CouchDB, una base de datos NoSQL, en Ubuntu. Para esto, el script requiere las coordenadas de la ubicación geográfica en formato CSV y la base de datos de CouchDB para almacenar los tweets recolectados.

Como resultado, se tienen 20 bases de datos con los datos de los tweets correspondientes a los paises participantes de la Copa Mundial de la FIFA Rusia 2018. Los tweets fueron recolectados en el horario correspondiente a los partidos de las selecciones desde el 28 de Junio del 2018 hasta el 15 de Julio del mismo año. Las bases de datos en CouchDB son las siguientes, con sus nombres exactos: argentina, belgica, brasil, colombia, croacia, dinamarca, espana, francia, inglaterra, japon, mexico, panama, polonia, portugal, rusia, senegal, suecia, suiza, tunez y uruguay.

* Preprocesamiento

Para el preprocesamiento, se requiere filtrar el campo de texto de los tweets obtenidos para eliminar  caracteres especiales, links, tags, etc. Este filtrado es realizado en el script de Python que solo reconoce caracteres alfanúmericos dentro del campo de texto en los tweets. El filtrado se realiza utilizando expresiones regulares y para el presente trabajo se establece el reconocimiento con la siguiente expresión: ^[a-zA-Z 0-9,.;#@\'\"&?$%()-+!]*$ . De esta manera, se recuperan solamente los caracteres alfanumericos para poder realiza un análisis de opinión pública sobre el mundial sin que se recuperen los caracteres especiales, url’s o hashtags.

* Procesamiento

Para el procesamiento, se requiere obtener el campo texto de los tweets y con esto determinar la opinión publica respecto al mundial. La obtención de los tweets de la copa de la FIFA Rusia 2018 se realiza filtrando los mismos con los hashtags del evento y de las selecciones involucradas en los partidos. Estos hashtags dependen de las selecciones involucradas en los partidos y son #WorldCup, #Rusia2018, #WordCup2018, #Russia2018, #ARG, #AUS, #BEL, #BRA, #COL, #CRC, #CRO, #DEN, #EGY, #ENG, #ESP, #FRA, #GER, #IRN, #ISL, #JPN, #KOR, #KSA, #MEX, #MAR, #NGA, #PAN, #PER, #POL, #POR, #RUS, #SEN, #SRB, #SUI, #SWE, #TUN y #URU. 

Para el procesamiento de los tweets, se realiza el análisis de sentimiento con un script en Python que obtiene de una vista, filtrada de la manera anteriormente indicada, el campo del texto del tweet y mediante la utilización de la librería de TextBlob establece un valor de polaridad que sirve para etiquetar al texto como positivo, negativo o neutro. De esta manera, se obtiene un arreglo de objetos en formato JSON en donde se identifican el texto del tweet con el nombre “text” y a su clasificación con el nombre “label”. 

* Análisis

El análisis en el presente trabajo involucra la presentación de la información de tweets por hora del día, por fecha, por ubicación geográfica, por idiomas, por país, porcentaje de sentimientos sobre el mundial y tweets relacionados al mundial por país.

Para el análisis de tweets por hora del día, se genera una vista mediante el código en Javascript donde se emite la hora del día con el texto del respectivo tweet. Con esta hora del día es posible generar las estadísticas sobre los tweets generados sobre un partido durante todo el día que este se juega.

Para el análisis por fecha, se genera una vista mediante Javascript que contiene la fecha y el texto de los tweets del partido a analizar; de esta manera, se genera la estadística con un script en Python sobre las fechas y la cantidad de tweets generados por los usuarios sobre cada partido.

Para el análisis de la ubicación geográfica, se genera una vista mediante Javascript que contiene las coordenadas desde donde los tweets fueron generados; de esta manera, se obtiene la cantidad de tweets por ubicación y mediante un script en Python genera un archivo .kml que sirva para la generación del mapa de calor en Google Fusion Tables.

Para el análisis del idioma, se genera una vista mediante Javascript que contiene el campo de idioma que cada tweet tiene; de esta forma, se obtiene la cantidad de tweets por idioma con script en Python y se genera la estadística correspondiente. 

Para el análisis de sentimientos, se utiliza una vista mediante Javascript con el contenido del campo texto del tweet y que corresponden a tweets del mundial, filtrados por los hashtagas oficiales previamente descritos. De esta manera, con un script en Python se etiqueta cada tweet con TextBlob para obtener el sentimiento en cada tweet. A continuación, se recuperan los tweets ya etiquetados para generar la estadística sobre los sentimientos correspondiente.

* Presentación

La presentación de los resultados para cada ítem descrito en el apartado de Análisis se realiza a manera de gráficos de barras, gráficos pastel y mapa de calor. Estas presentaciones sirven para mostrar de manera más sencilla los resultados obtenidos del desarrollo del presente trabajo.

## Resultados

    • Se observa durante el análisis de sentimientos, los gráficos muestran un alto índice de tweets neutrales, principalmente en los países europeos. Con lo cual se puede llegar a la relativa idea que el mundial de futbol no es tan relevante para esta región.
    • La gran mayoría de los tweets recopilados, fueron emitidos dentro de las grandes urbes de los países analizados.
    • La cantidad de tweets contabilizados durante los partidos es superior a los generados fuera de los horarios de estos, con esto se puede determinar la atracción que genera un encuentro de fútbol en el mundial de la FIFA.

## Conclusiones y trabajo futuro

Bajo el telón tecnológico de las redes sociales, se encuentran twitter, Facebook.. que, gracias a sus herramientas basadas en servicios web, ha facilitado el trabajo de los analistas de datos. Por lo tanto, con una gran capacidad computacional y toda la gran cantidad de información que se podrá obtener fácilmente en un futuro cercano. Con lo cual favorecerán al mercado, gracias al avanzado minado de opinión que se podrá obtener.

Las organizaciones interesadas en conocer la opinión pública de un grupo en específico encuentra en los análisis desarrollados en el presente trabajo una herramiente capaz de proporcionar información útil y que permite mejorar la competitividad de sus servicios o productos de acuerdo a la reacción del público.

Para el futuro, se tiene pensado implementar un clasificador basado en deep-learning, el cual ya se lo ha implementado, aunque su precision no es muy aceptable.

## Apéndice

Apéndice A. Comandos para compilación de scripts Python.

Los siguientes comandos deben ser ejecutados en la ubicación de los scripts en Python.
Generar coordenadas kml $python get_kml.py <pais> 
Generar grafico de barras por hora $python barras.py <partido> <operacion> --> (horas, lang) 
Diagrama de pastel: $python pastel.py <pais>
