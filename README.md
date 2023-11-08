
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

<div align = "center">
<a href=""><img src="/img/accidentes.jpg" width="100%"></a>

# [Proyecto Analisis de Datos ](#)
  
# [Visualizacion con Power Bi :chart_with_upwards_trend:, crear historia a partir de los datos :memo:  ](#)
<H2> :point_down: Podes encontrar el Tablero aca! ✈️</H2>

:city_sunrise: [Tablero](https://drive.google.com/file/d/1k6ldkvm6nfUKWD5xpG3PUXJKG7y2L__m/view?usp=sharing) - Power bi 

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

## Table of Contents

</br>

| | Table Of Contents |
|--|----------------|
| 1 | [About](#About)  |
| 2 | [Setup](#setup)  | 
| 3 | [Consultas_SQL](#Consultas_SQL)  | 


</div>

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

## Directory Structure

```js
├── jupyter
│   ├── Exploracion de datos_AccidentesAviones.py  
│ 
├── Limpieza_y_transformacion_de_datos
│   ├──funciones_py.py
│   ├──Transformar_datos_de_accidentes.py
│
├──.Crear_db_SQLite_y_consultas.py   
└── README.md
```

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>
  
******************************************************************************
<div>

## About

<div align = "center">
<img src="/img/1.jpg" width="100%">Cruzar con otra fuente de datos, realizar el tablero en Power bi, redactar una historia con los datos.
Para cruzar datos con otras fuentes utilizo los datos que provee la web www.macrotrends.net/.
</div>
<div align = "center">
<img src="/img/2.jpg" width="100%">
</div>


Los datos provienen de:
La Organización de Aviación Civil Internacional
Y de el precio historico de Boeing en la bolsa de valores (- 60 Year Stock Price History )

En el periodo 2017-2021 surgen las preguntas:
¿Qué empresa tuvo más fatalidades? 
¿Cuál fue el año con más fatalidades?
¿Cuál fue la empresa que más personas transporto?
¿Qué ocurrió con el precio de Boeing en el año de mayor fatalidades?¿Por qué?

Para resolver las preguntas
Observo los datos con diferentes gráficos

En el periodo comprendido entre 2017-2021 se registraron en total 220 fallecidos para tripulantes y 1638 fallecidos para pasajeros. (Esto seria sumando el total de los segmentos).

Se observa que son 48 personas de 220 (en el gráfico de tripulación)  y son 696 personas fallecidas de 1638 (en el gráfico de pasajeros) son de la empresa Boeing

Totalizando las observaciones hay 744 personas fallecidas de 1858 que corresponden a la empresa Boeing.

En el periodo 2017-2021
¿Qué empresa tuvo más fatalidades? 

La empresa con más fatalidades es Boeing.

¿Cuál fue el año con más fatalidades?

El año con más fatalidades es el año 2018.
Segmentando el gráfico por la empresa Boeing vemos que la cantidad de fallecidos aumenta en el año 2020 y que disminuye en el año 2021

¿Cuál fue el año con más fatalidades?
¿Cuál fue la empresa que más personas transporto?

La empresa que más personas transportó es Boeing

¿Qué incidencia tienen los accidentes con la empresa Boeing? y viceversa o sea ¿Cómo repercute la empresa en los accidentes?. En cuanto a cantidad de fatalidades por año.

Desde Boeing aseguran que hay más de 10.000 aviones comerciales Boeing en servicio, que transportan pasajeros y carga de manera más eficiente que los modelos de la competencia en el mercado.

También tomando en cuenta que el valor de las acciones de una empresa que cotiza en bolsa depende de la ley de la oferta y la demanda. Y que por este motivo cuando la bolsa sube significa que los títulos o valores que en ella se negocian están al alza debido a que hay más inversores intentando comprarlos (demanda) que títulos o valores disponibles para la venta (oferta). Cuando la bolsa baja es porque se da, justamente, la situación contraria: hay pocos inversores interesados en comprar las acciones disponibles, por lo que el valor de los títulos disminuye.

Teniendo en cuenta la dimensión de la empresa y el significado que es cotizar en bolsa. Podría decir que una de las razones por las que los inversores no estarían interesados en comprar acciones son los accidentes. 
El precio más alto de las acciones fue alcanzado en el año 2018 y 2019.
El precio más bajo fue alcanzado en el año 2020. 

¿qué ocurrió en 2020?

En el año 2020 hubo una disminución de vuelos por causa de la pandemia. los problemas del 737 MAX y los retrasos en el 777X.

Por ej: La empresa Boeing reconoció tener pérdidas millonarias en dolares en los años 2018-2019. Tras accidentes que dejaron muertos, tuvieron que compensar a sus clientes y proveedores.

Esto mismo hace que la desconfianza de los inversores crezca aunque esto contrasta con los ingresos en facturación por entrega de aviones.

Como conclusión Boieng tiene intenciones de mejorar estos números tanto económicos como de reducir fatalidades para seguir expandiendo su mercado. Boeing continuará invirtiendo en eficiencia para reducir el uso de combustible y la emisión de carbono

fuentes:
https://www.infobae.com/america/2021/01/28/boeing-perdio-usd-11900-millones-en-2020-entre-la-pandemia-los-problemas-del-737-max-y-los-retrasos-en-el-777x/

https://www.macrotrends.net/stocks/charts/BA/boeing/stock-price-history
https://aeromarket.com.ar/noticias/boeing-preve-que-en-20-anos-se-dupliquen-las-flotas/

