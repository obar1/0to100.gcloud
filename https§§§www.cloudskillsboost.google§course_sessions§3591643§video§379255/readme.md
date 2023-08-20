# <https§§§www.cloudskillsboost.google§course_sessions§3591643§video§379255>

> [https://www.cloudskillsboost.google/course_sessions/3591643/video/379255](https://www.cloudskillsboost.google/course_sessions/3591643/video/379255)

# Module introduction

we will discuss how to manage data pipelines with Cloud Data Fusion and Cloud Composer
cdf to build datap and use composer to orchestarte work
![1687321407814.png](./1687321407814.png)

## Introduction to Cloud Data Fusion 3 minutes

![1687321652770.png](./1687321652770.png)

ux based

no code tools for datapip

![1687321728572.png](./1687321728572.png)

diff users

![1687326193264.png](./1687326193264.png)

connectors

less complex

interoperability with opne soruce software

![1687326231961.png](./1687326231961.png)

use templates and connectors and lib of tranforamtion

test and debug the pipeline

![1687326257740.png](./1687326257740.png)

use of unified serach func

track of lienage of transformation

![1687326286040.png](./1687326286040.png)

## Components of Cloud Data Fusion 1 minute

![1687326343350.png](./1687326343350.png)

warngler and data pipeline

![1687326406131.png](./1687326406131.png)

create and share datac dictionary between the 2

![1687326427000.png](./1687326427000.png)

eca to parse events

## Cloud Data Fusion UI 1 minute

high level look to UX

![1687326460230.png](./1687326460230.png)

home

![1687326473295.png](./1687326473295.png)

mutiple pipelines

![1687326497079.png](./1687326497079.png)

dev studio

![1687326512457.png](./1687326512457.png)

wrangler

![1687326522169.png](./1687326522169.png)

tag properties and lineage

![1687326536309.png](./1687326536309.png)

hub for sample

![1687326545139.png](./1687326545139.png)

![1687326552540.png](./1687326552540.png)

admin for mng of services and conf for namespace etc

## Build a pipeline 4 minutes

![1687327525925.png](./1687327525925.png)

flow from one direction to another

they cannot feed themself

each stage is a node

![1687327574613.png](./1687327574613.png)

you can multiple nodes forking out from a parent

![1687327609340.png](./1687327609340.png)

studio is where you have a canvas

minimap to navigate

![1687327652695.png](./1687327652695.png)

all the elements

you can use templates

![1687327685367.png](./1687327685367.png)

preview mode before deploy, see sample data from each node

![1687327758577.png](./1687327758577.png)

click on node add details about it

ex use of speech text api

![1687327795830.png](./1687327795830.png)

run pipeline on schedule

designe for bacth data pipelines

![1687327828866.png](./1687327828866.png)

lineage tracked

## Explore data using wrangler 1 minute

![1687327908151.png](./1687327908151.png)

wrangler used to explore the dataset

useful before building the actual pipeline

new dataset can be explored with the wrangler

ux

- left connection to dataset
- add new connection to datasources
- live browsing in the connection
- rx ex on bucket

![1687327996309.png](./1687327996309.png)

explor row and columns

calculated field and filter and wrangle the data as recipe

## Lab Intro: Building and executing a pipeline graph in Cloud Data Fusion 1 minute

![1687328055239.png](./1687328055239.png)

## Building and Executing a Pipeline Graph with Data Fusion 2.5 2 hours 30 minutes

[https://www.cloudskillsboost.google/course_sessions/3591643/labs/379262](https§§§www.cloudskillsboost.google§course_sessions§3591643§labs§379262/readme.md)

## Orchestrate work between Google Cloud services with Cloud Composer 1 minute

![1687328989629.png](./1687328989629.png)

control services with orch engine

ssas based on airflow

![1687329019935.png](./1687329019935.png)

4 tasks to manage ml pipeline

## Apache Airflow environment 1 minute

![1687329058627.png](./1687329058627.png)

home

![1687329130238.png](./1687329130238.png)

dags folder

bucket with dags file

## DAGs and Operators 7 minutes

![1687329341664.png](./1687329341664.png)

dag and operators

workflow are written in py

![1687329414341.png](./1687329414341.png)

upload the file and under dags is representd visually as a dag with nodes and edges

wofloflow is called gsctobqtriggered and it ahs 3 taks

each task invokes something

![1687329501425.png](./1687329501425.png)

we have success and failure handling

nodes are executed based on the parent outcome

![1687329562499.png](./1687329562499.png)

uses 2 operators

![1687329581863.png](./1687329581863.png)

airflow has many opearote to impl a task

a task usually is atomic and self contained

![1687329616198.png](./1687329616198.png)

more common op for gcp data eng

![1687329679053.png](./1687329679053.png)

ml op

![1687329710422.png](./1687329710422.png)

open source an multi cloud

![1687329729071.png](./1687329729071.png)

4 tasks

and 4 op

![1687329787413.png](./1687329787413.png)

the bqop needs some params like the query

![1687329817791.png](./1687329817791.png)

filters on the sql are parameters using `{ ... }`

![1687329842308.png](./1687329842308.png)

params can be dynamic too based on the airflow vars

![1687329865474.png](./1687329865474.png)

ml related

![1687329878733.png](./1687329878733.png)

usually the op execution order is defined at the end

## Workflow scheduling 5 minutes

![1687334049207.png](./1687334049207.png)

schedule your workflow or trigger based

![1687334077018.png](./1687334077018.png)

schedule can be defined

![1687334101305.png](./1687334101305.png)

cf to trigger

![1687334110255.png](./1687334110255.png)

regualr schedule route

![1687334133043.png](./1687334133043.png)

event trigger and then it kicks off

![1687334143666.png](./1687334143666.png)

push pull arch

![1687334208333.png](./1687334208333.png)

csv in gcs so we choose evnt trigger and bucket to watch

![1687334226021.png](./1687334226021.png)

most of this code is all bolier plate to copy from

![1687334269754.png](./1687334269754.png)

```
 Here, we specify a name for our function called Trigger DAG, then we tell it where your airflow environment is to be triggered
and which DAG in that airflow environment. In this case, it's looking for one called GCS to BigQuery triggered. Keep in mind, you can have multiple workflows or DAGs in a single airflow environment,
so be sure you specify the correct DAG underscore name to trigger. Then we have a few constants that we are provided, which construct the airflow URL that we're going to trigger a post request to,
as well as who's making the request and what the body of the request is. Lastly, the Trigger DAG function makes the actual request against the airflow server to kick off a workflow DAG
```

![1687334301032.png](./1687334301032.png)

index.js and package.json and trigger dag and dunc is capitale seinsitive

![1687334333891.png](./1687334333891.png)

the func is watching for the bucket

## Monitoring and Logging 3 minutes

![1687335519406.png](./1687335519406.png)

monitor and trouble shoot

check historical

we can have auto retry

![1687335560100.png](./1687335560100.png)

some reds -> issues

![1687335580359.png](./1687335580359.png)

1st is fine but 2nd is failing

![1687335747311.png](./1687335747311.png)

check logs

![1687335763989.png](./1687335763989.png)

or cloud logs as well

![1687335800454.png](./1687335800454.png)

when using cf check gcloud logs

## Lab Intro: An Introduction to Cloud Composer 1 minute

![1687335847308.png](./1687335847308.png)

## An Introduction to Cloud Composer 2.5 1 hour 30 minutes

[https://www.cloudskillsboost.google/course_sessions/3591643/labs/379269](https§§§www.cloudskillsboost.google§course_sessions§3591643§labs§379269/readme.md)

## QUIZ Manage Data Pipelines with Cloud Data Fusion and Cloud Composer
