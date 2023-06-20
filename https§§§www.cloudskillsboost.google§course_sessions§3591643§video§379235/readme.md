# <https§§§www.cloudskillsboost.google§course_sessions§3591643§video§379235>

> [https://www.cloudskillsboost.google/course_sessions/3591643/video/379235](https://www.cloudskillsboost.google/course_sessions/3591643/video/379235)

# Serverless Data Processing with Dataflow

until now we checked dataporc and batch, now we check batch dataflow pipelines

![1687252489419.png](./1687252489419.png)

cover streaming pipeline later

## Module introduction 1 minute

![1687252529901.png](./1687252529901.png)

dataflow is servless

dataflow allow to use same code for batch and streaming

> suggested way

learn dataflow and datproc and choose based on use cases

![1687252593671.png](./1687252593671.png)

![1687252608256.png](./1687252608256.png)

it is scalable

low latency, process data as it comes in

process batch and streaming in same api ...

![1687252662370.png](./1687252662370.png)

data process as data comes in in micro batch

![1687252678731.png](./1687252678731.png)

in beam it's unified

PTransform PCollection Pipeline runners and pipeline

PCollection is immutable and abstract

pipeleine changes ingest a pcol and create a new one

ptr handle input output and tranformation

data is passed from ptranf to another in the graph

pipeline runners are like containers

a pipline can be run on a computer, adata center or cloud

immutable datya is key diff betwenn batch and data processing

immutable data had no need sharing needed some sipler arch, it simplified distributed process

![1687259151982.png](./1687259151982.png)

direct graph and called pipeline but better to called data flow graph

a pcollection represnt batch or streaming  data

no size limit to pcollection

streaming data is a unbounded pcollection

![1687259205145.png](./1687259205145.png)

element in a pcollection are individually accessible and immutable

the pipliene and ptranform, runner handles the transfn on each element and distirubte the work

element represnts diff data types and stored in mem with related metadata

in pcollection data types are stored in serialized data so the network transer is easier

the data moves in a serialized state and de-serialize before the ptransf actions

## Introduction to Dataflow 5 minutes

![1687259459935.png](./1687259459935.png)

dataflow runs beam

dataflow service choose how to run the pipeline

reads, traform and write out to the sinks

to opt dataflow service optimize the graph

jobs is broken into units and scheduled

resources are free at the end of the job

fault toleranze is automatic

no preemptive scheduling

serveless job handling to process the data

## Why customers value Dataflow 2 minutes

![1687259606361.png](./1687259606361.png)

adv: fully mangaed and autoconfired, just deploy the pipeline, graph optimization, it does not wait a step to finish ebfore the next one, autoscale happens in the middle of the job when more resources are needed,

![1687259648355.png](./1687259648355.png)

tasks queued are rebalanced to the idle machines when possible

dynamic work rabalancing avoid devops hunti downm hot keys

![1687259684133.png](./1687259684133.png)

dataflow can handle late arrival records

glue other service like bigtable or bq or read from pubsub and save in cloudsql...

## Building Dataflow pipelines in code 3 minutes

![1687259836690.png](./1687259836690.png)

ex of pipeline, 3 ptranform to have an ooutput pcoll

syntax in python

![1687259861892.png](./1687259861892.png)

pipe operator applies the ptransf to the pcollections and output to a new pcoll

in java use of apply()

![1687259931579.png](./1687259931579.png)

branching to both ptransform 1 and 2 and store in 2 new pcollections

![1687259977772.png](./1687259977772.png)

a more complite example, we have a source where the data in pcollection comes from a sink

ptransh faltmap does apply a func to each row of the input and concatenates all the oputput, retuens 0 or more lelevance going to the output pcollection, the functions is called count_words with biz logic, the output is a set of integer and written in a atext file in cloud storage

using a with clause being the a batch process the pipeline is automatically terminated when done

![1687260132447.png](./1687260132447.png)

program execute with defualt runner // local to the machine

pass a aset of options is the runner to tun local or on the gcloud

![1687260183117.png](./1687260183117.png)

use of cmd line parameters to switch local and cloud

## Key considerations with designing pipelines 2

in  apcollection we have eleemnts

input and output of the pipline

setup the pipeline with bea.pipeline(options)

get data as input

![1687266648340.png](./1687266648340.png)

use readfromtest to read from a bucket

![1687266662148.png](./1687266662148.png)

read from pub/sub and parse the topic name

![1687266675587.png](./1687266675587.png)

read from bq

write to sinks to bq

![1687266717612.png](./1687266717612.png)

establish ref to bq table and details

use beam.writetobq to write

![1687266750992.png](./1687266750992.png)

we truncate data for each load

![1687266781514.png](./1687266781514.png)

in mem for small data set for lookup data

## Transforming data with PTransforms 3 minutes

![1687266820217.png](./1687266820217.png)

now data is in we need ptranform

map phase to do something in parallel

use generator to preserve the seed of the func, so the next is called it can continue where it left off

faltmap iterate over 1 to many

map ex returns (key,value) pair

flatmap ex yields the line only for lines containing the search term

![1687266952945.png](./1687266952945.png)

pardo to consider each eleemnt in a pcollection and output to a new collection or discrd it

use pardo to perform conversion of elemtns, simple or complex on elements and output the result as new pcoll

![1687267051007.png](./1687267051007.png)

code is as DoFn way and it's a beam class

the dofn function needs to be

- fully seriazilble
- idemptonemt
- code safe

as they work in ditributed env and parallell

![1687267128204.png](./1687267128204.png)

## Lab Intro: Building a Simple Dataflow Pipeline 1 minute

![1687267162571.png](./1687267162571.png)

## A Simple Dataflow Pipeline (Python) 2.5 1 hour 30 minutes

https://www.cloudskillsboost.google/course_sessions/3591643/labs/379242

## ~Serverless Data Analysis with Dataflow: A Simple Dataflow Pipeline (Java) 1 hour 30 minutes~

## Aggregate with GroupByKey and Combine 5 minutes

after map shuffle phase

![1687269533771.png](./1687269533771.png)

group by common keys and return the aggregated values

be aware of data skew ex 1 key with millions of items, then all the elements related go to the same worker group

![1687269651282.png](./1687269651282.png)

x will tyake for ever compared to y

y is idle

dataflow is designed to avoid eff like this

def aggregtion steps in dataflow

cogorupbykey

![1687269707551.png](./1687269707551.png)

now move to the reduce phase

![1687269742139.png](./1687269742139.png)

![1687269764282.png](./1687269764282.png)

when you apply combine ptrandform provide a func()  with logic

we have pre-built ones like sum miin and max

more copmplex case use subclass of a combine function

![1687269865809.png](./1687269865809.png)

combining func might called multiople times so it needs to have some properties

![1687269925498.png](./1687269925498.png)

provide 4 op with override

![1687269960498.png](./1687269960498.png)

Combine is orders of magnitude faster than GroupByKey because Dataflow knows how to parallelize a combine step

dataflow uses one worker per key at max

combine by key agggregate and then processed, less data goes on the networker

func must be commutative and associative

![1687270149967.png](./1687270149967.png)

flatten like union in sql for obj with same data type

merge pcollection into a bigger one

![1687270177718.png](./1687270177718.png)

split a pcollection in smaller pcollection

ex calculate perc and quartile and the top quartile has different processing than all the others

## Lab Intro: MapReduce in Beam1 minute

![1687270254427.png](./1687270254427.png)

map/reduce on pcolection

## MapReduce in Beam (Python) 2.5 1 hour 30 minutes

https://www.cloudskillsboost.google/course_sessions/3591643/labs/379246

## ~Serverless Data Analysis with Beam: MapReduce in Beam (Java) 1 hour 30 minutes~

## Side inputs and windows of data 4 minutes

![1687272679998.png](./1687272679998.png)

side inputs and windows goes with pcollection input

a side input is additional input that pardo func can access when processing element in the input pcollection

view of some other data that can be read to enrich the elements

inject additional data when processing each element in the input pcollection

additional data needs to def at runtime

![1687272800671.png](./1687272800671.png)

ex

words run in map to get lenght

combined globally for total lengh across all the data

figure out the avg lenght of words and feed back in that method to create a view and aviabled to workder nodes as side input

![1687272876538.png](./1687272876538.png)

additional capabilites

many ptranfo have 2 parts

ex arith mean with its accumulation step, after we processed all the elements we have the total and the count , the last part is just to divide

in case of unbounded dataset there is no ending, so we need some windowing

![1687272969941.png](./1687272969941.png)

![1687273022683.png](./1687273022683.png)

global window is by default

![1687273034629.png](./1687273034629.png)

streaming pipelines use time based windows for processing data in streaming

![1687273061918.png](./1687273061918.png)

for batch we can def some time stamped values

subsequ op can be computed on windows instead of globally

ex sliding windows 60 sec of data and starts a new one each 30 sec

you can do this streaming shit in bactch 📦

## Lab Intro: Practicing Pipeline Side Inputs 1 minute

![1687273198221.png](./1687273198221.png)

## Serverless Data Analysis with Dataflow: Side Inputs (Python) 1 hour 30 minutes

https://www.cloudskillsboost.google/course_sessions/3591643/labs/379250

## ~Serverless Data Analysis with Dataflow: Side Inputs (Java) 1 hour 30 minutes~

## Creating and re-using pipeline templates 3 minutes

create templates for the team

![1687278106206.png](./1687278106206.png)

rapid deployment of std pipeline

![1687278127797.png](./1687278127797.png)

traditional flow

dev and user need to be the same

with template

![1687278152779.png](./1687278152779.png)

user no need of dev

batch job submission by users

![1687278182753.png](./1687278182753.png)

submit using api or cmd line

![1687278213435.png](./1687278213435.png)

google provided template

![1687278224601.png](./1687278224601.png)

![1687278204299.png](./1687278204299.png)

![1687278231487.png](./1687278231487.png)

![1687278241675.png](./1687278241675.png)

you can create your own template

![1687278259651.png](./1687278259651.png)

run time and compile time params

add value provider interface

![1687278292378.png](./1687278292378.png)

java sample

![1687278301425.png](./1687278301425.png)

transform what usr submit on what you need

![1687278319605.png](./1687278319605.png)

metaata file is used for that

> underscore metadata suffix to the name.

## Summary 2 minutes

dataflow for new pipeline of rewrite old spark code

![1687278667459.png](./1687278667459.png)

## QUIZ Serverless Data Processing with Dataflow

 ![1687278756305.png](./1687278756305.png)
