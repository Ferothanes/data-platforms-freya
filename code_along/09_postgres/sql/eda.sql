SELECT
    utbildningsnamn,
    utbildningsområde,
    "yh-poäng",
    beslut,
    "utbildningsanordnare administrativ enhet",
    kommun
FROM
    myh_2024
WHERE
    beslut = 'Beviljad'
    AND utbildningsområde = 'Data/IT';

SELECT
    COUNT(*)
FROM 
    it_education;

SELECT * FROM it_education
WHERE LOWER(utbildningsnamn) LIKE '%data eng%';