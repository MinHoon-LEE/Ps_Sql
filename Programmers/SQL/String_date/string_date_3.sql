SELECT ANIMAL_ID , NAME , (CASE WHEN REGEXP_LIKE
                           (SEX_UPON_INTAKE,'Spayed.*|Neutered.*') THEN 'O' ELSE 'X' END) "중성화"
    FROM ANIMAL_INS
        ORDER BY ANIMAL_ID
