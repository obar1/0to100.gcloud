# <https§§§www.cloudskillsboost.google§course_sessions§3724532§labs§382275>

> [https://www.cloudskillsboost.google/course_sessions/3724532/labs/382275](https://www.cloudskillsboost.google/course_sessions/3724532/labs/382275)


# Loading data into BigQuery

 ![1687898729837.png](./1687898729837.png)



## Task 1. Create a new dataset to store tables

 ![1687898787088.png](./1687898787088.png)

## Task 2. Ingest a new dataset from a CSV

 ![1687898844273.png](./1687898844273.png)

 ![1687898859458.png](./1687898859458.png)




## Task 3. Ingest a new dataset from Google Cloud Storage



```bash
bq load \
--source_format=CSV \
--autodetect \
--noreplace  \
nyctaxi.2018trips \
gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_2.csv
```


 ![1687899010844.png](./1687899010844.png)

now we have

20k rows

 ![1687899052237.png](./1687899052237.png)



## Task 4. Create tables from other tables with DDL


```bash

#standardSQL
CREATE TABLE
  nyctaxi.january_trips AS
SELECT
  *
FROM
  nyctaxi.2018trips
WHERE
  EXTRACT(Month
  FROM
    pickup_datetime)=1;


-- and
#standardSQL
SELECT
  *
FROM
  nyctaxi.january_trips
ORDER BY
  trip_distance DESC
LIMIT
  1
```
