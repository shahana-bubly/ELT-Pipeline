truncate table stg.stgDate;
-- Transfer data from public.financialdata to stg.stgDate

INSERT INTO stg.stgDate (Date, Month_Number, Month_Name, Year)
SELECT DISTINCT Date, Month_Number, Month_Name, Year
FROM sourcedb.financialdata;