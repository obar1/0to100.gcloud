# <https§§§www.cloudskillsboost.google§course_sessions§3631336§video§376363>

> [https://www.cloudskillsboost.google/course_sessions/3631336/video/376363](https://www.cloudskillsboost.google/course_sessions/3631336/video/376363)

# Data analyst tasks and challenges and Google Cloud data tools

![1687422294216.png](./1687422294216.png)

data analyst

- ingest data
- transorm data
- cretesoke reports
- analyz
- visualzie

![1687422317899.png](./1687422317899.png)

each step presents some chalenges

ingstion - petabyte of data to load not possible, only small amount

transform data - slow process as you need to  rely on other ppl

store - scaling up  the amount  of data

analyze - slow quries

visualzie - some lag in the analyze

![1687422432338.png](./1687422432338.png)

gcloud can help to mitigate/face those

ingest = bq storage and ingestion

transofrm = sql in bq and datarprep

store = bucket is not exp and bq storage

analysys = sql bq and scale out as ssas

visualzie = looker studio on top of bq

![1687422547025.png](./1687422547025.png)

# 9 fundamental BigQuery features

![1687422597295.png](./1687422597295.png)

dont manage hw but focus on data insights

in a nutshell

![1687422627862.png](./1687422627862.png)

pay for what you consume

![1687422645112.png](./1687422645112.png)

acl for members and groups

queries goes i the logging

pass multiple query at same time

![1687422701064.png](./1687422701064.png)

multiple datasets and no idx or keys as traditional rdbms

explore prebuilt dataset on line

![1687422769643.png](./1687422769643.png)

# Walkthrough: Data architecture diagram

arch diagram

![1687422791301.png](./1687422791301.png)

a job is what you sumbit on bq ssas

data is fully managed

![1687422824881.png](./1687422824881.png)

or put data in buckets and then query it

![1687422870127.png](./1687422870127.png)

bq is

- managed storage service
- analysis service

![1687422900501.png](./1687422900501.png)

- 2002 = gfs and mr papers
- 2008 dremel = process query on parallel on small cluster

![1687422979606.png](./1687422979606.png)

bq is 15y old

2015 https://archive.is/pQR2x

# Google Cloud tools for analysts data scientists and data engineers

this is more for data analyst

![1687423108455.png](./1687423108455.png)

vs

![1687423171673.png](./1687423171673.png)

ex

![1687423182021.png](./1687423182021.png)

```
So you have two different types of data. You have streaming events coming off a video game online.

You also have massive logs of data that are loaded in batches to a Cloud Storage staging area through a bucket resource. Data Engineers could use a service like Dataflow to build a pipeline.

You could then pipe in massive amounts of data into a data warehouse like BigQuery to perform ad hoc queries. Further right of that, for your reports, you could use an Analytics tool like Looker Studio

to analyze, explore, visualize, and present that information. Or, if you're a Data Scientist, you can plug in Vertex AI as a layer on top of BigQuery and invoke those queries to pre-process your data to build something cool like a machine

learning model
```

# Exploring an Ecommerce Dataset using SQL in Google BigQuery


[https://www.cloudskillsboost.google/course_sessions/3631336/labs/376367](https§§§www.cloudskillsboost.google§course_sessions§3631336§labs§376367/readme.md)

# Quiz: Big Data Tools Overview
 ![1687427000013.png](./1687427000013.png)

