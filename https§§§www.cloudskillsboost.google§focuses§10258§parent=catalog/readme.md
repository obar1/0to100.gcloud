# <https§§§www.cloudskillsboost.google§focuses§10258§parent=catalog>

> [https://www.cloudskillsboost.google/focuses/10258?parent=catalog](https://www.cloudskillsboost.google/focuses/10258?parent=catalog)

# Create and Manage Cloud Resources: Challenge Lab


```bash



#Task 2. Create a Kubernetes service cluster


export zone=us-west3-c
export region=us-west3
export PORT_NO=8081
export FIREWALL_RULE="permit-tcp-rule-575"

gcloud container clusters create nucleus-backend \
          --num-nodes 1 \
          --network nucleus-vpc \
          --zone $zone

gcloud container clusters get-credentials nucleus-backend \
          --zone $zone

kubectl create deployment hello-server \
          --image=gcr.io/google-samples/hello-app:2.0

kubectl expose deployment hello-server \
          --type=LoadBalancer \
          --port $PORT_NO


# Task 3. Set up an HTTP load balancer

gcloud compute instance-templates create web-server-template \
       --metadata-from-file startup-script=startup.sh \
       --network nucleus-vpc \
       --machine-type g1-small \
       --region $region

gcloud compute target-pools create nginx-pool --region $region

gcloud compute instance-groups managed create web-server-group \
--base-instance-name web-server \
--size 2 \
--template web-server-template \
--region $region

gcloud compute firewall-rules create "$FIREWALL_RULE" \
       --allow tcp:80 \
       --network nucleus-vpc

gcloud compute http-health-checks create http-basic-check

gcloud compute instance-groups managed \
       set-named-ports web-server-group \
       --named-ports http:80 \
       --region $region

gcloud compute backend-services create web-server-backend \
       --protocol HTTP \
       --http-health-checks http-basic-check \
       --global

gcloud compute backend-services add-backend web-server-backend \
       --instance-group web-server-group \
       --instance-group-region $region \
       --global

gcloud compute url-maps create web-server-map \
       --default-service web-server-backend

gcloud compute target-http-proxies create http-lb-proxy \
       --url-map web-server-map

gcloud compute forwarding-rules create "$FIREWALL_RULE" \
     --global \
     --target-http-proxy http-lb-proxy \
     --ports 80

gcloud compute forwarding-rules list


# NOTE : Please Wait Up To 5 Minutes After Commands Executed And Then Click On Check My Progress.

```
