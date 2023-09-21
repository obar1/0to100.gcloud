# <https§§§www.cloudskillsboost.google§games§4424§labs§28636>
> <https://www.cloudskillsboost.google/games/4424/labs/28636>

# Creating and Populating a Bigtable Instance

![Alt text](image.png)
![Alt text](image-1.png)
![Alt text](image-2.png)
df api
![](image-3.png)

## Task 1. Create a Bigtable instance

![Alt text](image-5.png)
![Alt text](image-6.png)    
![Alt text](image-7.png)

## Task 2. Create a new Bigtable table

create table
![Alt text](image-8.png)

![Alt text](image-14.png)

## Task 3. Load data files from Cloud Storage using a Dataflow template
 you run a Dataflow job to load data from Cloud Storage to Bigtable. In order to run the Dataflow job successfully, you first have to create a Cloud Storage bucket for Dataflow to write temporary files as needed. Then you can successfully create and run a new Dataflow job from a template.

 ![Alt text](image-9.png)

 ![Alt text](image-10.png)

 ![Alt text](image-11.png)

 ## Task 4. Verify data loaded into Bigtable

```bash
echo project = `gcloud config get-value project` \
>> ~/.cbtrc
echo instance = personalized-sales \
>> ~/.cbtrc    
```


![Alt text](image-12.png)


```
cbt read UserSessions \
    count=10
    ```
![Alt text](image-13.png)

![Alt text](image-15.png)

![Alt text](image-16.png)