-- el reajuste lo toma como un porcentaje y ese valor se suma al salario actual
UPDATE employees
SET salary=subquery.reajuste
FROM (
    SELECT (e.salary+ (e.salary*c2.anual_adjustment /100)) reajuste , e.id employee
    FROM  employees e JOIN countries c on c.id = e.country_id
    JOIN continents c2 on c.continent_id = c2.id
        where salary <=5000
         ) AS subquery
WHERE employees.id=subquery.employee;