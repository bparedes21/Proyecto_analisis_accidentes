
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

<div align = "center">
<a href=""><img src="/img/accidentes.jpg" width="400 px"></a>

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
| 2 | [Consultas_SQL](#Consultas_SQL)  | 


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
<H3>Cruzar con otra fuente de datos, realizar el tablero en Power bi, redactar una historia con los datos.
Para cruzar datos con otras fuentes utilizo los datos que provee la web www.macrotrends.net/.</H3>
<div align = "center">
<img src="/img/1.jpg" width="100%">
</div>
<div align = "center">
<img src="/img/2.jpg" width="100%">
</div>
<div align = "center">


<H2> 👇 Podes encontrar la presentacion completa aca! :technologist: </H2>

🌍  [Presentacion](https://docs.google.com/presentation/d/1LhDOYOHI9AY0KWa3QyYjlPp6FCHtt5v5511Wk6EuQCg/edit?usp=sharing) - Analisis
</div>

******************************************************************************

<div>

## Consultas_SQL

Se requiere saber cual es la empresa fabricante de aviones que tuvo mas aviones involucrados en accidentes aereos a partir del año 2016. Y el año de los incidentes.

```js 

SELECT a.año, a.empresa, COUNT(a.empresa)   as cant_accid_por_empresa FROM Accidentes a 
WHERE a.año >2016 and a.empresa <> "Otra empresa"
GROUP BY a.año , a.empresa
ORDER BY   a.año  ASC   ,cant_accid_por_empresa DESC 
LIMIT 10

```
</div>

Resultado de la consulta:

<div align = "center">

| año_de_accidente | empresa | cant_accid_por_empresa |
|---|----------------|---|
| 2017 | Antonov  |  2  |
| 2017 | Lockheed  |  1  |
| 2017 | Boeing  |  1  |
| 2018 | Boeing |  5  |
| 2018 | Antonov |  2  |
| 2018 | Lockheed |  1  |
| 2018 | Lockheed |  1  |
| 2018 | De Havilland |  1  |
| 2019 | Boeing |  3  |
| 2019 | Antonov |  2  |

</div>

fuentes:
https://www.infobae.com/america/2021/01/28/boeing-perdio-usd-11900-millones-en-2020-entre-la-pandemia-los-problemas-del-737-max-y-los-retrasos-en-el-777x/

https://www.macrotrends.net/stocks/charts/BA/boeing/stock-price-history
https://aeromarket.com.ar/noticias/boeing-preve-que-en-20-anos-se-dupliquen-las-flotas/

