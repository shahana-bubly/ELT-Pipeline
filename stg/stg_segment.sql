truncate table stg.stgSegment;
INSERT INTO stg.stgSegment (Segment)
SELECT DISTINCT Segment
FROM sourcedb.financialdata;