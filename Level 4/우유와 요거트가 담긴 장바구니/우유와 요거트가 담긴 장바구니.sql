SELECT DISTINCT A.CART_ID FROM CART_PRODUCTS A, CART_PRODUCTS B WHERE A.NAME = '우유' and B.NAME = '요거트' and A.CART_ID = B.CART_ID ORDER BY A.CART_ID