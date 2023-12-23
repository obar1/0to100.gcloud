# <https§§§www.cloudskillsboost.google§games§4424§labs§28640>
> <https://www.cloudskillsboost.google/games/4424/labs/28640>

# Data Catalog: Qwik Start
GSP729

[https://cloud.google.com/data-catalog](../https§§§cloud.google.com§data-catalog/readme.md)

## Task 3. Copy a public New York Taxi table to your dataset.


```
bq cp bigquery-public-data:new_york_taxi_trips.tlc_yellow_trips_2018 $(gcloud config get project):demo_dataset.trips
```
![Alt text](image.png)

## Task 4. Create a Data Catalog tag template

![Alt text](image-1.png)

![Alt text](image-2.png)

![Alt text](image-3.png)


##  Task 5. Tag your table with the newly created tags

![Alt text](image-4.png)

![Alt text](image-5.png)