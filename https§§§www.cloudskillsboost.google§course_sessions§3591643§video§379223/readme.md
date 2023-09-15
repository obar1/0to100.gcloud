# <https§§§www.cloudskillsboost.google§course_sessions§3591643§video§379223>

> [https://www.cloudskillsboost.google/course_sessions/3591643/video/379223](https://www.cloudskillsboost.google/course_sessions/3591643/video/379223)

# [Building Batch Data Pipelines on Google Cloud] Executing Spark on Dataproc
## Module introduction 1 minute

![1687192250905.png](./1687192250905.png)

apache spark and hadoop ecosystem
hadoop on dataproc
gcs and hdfs

## The Hadoop ecosystem 4 minutes

historical notes
![1687192365619.png](./1687192365619.png)

![1687192379198.png](./1687192379198.png)
stored data in the cluister
ecosystem for hadoop
![1687192397796.png](./1687192397796.png)
on premise cluster
presto and spark used

spark is 100 faster than hadoop analytical engine

instead of hadoop cluster you can use dataproc

![1687192488070.png](./1687192488070.png)

problem and limitation of hadoop on premise

dataproc is managed hadoop to run existing jobs and tools

managed hw and configuration, dataproc allocate the resources and autoscale

simplified with dataproc version

flexible job conf, in dataproc you focus on clsuter with multiple cluster<->jobs

![1687192585133.png](./1687192585133.png)

spark uses available resources

in declarative programming the system handle the how, you say what you need

## Running Hadoop on Dataproc 10 minutes

how and why to run your hadoop/spark/pig code in dataproc

![1687193203680.png](./1687193203680.png)

minute by minute billing

fast to start

reasazable clusters

open source ecosystem

integrated with gcloud //cloud monitoring

managed as ssas

img versioning of the tools

HA for job restart

developer tools // api ssh and skd

init action to customize the cluster

auto/manual conf for resources

![1687193363446.png](./1687193363446.png)

ex

![1687193379010.png](./1687193379010.png)

![1687193412319.png](./1687193412319.png)

simple arch as on premise

primary nodes vm

use the same template to spin new vms and resize the cluster

dataproc is short lived cluster

use gcs instead of hdfs

![1687193476912.png](./1687193476912.png)

```
hdfs:// -> gs://
```

![1687193567539.png](./1687193567539.png)

![1687193543611.png](./1687193543611.png)

cluster as single vm for dev

HA with 3 primary nodes

regional endpoints for lowe latency

replication is 2 by default

pre-emptable nodes for saving cost

![1687193715217.png](./1687193715217.png)

job submission

you can createre restartable jobs that are idempotent

![1687193757011.png](./1687193757011.png)

monitoring of the cluster

## Cloud Storage instead of HDFS 6 minutes

instead of hdfs, before data locality, now with petabyte not needed

![1687194689297.png](./1687194689297.png)

block size are related to the actual hw

better having a separated solution

![1687194769732.png](./1687194769732.png)

bisection

![1687194784762.png](./1687194784762.png)

rate of 1 server from another part, petabyte => no need for local storage, used data from where it is located

![1687194829455.png](./1687194829455.png)

colossus and jupyter //fs and network

![1687194845603.png](./1687194845603.png)

bq released in 2010 by g

![1687194889808.png](./1687194889808.png)

separation of computer and storage

clusters and ephemeral resources

![1687194922778.png](./1687194922778.png)

use cloud storage what you need when you need

![1687194978061.png](./1687194978061.png)

![1687194996962.png](./1687194996962.png)

obj storage

![1687195016721.png](./1687195016721.png)

use `distcp`

## Optimizing Dataproc 2 minutes

you can use autozone where to put the cluster

use same region for gcs

check funneled vpn to avoid bottlenecks

avoid 10k input files oth combine in larger files

`fs.gs.block.size`

![1687195167506.png](./1687195167506.png)

how to size the number of vm needed compared the on premise cluster

## Optimizing Dataproc storage 9 minutes

some reasons to still use hdfs

![1687203161550.png](./1687203161550.png)

in general

![1687203210332.png](./1687203210332.png)

first reads from gcloud and last one

so you can separate storage and compute and reduce cost

use local non hdfs for shuffling

![1687203344759.png](./1687203344759.png)

some advices

think about region and zones when planning

![1687203372812.png](./1687203372812.png)

diff region calls can imply automatic copy of data in diff zones

![1687203398744.png](./1687203398744.png)

some other option to store

big table - hbase comliant , low latency and scatter data handling

bq - dwh oriented data

think as shor lived small clsuter for spec jobs called **ephemeral model**

![1687203621204.png](./1687203621204.png)

timer to delete the cluster

![1687203645610.png](./1687203645610.png)

specialized ephemeral cluster

reduce cost and admin

cluster can be resized any time

![1687203725998.png](./1687203725998.png)

decompose with job scoped clusters

use cloud storage

use acl

use eph cluster for the job lifetime

![1687203757985.png](./1687203757985.png)

cluster life cycle

![1687203787777.png](./1687203787777.png)

use case for persistent cluster

## Optimizing Dataproc templates and autoscaling 5 minutes

yaml file

![1687203838494.png](./1687203838494.png)

gcloud and rest api

ex

![1687203871166.png](./1687203871166.png)

startup script to install some extra'

use gcloud to create ąnew cluster, def the template to be used and vm details

add job to the cluster // spark job

submit the template as worflow template

![1687203923074.png](./1687203923074.png)

save money with autoscale polcies

auto scale improvements:

2 min

polciy can be shared among clusters

cloud logging has info about scaling

![1687203998868.png](./1687203998868.png)

set initial workers

![1687204082208.png](./1687204082208.png)

after action cooldown period and then autoscaling evalutaion happen again to avoid nodes new and kill in the same moment

## Optimizing Dataproc monitoring 3 minutes

![1687204987475.png](./1687204987475.png)

check history server and logs

yarn collect all logs in cloud logging

filter spark app using spark job ids

use labels and for dataproc jobs

![1687205087584.png](./1687205087584.png)

dataproc runs on top of compute engine
![1687205141812.png](./1687205141812.png)

log level
![1687205554366.png](./1687205554366.png)
![1687205588358.png](./1687205588358.png)

monitoring
![1687205569032.png](./1687205569032.png)

## Lab Intro: Running Apache Spark jobs on Dataproc 1 minute

 ![1687205618133.png](./1687205618133.png)


## Lab Running Apache Spark jobs on Cloud Dataproc 1 hour 30 minutes

[https://www.cloudskillsboost.google/course_sessions/3591643/labs/379232](https§§§www.cloudskillsboost.google§course_sessions§3591643§labs§379232/readme.md)


## Summary 1 minute

![](1687251862376.png)

## Executing Spark on Dataproc

![](1687251963223.png)
