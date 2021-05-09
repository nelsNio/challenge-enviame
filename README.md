
**Backend Test: Desafío Envíame**

Autor : NELSON ANDRES NIÑO VERDUGO

Solucion planteada en python3

Luego de descargar el repositorio, se sugieren los siguientes pasos con sus respectivos comandos.

**Paso 1:** 
`docker-compose run web django-admin startproject challenge_enviame`

**Paso 2:**
`
docker-compose -f ./docker-compose.yml run --rm web python manage.py migrate
`

**Paso 3:**
`docker-compose -f docker-compose.yml build`

**Paso 4:**
`docker-compose up
`

**_Solución de los puntos:_**

**Ejercicio 1:** Docker. Ver en la raiz del proyecto

_Luego de tener en ejecucion lo anterior, se tienen los siguientes endpoints 
para cada uno de los siguiente puntos:_

**Ejercicio 2:** API REST + CRUD.: Al montar la imagen se crea la API,
y luego de ello se ejecuta se hace una llamado **GET** al siguiente endpoint:
para hacer la insercion de datos faker:

`http://0.0.0.0:8000/api/v1/empresas/fill_data/`

**Ejercicio 3:** Análisis + Desarrollo

Llamar al siguiente endpoint:
**GET**  `http://0.0.0.0:8000/api/v1/find_words/`

**Ejercicio 4:** Consumo API Envíame para la creación de un envío.

Llamar al siguiente endpoint:
**POS** `http://0.0.0.0:8000/api/v1/deliveries/`

_Es necesario en el body enviar la data planteada por la prueba_
_La informacion es guardada en una DB_

**Ejercicio 5:** Análisis + Desarrollo

Llamar al siguiente endpoint:
**GET** `http://0.0.0.0:8000/api/v1/fibonacci/`
retorna un valor numerico

**Ejercicio 6:** Análisis + Desarrollo Aplicado a Negocio
Llamar al siguiente endpoint:

**GET** `http://0.0.0.0:8000/api/v1/deliveries/estimate_delivery_time/`


_NOTA:_ Para los endpoints se adjunta una colección de postman y se encuentra en la carpeta **extras**


**Ejercicio 7:**  SQL
Se plantea la siguiente solucion:
```
UPDATE employees
SET salary=subquery.reajuste
FROM (
    SELECT (e.salary+ (e.salary*c2.anual_adjustment /100)) reajuste , e.id employee
    FROM  employees e JOIN countries c on c.id = e.country_id
    JOIN continents c2 on c.continent_id = c2.id
        where salary <=5000
         ) AS subquery
WHERE employees.id=subquery.employee;
```
_Se adjunta archivo .sql y se encuentra en la carpeta **extras**_
