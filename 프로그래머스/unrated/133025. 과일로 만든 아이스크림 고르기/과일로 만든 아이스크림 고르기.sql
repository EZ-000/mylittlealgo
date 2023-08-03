SELECT A.FLAVOR
FROM ICECREAM_INFO A, FIRST_HALF B
WHERE A.FLAVOR = B.FLAVOR AND 3000 < B.TOTAL_ORDER AND A.INGREDIENT_TYPE = 'fruit_based'
ORDER BY B.TOTAL_ORDER DESC;