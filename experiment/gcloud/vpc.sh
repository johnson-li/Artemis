#!/bin/bash
gcloud compute --project=warm-canto-273013 networks create default2 --subnet-mode=custom
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-east1 --range=10.28.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-east2 --range=10.32.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=northamerica-northeast1 --range=10.38.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=southamerica-east1 --range=10.40.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-central1 --range=10.42.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-east1 --range=10.46.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-east4 --range=10.48.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-west1 --range=10.50.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-west2 --range=10.52.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=europe-north1 --range=10.54.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=europe-west1 --range=10.56.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=europe-west2 --range=10.58.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=europe-west3 --range=10.60.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=europe-west4 --range=10.62.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=europe-west6 --range=10.64.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-northeast1 --range=10.66.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-northeast2 --range=10.68.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-south1 --range=10.70.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-southeast1 --range=10.72.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=australia-southeast1 --range=10.74.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=asia-northeast3 --range=10.78.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-west3 --range=10.80.0.0/20
gcloud compute --project=warm-canto-273013 networks subnets create default2 --network=default2 --region=us-west4 --range=10.82.0.0/20