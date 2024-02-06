# <https§§§www.cloudskillsboost.google§course_sessions§7048758§labs§448290>
> <https://www.cloudskillsboost.google/course_sessions/7048758/labs/448290>

# Develop an app with Duet AI

![alt text](image.png)

## Task 1. Configure your environment and account


console

```bash
gcloud auth list

PROJECT_ID=$(gcloud config get-value project)
REGION=us-east1
echo "PROJECT_ID=${PROJECT_ID}"
echo "REGION=${REGION}"

USER=$(gcloud config get-value account 2> /dev/null)
echo "USER=${USER}"

gcloud services enable cloudaicompanion.googleapis.com --project ${PROJECT_ID}


```

```bash
# To use Duet AI, grant the necessary IAM roles to your Google Cloud Qwiklabs user account:

gcloud projects add-iam-policy-binding ${PROJECT_ID} --member user:${USER} --role=roles/cloudaicompanion.user
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member user:${USER} --role=roles/serviceusage.serviceUsageViewer
```

![alt text](image-1.png)

## Task 2. Create a Cloud Workstation

This lab uses Duet AI assistance to develop an app with the Cloud Code plugin for Cloud Workstations IDE. Cloud Workstations is a fully managed integrated development environment that includes native integration with Duet AI.

![alt text](image-2.png)

cluster configuration

![alt text](image-3.png)

![alt text](image-4.png)

create workstation

![alt text](image-5.png)

lunch wotkstation

![alt text](image-6.png)

## Task 3. Update the Cloud Code extension to enable Duet AI

enable duet ai
![alt text](image-7.png)

![alt text](image-8.png)
> click on the link to enable duet ai

![alt text](image-9.png)

## Task 5. Develop a Python app

How do I create a new Cloud Run app in Cloud Code using the command palette? What languages are supported?

![alt text](image-10.png)

create flask app
![alt text](image-11.png)

explain this 
![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-14.png)

run locally
![alt text](image-15.png)

![alt text](image-16.png)

![alt text](image-17.png)

Click the bulb, and then in the More Actions menu, select Generate code.

generating code
![alt text](image-18.png)

https://8080-my-workstation.cluster-yfldxa53efgn6qwgpowo53tq3e.cloudworkstations.dev/inventory

![alt text](image-19.png)

## Task 7. Deploy the app to Cloud Run

![alt text](image-20.png)

![alt text](image-21.png)
test

```bash
export SVC_URL=$(gcloud run services describe hello-world \
  --region us-east1 \
  --platform managed \
  --format='value(status.url)')
echo ${SVC_URL}/inventory
```

![alt text](image-22.png)

![alt text](image-23.png)



![alt text](image-24.png)