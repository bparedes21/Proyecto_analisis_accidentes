DROP TABLE IF EXISTS Accidentes;

CREATE TABLE Accidentes (
    Date TEXT NOT NULL,
    Time INTEGER NOT NULL,
	Ruta INTEGER NOT NULL,
    Operator TEXT,
    Type TEXT,
    all_aboard INTEGER,
    passengers_aboard INTEGER,
    crew_aboard INTEGER,
    all_fatalities	INTEGER,
    passenger_fatalities	INTEGER,
    crew_fatalities INTEGER,
	ground INTEGER,
    summary TEXT,
	año INTEGER,
	empresa TEXT,
	
);

DROP TABLE IF EXISTS BoiengHistoricalValues;


CREATE TABLE BoiengHistoricalValues (
    date TEXT,
    open REAL,
	high REAL,
    low REAL,
    close REAL,
    volume REAL,
    año INTEGER
);

SELECT * FROM Accidentes

SELECT * FROM BoiengHistoricalValues


SELECT a.empresa , SUM(all_fatalities) as cantidad_de_fallecidos  FROM Accidentes a 
WHERE a.año >2016 and a.empresa <> "Otra empresa"
GROUP BY  a.empresa
ORDER BY  cantidad_de_fallecidos  DESC 


SELECT a.año, a.empresa, COUNT(a.empresa)   as cant_accid_por_empresa FROM Accidentes a 
WHERE a.año >2016 and a.empresa <> "Otra empresa"
GROUP BY a.año , a.empresa
ORDER BY   a.año  ASC   ,cant_accid_por_empresa DESC 

SELECT a.año, a.empresa , SUM(all_fatalities) as cantidad_de_fallecidos  FROM Accidentes a 
WHERE a.año >2016 and a.empresa <> "Otra empresa"
GROUP BY a.año , a.empresa
ORDER BY   a.año  ASC, cantidad_de_fallecidos  DESC 
