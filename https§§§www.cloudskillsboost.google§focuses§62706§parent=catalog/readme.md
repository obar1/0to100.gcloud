# <https§§§www.cloudskillsboost.google§focuses§62706§parent=catalog>
> <https://www.cloudskillsboost.google/focuses/62706?parent=catalog>

# Get Started with Cloud Storage: Challenge Lab

## Challenge scenario

```bash
gcloud auth list
gcloud config list project
gcloud config set compute/region us-central1
```


## Task 1. Create a bucket

```bash
export BUCKET_NAME=$(gcloud config get-value project)
gsutil mb gs://${BUCKET_NAME}
```

## Task 2. Create a retention policy

```bash
gsutil retention set 30s "gs://$BUCKET_NAME"

gsutil retention get "gs://$BUCKET_NAME"

```
## Task 3. Add a file to the bucket

```bash
curl https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Ada_Lovelace_portrait.jpg/800px-Ada_Lovelace_portrait.jpg --output ada.jpg
gsutil cp ada.jpg gs://${BUCKET_NAME}
gsutil acl ch -u AllUsers:R gs://${BUCKET_NAME}/ada.jpg
```