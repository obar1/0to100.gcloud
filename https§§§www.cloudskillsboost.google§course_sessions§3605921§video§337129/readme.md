# <https§§§www.cloudskillsboost.google§course_sessions§3605921§video§337129>

> [https://www.cloudskillsboost.google/course_sessions/3605921/video/337129](https://www.cloudskillsboost.google/course_sessions/3605921/video/337129)

# Data Warehouse Solutions on Google Cloud

## Introduction 1 minute

![1687345164056.png](./1687345164056.png)

dwh tool in gcloud

end to end dwh solution

identify the feature and insight

tech resource

use the test env

## Implement Big Data Solutions on Google Cloud 3 minutes

impl of big data of gcloud of petabyes

dwh is the repository - bq in gcp

![1687346795180.png](./1687346795180.png)

dwh have datamarts as smaller repo to simplify

![1687346808456.png](./1687346808456.png)

in bq dataset can be seen as datamarts

data can raw

![1687346814635.png](./1687346814635.png)

datalake has raw data as files or bigtable transaction

we can def federated queries on them

![1687346845482.png](./1687346845482.png)

![1687346891140.png](./1687346891140.png)

traditional dwh are hard to op

bq is modern dwh

![1687346992029.png](./1687346992029.png)

bq can

- create read only view of data
- make result accessible via looker, google sheets
- foundation of ml/ai
- analyhze evnt in real time
- ingest up to 100k rows at second and pb fast query
- use of iam for access control

## Customer Needs 6 minutes

![1687347160712.png](./1687347160712.png)

what they need

resonable expections

what vallue dwh add to the customer and insights but they can t, feature they want when they move to the cloud

for on premiSE check curr impl

tool used for current analytics

![1687347218543.png](./1687347218543.png)

![1687347395566.png](./1687347395566.png)

use cases

- corporate reports
- get valuable insight

![1687347454765.png](./1687347454765.png)

usually they just do

![1687347464297.png](./1687347464297.png)

platorm need to reliable

more tools these days for complex questions

![1687347517963.png](./1687347517963.png)

predictive analysis is the end goal

![1687347547225.png](./1687347547225.png)

data on reliable

fast data access

poweful tool for analysis with scalability

![1687347590309.png](./1687347590309.png)

dwh scehma def how data is related and structured

schema is core of the design

pre-existing schema needs to be update thinking of bq

bq and teradata ansi sql

![1687347652506.png](./1687347652506.png)

bq does not support propetaty td sql, so some queires need to be refactored

![1687347696288.png](./1687347696288.png)

governance using iam and uth views can be useful

![1687347714922.png](./1687347714922.png)

use of datap from operation sources

migration of existing etl

![1687347735595.png](./1687347735595.png)

bi solution for reporting and analysis in combination with bq

migrate existing bi solution to bq

![1687347767847.png](./1687347767847.png)

even small jobs will run fine in bq or cehck the optimization guide

## Sample Architectures 1 minute

![1687347825098.png](./1687347825098.png)

just a sample

![1687347834922.png](./1687347834922.png)

op datasource feeding moden dwh

![1687347872933.png](./1687347872933.png)

combination of pub/sub and dataflow

![1687347931991.png](./1687347931991.png)

more complex using federated query

## Migration Strategies and Planning 8 minutes

key questions

- why migrating to gcloud, think the resource and how to apply, dont architect yet
- doc for migration, where to start
- def end state and scope of migration

![1687348028221.png](./1687348028221.png)

in the past we have op stores and dwh for the 3V (velocity, variaty and volume)

![1687348097443.png](./1687348097443.png)

history

on gcloud dwh can have the 3v

answers:

![1687348162672.png](./1687348162672.png)

focus on data not to infra, to save time

![1687348233005.png](./1687348233005.png)

more time for core biz

and roll out new idea

think of bq transfer service

![1687348306892.png](./1687348306892.png)

fast access to new results

on premise still there

gcp adoption to styart with

easy to compare both

![1687348334494.png](./1687348334494.png)

ideally on-premise will be decommissioned

![1687348377327.png](./1687348377327.png)

bq pricing and cost

![1687348394710.png](./1687348394710.png)

flat rate on fixed rate of slot

slot is a resource

![1687348420941.png](./1687348420941.png)

coast calculator

![1687348441282.png](./1687348441282.png)

extra tool - not GA yet

![1687348450735.png](./1687348450735.png)

## Working with PSO 2 minutes

![1687348486669.png](./1687348486669.png)

gcloud helps partners ;)

![1687348552828.png](./1687348552828.png)

for poc etc

![1687348569095.png](./1687348569095.png)

## ~Demo: Qwiklabs and the Google Cloud Platform 7 minutes~

## LAB Tour Qwiklabs and Google Cloud [PWDW] 1 hour 30 minutes


## Summary 1 minute
