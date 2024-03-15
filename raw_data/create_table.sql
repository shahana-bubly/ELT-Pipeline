-- SQL code for creating the table
CREATE TABLE IF NOT EXISTS sourcedb.financialData (
    Segment VARCHAR(255),
    Country VARCHAR(255),
    Product VARCHAR(255),
    Discount_Band VARCHAR(255),
    Units_Sold INTEGER,
    Manufacturing_Price DECIMAL,
    Sale_Price DECIMAL,
    Gross_Sales DECIMAL,
    Discounts DECIMAL,
    Sales DECIMAL,
    COGS DECIMAL,
    Profit DECIMAL,
    Date DATE,
    Month_Number INTEGER,
    Month_Name VARCHAR(255),
    Year INTEGER
);
