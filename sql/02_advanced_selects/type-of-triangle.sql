SELECT 
    CASE 
        WHEN A + B <= C OR A+C<=B OR C+B<=A THEN 'Not A Triangle' 
        WHEN A = B AND B=C THEN 'Equilateral' 
        WHEN A=B OR B=C OR C=A THEN 'Isosceles' 
        ELSE 'Scalene' END AS triangles_types 
    FROM 
        TRIANGLES