truncate table  stg.stgsales
-- Transfer data from public.financialdata to stg.stgSales
INSERT INTO stg.stgsales (
    Units_Sold, Manufacturing_Price, Sale_Price, Gross_Sales, Discounts, Sales, COGS, Profit
    )
SELECT DISTINCT
    f.Units_Sold, f.Manufacturing_Price, f.Sale_Price, f.Gross_Sales, f.Discounts, f.Sales, f.COGS, f.Profit
FROM 
    sourcedb.financialdata AS f