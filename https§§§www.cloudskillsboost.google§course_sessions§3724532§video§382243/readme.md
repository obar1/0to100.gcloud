# <https§§§www.cloudskillsboost.google§course_sessions§3724532§video§382243>

> [https://www.cloudskillsboost.google/course_sessions/3724532/video/382243](https://www.cloudskillsboost.google/course_sessions/3724532/video/382243)

# Module introduction

role of data eng and why to be done in the cloud

data pipliena nd their prupose

challenege in the data eng and cloud solution

bq intro

def datalakes and dataw

transactional databases

how to partner with the other teams

data governace

prod and monitoring

user case study

![1687867590699.png](./1687867590699.png)

# The role of a data engineer

a ta eng build data pipeline to get data to  help biz to take data drive decisions

![1687867667962.png](./1687867667962.png)

data lake bring data from enterprise and store raw data in datalake in single location

ex is to store in gcloud bucket

consideration

- datalka fits in cloud bucket or cloudsql
- scale to meet demand
- does it support high trougguput

![1687867742744.png](./1687867742744.png)

cloud storage is blob storage so think about granularity access![1687867774133.png](./1687867774133.png)

bucket is good place to land raw data and then ingest in other places

storing data in buckets is durable and reliable

you can query the bucket data from bq

![1687867831766.png](./1687867831766.png)

loading data needs etl

extract tranform and load them

![1687867863431.png](./1687867863431.png)

batch pipeline in this case

![1687867875391.png](./1687867875391.png)

store data in pub sub - transform it in datflow and store in bq

# Data engineering challenges

challenges

- diffucult access data
- quality of raw data is low
- tranf to refine data need resources
- challenge query perfomance

![1687867947160.png](./1687867947160.png)

ex compute cost of acquring a customer,  data scattered in crm and other system

![1687867975850.png](./1687867975850.png)

data access is difficult as data is silos inside departments

![1687868003223.png](./1687868003223.png)

you need to know how tio combine data and each one has diff way to be accessed

so it can be challenge

![1687868056452.png](./1687868056452.png)

dwh place where the data is in some form where easy to joina and query the data

dl raw is not easy to query

![1687868098441.png](./1687868098441.png)

transform data from raw, etl the data and store in dwh

get raw data and then tranform to apply transf

![1687868189539.png](./1687868189539.png)

if you need to do a lot of T a lot of resource can be necessary

![1687868210492.png](./1687868210492.png)

etl jobs depends on data volume

![1687868230471.png](./1687868230471.png)

eff of performnace

![1687868247355.png](./1687868247355.png)

a lot of ovehead here, instead of focusing on insights

# Introduction to BigQuery

![1687868268492.png](./1687868268492.png)

instead of the above you can use gcloud bq

ssas petascale dwh on gcloud

bq service replaces traditional dwh

dataset are like adata mart

data lake as bucket and cloudsql

def view as ansi 2011

iam grant

![1687868367190.png](./1687868367190.png)

do more with less and avoid spending time on things not bringing value

![1687868392635.png](./1687868392635.png)

avoid to previsions or tuning sresource

![1687868410180.png](./1687868410180.png)

no need to provision reosurce

bq allocate resource as we consume as we add data to tables

queries use slot (cpu and ram resources)

# Data lakes and data warehouses

details on dwh and dl

we need to have data in usable form, raw data usually is not

![1687868475531.png](./1687868475531.png)

consider key consideration about dwh  option

- dwh is a sink fed by batch or streaming
- will dwh scale to meet needs // def concurr query limits
- how data is organize catalogues and iam
- who pay for the query
- is perforance enough
- level of maintanance

![1687868552513.png](./1687868552513.png)

![1687868558481.png](./1687868558481.png)

- tradizional were limited hoe many ppl can use it
- you can share query results like looker
- bq lays foundation for ai

![1687868614618.png](./1687868614618.png)

- bq allows analyse streaming data ingestion
- bq eliminates infrastarcture
- simplify iam and resource access

![1687868685077.png](./1687868685077.png)

you can treat bq as simple query engine and query data stored in cloud sql or files in buckets and leave the data in place

![1687868710400.png](./1687868710400.png)

# Transactional databases versus data warehouses

![1687868754722.png](./1687868754722.png)

diff between db and dwh

you can migrate your db to cloud

![1687868775714.png](./1687868775714.png)

a lot of reosurce per instance and autoscale with 0 downtime

avoid cloudsql for reporting

![1687868804796.png](./1687868804796.png)

few  option for sql transaction //  opt for writes

bq is for analaysse // opt for reads

bq is column based storage so you can read individual columns

![1687868869737.png](./1687868869737.png)

they serve 2 diff purposes

ex sql needs transactions

built on ref entegrity too

![1687868935936.png](./1687868935936.png)

transactional systsme are raw data source on the left, these upstream get gathered togethers called dl

data is transformerd and stored in dwh and used by other systems and teams

# Partner effectively with other data teams

![1687869029601.png](./1687869029601.png)

add new value to the data as ml

![1687869042164.png](./1687869042164.png)

other teams partner with data eng core team working on dwh

- ml  enf
- data analyst and bi
- other data eng

![1687869081849.png](./1687869081849.png)

earn trust making data discoverable, documented and easily accessable by toher teams

![1687869185976.png](./1687869185976.png)

you can use bq ml to make ml in bq directly

![1687869202038.png](./1687869202038.png)

other teams built dataset with clear schema def and perf to scale to concurrent dashborad

![1687869233838.png](./1687869233838.png)

bq bi engine to speed up bi  app

instead of usingn  olap cube to have sub-sec response time, with intelligence caching and bq data access

![1687869304154.png](./1687869304154.png)

how to scale and monitor the dwh

use of monitoring with alerts and notification on mterics

![1687869327999.png](./1687869327999.png)

and track exp and cloud autdit log to see granular on execution query

![1687869359642.png](./1687869359642.png)

# Manage data access and governance

def data access policy and how data would be used

![1687869393640.png](./1687869393640.png)

![1687869397893.png](./1687869397893.png)

- who can access
- pii handling
- acess to metadata

![1687869418775.png](./1687869418775.png)

data catalofues helop to search the data,  in case of a lot of dataset for unified discovering

cloud data loss api helps to manage sensitive data

![1687869466754.png](./1687869466754.png)

# Demo: Finding PII in your dataset with the DLP API

![1687869488369.png](./1687869488369.png)

![1687869526333.png](./1687869526333.png)

![1687869535490.png](./1687869535490.png)

ex

identify pii  on tb of data

# Build production-ready pipelines

![1687869580405.png](./1687869580405.png)

end to end and scalable processign data

![1687869618427.png](./1687869618427.png)

use of workflow

![1687869631020.png](./1687869631020.png)

aka cloud composer

![1687869643269.png](./1687869643269.png)

you can call api endpoint

kick off datapip for you

# Google Cloud customer case study

![1687869708511.png](./1687869708511.png)

data on hdfs copied to gcloud buckets

and give access to us from there

# Recap

![1687869763645.png](./1687869763645.png)

![1687869799493.png](./1687869799493.png)

https://github.com/priyankavergadia/google-cloud-4-words

# Lab Intro: Using BigQuery to do Analysis

![1687869980879.png](./1687869980879.png)

# Using BigQuery to do Analysis

https://www.cloudskillsboost.google/course_sessions/3724532/labs/382256



# Quiz: Introduction to Data Engineering


 ![1687870669867.png](./1687870669867.png)
