# <https§§§www.cloudskillsboost.google§games§4422§labs§28603>
> <https://www.cloudskillsboost.google/games/4422/labs/28603>


# APIs Explorer: Qwik Start

http://developers.google.com/apis-explorer/


## Task 1. Create a Cloud Storage bucket

```
export PROJECT_ID=$(gcloud config get-value project)
gsutil mb -p $PROJECT_ID -c regional -l us-central1 gs://$PROJECT_ID-bucket


```

## Task 2. Upload an image

```
curl -O https://github.com/siddharth7000/practice/blob/main/sign.jpg
mv sign.jpg demo-image.jpg
gsutil cp demo-image.jpg gs://$PROJECT_ID-bucket/demo-image.jpg
gsutil acl ch -u allUsers:R gs://$PROJECT_ID-bucket/demo-image.jpg
```

