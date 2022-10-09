--SELECT 
--FROM AdventureWorksDW2019.dbo.DimCustomer
--WHERE nama IN ('FirstName','LastName');


SELECT c.COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS c
WHERE TABLE_NAME = 'DimCustomer' 
AND COLUMN_NAME IN ('FirstName', 'LastName');


SELECT TOP 10 FirstName, LastName 
FROM AdventureWorksDW2019.dbo.DimCustomer;