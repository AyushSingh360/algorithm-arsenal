-- Write your MySQL query statement below
SELECT
    s.product_id,
    m.first_year,
    s.quantity,
    s.price
FROM Sales AS s
JOIN (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) AS m
ON s.product_id = m.product_id
AND s.year = m.first_year;
