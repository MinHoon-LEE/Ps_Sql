SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS
        WHERE REGEXP_LIKE(NAME, '.*el.*','i')
        AND ANIMAL_TYPE = 'Dog'
            ORDER BY NAME
