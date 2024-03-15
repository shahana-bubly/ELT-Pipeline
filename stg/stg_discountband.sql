truncate table stg.stgdiscountband;
-- Transfer data from public.financialdata to stg.stgDiscountBand
INSERT INTO stg.stgdiscountband (Discount_Band)
SELECT DISTINCT Discount_Band
FROM sourcedb.financialdata;