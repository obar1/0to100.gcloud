# <https§§§www.cloudskillsboost.google§focuses§4415§parent=catalog>

> [https://www.cloudskillsboost.google/focuses/4415?parent=catalog](https://www.cloudskillsboost.google/focuses/4415?parent=catalog)

# Creating a Data Transformation Pipeline with Cloud Dataprep

## Overview

[https://cloud.google.com/dataprep/](https§§§cloud.google.com§dataprep§/readme.md)

## Task 1. Open Google Cloud Dataprep

![1687767520699.png](./1687767520699.png)

## Task 2. Creating a BigQuery dataset

![Data flow pipeline](https://cdn.qwiklabs.com/O2n0exH9RUENSsK99EJIUKFgk%2BX8HlTC95mpNxwqZcM%3D)



```sql
#standardSQL
 CREATE OR REPLACE TABLE ecommerce.all_sessions_raw_dataprep
 OPTIONS(
   description="Raw data from analyst team to ingest into Cloud Dataprep"
 ) AS
 SELECT * FROM `data-to-insights.ecommerce.all_sessions_raw`
 WHERE date = '20170801'; # limiting to one day of data 56k rows for this lab
```


 ![1687767717823.png](./1687767717823.png)



## Task 3. Connecting BigQuery data to Cloud Dataprep

 ![1687767803556.png](./1687767803556.png)


edit recipe

 ![1687767896608.png](./1687767896608.png)

column details

 ![1687767983852.png](./1687767983852.png)



## Task 5. Cleaning the data

change type

 ![1687768084668.png](./1687768084668.png)


uniq col

 ![1687768340568.png](./1687768340568.png)

 ![1687768547425.png](./1687768547425.png)


all transf

![Full Recipe](https://cdn.qwiklabs.com/rwbA5QmJRqmecUoGAhlAUNPBXlyJsBdSxYeqz4X7M%2F8%3D)



 ![1687768598692.png](./1687768598692.png)



## Task 7. Running Cloud Dataprep jobs to BigQuery

job def

 ![1687768775872.png](./1687768775872.png)

 ![1687768783667.png](./1687768783667.png)


job execution

 ![1687768817169.png](./1687768817169.png)


view bq job

 ![1687768852988.png](./1687768852988.png)




xxx
