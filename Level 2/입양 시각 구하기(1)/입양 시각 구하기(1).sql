SELECT hour(DATETIME) as HOUR, count(DATETIME) as COUNT from ANIMAL_OUTS where hour(DATETIME) >= 9  and hour(DATETIME) <= 19 group by hour(DATETIME)