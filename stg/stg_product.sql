truncate table stg.stgProduct;
INSERT INTO stg.stgProduct (Product)
SELECT DISTINCT Product
FROM sourcedb.financialdata;
