CREATE SCHEMA IF NOT EXISTS stg;

CREATE TABLE stg.stgDate (
    Date_id SERIAL PRIMARY KEY,
    Date DATE,
    Month_Number INTEGER,
    Month_Name VARCHAR(255),
    Year INTEGER
);

CREATE TABLE stg.stgProduct (
    Product_id SERIAL PRIMARY KEY,
    Product VARCHAR(255)
);

CREATE TABLE stg.stgSegment (
    Segment_id SERIAL PRIMARY KEY,
    Segment VARCHAR(255)
);

CREATE TABLE stg.stgCountry (
    Country_id SERIAL PRIMARY KEY,
    Country VARCHAR(255)
);

CREATE TABLE stg.stgDiscountBand (
    DiscountBand_id SERIAL PRIMARY KEY,
    Discount_Band VARCHAR(255)
);

CREATE TABLE stg.stgSales (
    sales_id SERIAL PRIMARY KEY,
    Units_Sold INTEGER,
    Manufacturing_Price DECIMAL,
    Sale_Price DECIMAL,
    Gross_Sales DECIMAL,
    Discounts DECIMAL,
    Sales DECIMAL,
    COGS DECIMAL,
    Profit DECIMAL
);
