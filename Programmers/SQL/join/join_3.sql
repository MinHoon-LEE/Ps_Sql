SELECT NAME, DATETIME FROM 
(SELECT ANIMAL_ID,NAME, DATETIME  FROM ANIMAL_INS WHERE ANIMAL_ID NOT IN 
            (SELECT ANIMAL_ID FROM ANIMAL_OUTS) ORDER BY DATETIME) 
            WHERE ROWNUM <=3 ORDER BY DATETIME
