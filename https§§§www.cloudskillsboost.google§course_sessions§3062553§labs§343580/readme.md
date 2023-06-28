# <https§§§www.cloudskillsboost.google§course_sessions§3062553§labs§343580>

> [https://www.cloudskillsboost.google/course_sessions/3062553/labs/343580](https://www.cloudskillsboost.google/course_sessions/3062553/labs/343580)

# PDE Prep: BigQuery Essentials

## Overview

![1687949453673.png](./1687949453673.png)

![1687949466642.png](./1687949466642.png)

## Task 1. Create a custom dataset

![1687949561086.png](./1687949561086.png)

![1687949648837.png](./1687949648837.png)

![1687949657564.png](./1687949657564.png)

preview:

![1687949673958.png](./1687949673958.png)


## Task 2. Query the dataset

 ![1687949738565.png](./1687949738565.png)


```sql
--  CHECK VALUES
select distinct  origin, destination from `qwiklabs-gcp-04-931cae51ab61.JasmineJasper.triplog`

-- all data 
select *  from `qwiklabs-gcp-04-931cae51ab61.JasmineJasper.triplog`
where origin ='FRA' and destination ='KUL'

-- ast query
select airline, avg(minutes)  from `qwiklabs-gcp-04-931cae51ab61.JasmineJasper.triplog`
where origin ='FRA' and destination ='KUL'
group by 1
order by 1



```

 ![1687950053266.png](./1687950053266.png)



 ![1687950394432.png](./1687950394432.png)
