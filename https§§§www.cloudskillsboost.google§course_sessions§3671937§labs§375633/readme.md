# <https§§§www.cloudskillsboost.google§course_sessions§3671937§labs§375633>

> [https://www.cloudskillsboost.google/course_sessions/3671937/labs/375633](https://www.cloudskillsboost.google/course_sessions/3671937/labs/375633)

# Data to Insights: Unioning and Joining Datasets v1.1

## Overview

JOINs enrich your dataset by potentially adding fields (horizontally). UNIONs append more data to your table (vertically). When you understand the relationships between your tables, use UNIONS to append records to a consolidated table, and JOINs to enrich your results with data from multiple sources.

![1687760251578.png](./1687760251578.png)

## Task 1. Practice unioning and joining datasets

```
#standardSQL
# UNION Wildcard and returning a table suffix
SELECT
  COUNT(*) as number_of_filings,
  AS year_filed
FROM `bigquery-public-data.irs_990.irs_990`
GROUP BY year_filed
ORDER BY year_filed DESC
```

compare

```sql
#standardSQL
# UNION Wildcard and returning a table suffix
SELECT
  COUNT(*) as number_of_filings,
  _TABLE_SUFFIX AS year_filed
FROM `bigquery-public-data.irs_990.irs_990_*`
GROUP BY year_filed
ORDER BY year_filed DESC
```

 ![1687761815451.png](./1687761815451.png)



**Modify** the query you just wrote to only include the IRS tables with the following format: `irs_990_YYYY`

```
#standardSQL
# UNION Wildcard and returning a table suffix
SELECT
  COUNT(*) as number_of_filings,
  CONCAT(,_TABLE_SUFFIX) AS year_filed
FROM `bigquery-public-data.irs_990.irs_990_*`
GROUP BY year_filed
ORDER BY year_filed DESC
```

compare with

```sql
#standardSQL
# UNION Wildcard and returning a table suffix
SELECT
  COUNT(*) as number_of_filings,
  CONCAT("2",_TABLE_SUFFIX) AS year_filed
FROM `bigquery-public-data.irs_990.irs_990_2*`
GROUP BY year_filed
ORDER BY year_filed DESC
```

 ![1687761841799.png](./1687761841799.png)

Lastly, modify your query to only include tax filings from tables on or after 2013. Also include average `totrevenue` and average `totfuncexpns` as additional metrics.

```sql
#standardSQL
# count of filings, revenue, expenses since 2013
SELECT
  CONCAT("20",_TABLE_SUFFIX) AS year_filed,
  COUNT(ein) AS nonprofit_count,
  AVG(totrevenue) AS avg_revenue,
  AVG(totfuncexpns) AS avg_expenses
FROM `bigquery-public-data.irs_990.irs_990_20*`
WHERE _TABLE_SUFFIX >= '13'
GROUP BY year_filed
ORDER BY year_filed DESC
```

 ![1687761867953.png](./1687761867953.png)



## Task 2. Practice joining tables

Find the Org Names of all EINs for 2015 with some revenue or expenses. You will need to join tax filing table data with the organization details table.

```
#standard SQL
  # Find the Org Names of all EINs for 2015 with some revenue or expenses, limit 100
SELECT
  tax.ein AS tax_ein,
  org.ein AS org_ein,
  org.name,
  tax.totrevenue,
  tax.totfuncexpns
FROM
  AS tax
JOIN
  AS org
ON
  tax.ein =
WHERE
  > 0
LIMIT
  100;
```

compare with

```sql
#standardSQL
  # Find the Org Names of all EINs for 2015 with some revenue or expenses, limit 100
SELECT
  tax.ein AS tax_ein,
  org.ein AS org_ein,
  org.name,
  tax.totrevenue,
  tax.totfuncexpns
FROM
  `bigquery-public-data.irs_990.irs_990_2015` AS tax
JOIN
  `bigquery-public-data.irs_990.irs_990_ein` AS org
ON
  tax.ein = org.ein
WHERE
  tax.totrevenue + tax.totfuncexpns > 0
LIMIT
  100;
```

 ![1687761907307.png](./1687761907307.png)

## Task 3. Practicing working with NULLs

```
#standardSQL
  # Find where tax records exist for 2015 but no corresponding Org Name
SELECT
  tax.ein AS tax_ein,
  org.ein AS org_ein,
  org.name,
  tax.totrevenue,
  tax.totfuncexpns
FROM
  `bigquery-public-data.irs_990.irs_990_2015` tax
FULL JOIN
  `bigquery-public-data.irs_990.irs_990_ein` org
ON
  tax.ein = org.ein
WHERE
  org.ein IS NULL
```

![1687760418010.png](./1687760418010.png)

 ![1687761924600.png](./1687761924600.png)

