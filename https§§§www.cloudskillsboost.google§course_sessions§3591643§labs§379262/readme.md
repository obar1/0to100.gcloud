# <https§§§www.cloudskillsboost.google§course_sessions§3591643§labs§379262>
> <https://www.cloudskillsboost.google/course_sessions/3591643/labs/379262>

# Building and Executing a Pipeline Graph with Data Fusion 2.5

![](1687328599033.png)

## Task 1. Creating a Cloud Data Fusion instance

https://cloud.google.com/data-fusion/docs/how-to/create-instance

![](1687328676782.png)

![](1687328752846.png)

you need one additional step to grant the service account associated with the instance permissions on your project. Navigate to the instance details page by clicking the instance name.

Copy the service account to your clipboard.

![](1687329983504.png)

add the new principal nd Cloud Data Fusion API Service Agent r role 

![](1687330042388.png)

## Task 2. Loading the data
```bash
export BUCKET=$GOOGLE_CLOUD_PROJECT
gcloud storage buckets create gs://$BUCKET
gcloud storage cp gs://cloud-training/OCBL017/ny-taxi-2018-sample.csv gs://$BUCKET

# tm storage
gcloud storage buckets create gs://$BUCKET-temp
```

![](1687330201091.png)
cdf home

Wrangler is an interactive, visual tool that lets you see the effects of transformations on a small subset of your data before dispatching large, parallel-processing jobs on the entire dataset

![](1687330245832.png)
bucket access

![](1687330282060.png)
sample data in bucket

## Task 3. Cleaning the data

![](1687330348069.png)
data types 

## Task 4. Creating the pipeline

You can now create a batch pipeline to run transformations on all your data.

Cloud Data Fusion translates your visually built pipeline into an Apache Spark or MapReduce program that executes transformations on an ephemeral Cloud Dataproc cluster in parallel

create pipeline button 
![](1687330633060.png)

## Task 5. Adding a data source

The taxi data contains several cryptic columns such as pickup_location_id, that aren't immediately transparent to an analyst. You are going to add a data source to the pipeline that maps the pickup_location_id column to a relevant location name. The mapping information will be stored in a BigQuery table.

![](1687330802175.png)

![](1687330850072.png)
settings

![](1687330871497.png)

Now, you will add a source in your pipeline to access this BigQuery table. Return to the tab where you have Cloud Data Fusion open, from the Plugin palette on the left, select BigQuery from the Source section\

![](1687331013375.png)

## Task 6. Joining two sources

Now you can join the two data sources—taxi trip data and zone names—to generate more meaningful output.

![](1687331071574.png)
joiner

![](1687331329018.png)
properties

## Task 7. Storing the output to BigQuery

![](1687331379647.png)

![](1687331500940.png)

![](1687331515929.png)
pipeline


## Task 8. Deploying and running the pipeline

![](1687331555090.png)

![](1687331578578.png)
run

When you run a pipeline, Cloud Data Fusion provisions an ephemeral Cloud Dataproc cluster, runs the pipeline, and then tears down the cluster
![](1687331626057.png)

![](1687331823565.png)

## Task 9. Viewing the results

![](1687331660707.png)

![](1687333215028.png)

inside the op
![](1687333289441.png)