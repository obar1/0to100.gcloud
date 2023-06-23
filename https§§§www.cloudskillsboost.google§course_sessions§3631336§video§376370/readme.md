# <https§§§www.cloudskillsboost.google§course_sessions§3631336§video§376370>

> [https://www.cloudskillsboost.google/course_sessions/3631336/video/376370](https://www.cloudskillsboost.google/course_sessions/3631336/video/376370)

![1687500992383.png](./1687500992383.png)

sql is imperative for data analyst

what to do

![1687501059616.png](./1687501059616.png)

ask question about data

access the dataset or load to bq anf familiriaze

write good sql

![1687501132710.png](./1687501132710.png)

from left to right, you need to practice

sql has been around since the '80s

ansi 2011 sql is used from bq

# IRS public dataset overview

![1687501219290.png](./1687501219290.png)

https://console.cloud.google.com/marketplace/product/internal-revenue-service/irs-990

# Query basics

convert questions to sql

![1687501313787.png](./1687501313787.png)

3 parts in backticks

![1687501388767.png](./1687501388767.png)

example

add more fields to make sense of the data or ordering

![1687501421919.png](./1687501421919.png)

# Introduction to functions

use of format fx()

![1687501458322.png](./1687501458322.png)

![1687501477451.png](./1687501477451.png)

some functions

![1687501498568.png](./1687501498568.png)

add alias

![1687501537821.png](./1687501537821.png)

calculated field

where condition, it saves bytes skipping the data

order by

![1687501794766.png](./1687501794766.png)

![1687501852154.png](./1687501852154.png)

![1687501876744.png](./1687501876744.png)

avoid select STAR

![1687501933666.png](./1687501933666.png)

# Filters, aggregates, and duplicates

![1687501948301.png](./1687501948301.png)

alias not known at filtering time

![1687501969275.png](./1687501969275.png)

check agrgations

![1687501977498.png](./1687501977498.png)

calculation/aggr on all the rows

![1687502021934.png](./1687502021934.png)

nested functions

![1687502069452.png](./1687502069452.png)

group what is **not **under aggr

![1687502124999.png](./1687502124999.png)

address duplicates

![1687502141139.png](./1687502141139.png)

filter on aggregation

![1687502159112.png](./1687502159112.png)

use explanation tab

![1687503021589.png](./1687503021589.png)

![1687503065649.png](./1687503065649.png)

check data quality al th time when working with new datasets

![1687503188845.png](./1687503188845.png)

treat date as str and then parse as date properly

![1687503223483.png](./1687503223483.png)

better than taking just the first 4 chars

# Data types, date functions, and NULLs

data types

![1687504252817.png](./1687504252817.png)

use cast to convert

![1687504298725.png](./1687504298725.png)

not sure what it is, use safe_cast

![1687504319378.png](./1687504319378.png)

null is absence of value - not empty or others

handy when matching data

![1687504354098.png](./1687504354098.png)

not state == NULL , use ISNULL

![1687504395945.png](./1687504395945.png)

![1687504424103.png](./1687504424103.png)

when you have as yyyymmdd then you can use a lot of date functions

![1687504503502.png](./1687504503502.png)

# Wildcard filters with LIKE

![1687504519108.png](./1687504519108.png)

![1687504566601.png](./1687504566601.png)

more specific with 'help%'

![1687504586631.png](./1687504586631.png)

![1687504597788.png](./1687504597788.png)

another module for late

summary:

![1687504631186.png](./1687504631186.png)

# Troubleshooting Common SQL Errors with BigQuery v1.5

https://www.cloudskillsboost.google/course_sessions/3631336/labs/376377

# Quiz: Exploring your Data with SQL

 ![1687504782673.png](./1687504782673.png)

