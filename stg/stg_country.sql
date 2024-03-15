truncate table stg.stgCountry;
INSERT INTO stg.stgCountry (Country)
SELECT DISTINCT Country
FROM sourcedb.financialdata;
