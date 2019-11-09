#!/bin/bash
gcloud compute instances create instance-1 --zone northamerica-northeast1-a
gcloud compute instances create instance-2 --zone southamerica-east1-b
gcloud compute instances create instance-3 --zone us-central1-a
gcloud compute instances create instance-4 --zone us-east1-b
gcloud compute instances create instance-5 --zone us-east4-c
gcloud compute instances create instance-6 --zone us-west1-b
gcloud compute instances create instance-7 --zone us-west2-a
gcloud compute instances create instance-8 --zone europe-north1-a
gcloud compute instances create instance-9 --zone europe-west1-b
gcloud compute instances create instance-10 --zone europe-west2-c
gcloud compute instances create instance-11 --zone europe-west3-c
gcloud compute instances create instance-12 --zone europe-west4-a
gcloud compute instances create instance-13 --zone europe-west6-a
gcloud compute instances create instance-14 --zone asia-east1-b
gcloud compute instances create instance-15 --zone asia-east2-a
gcloud compute instances create instance-16 --zone asia-northeast1-b
gcloud compute instances create instance-17 --zone asia-northeast2-a
gcloud compute instances create instance-18 --zone asia-south1-c
gcloud compute instances create instance-19 --zone asia-southeast1-b
gcloud compute instances create instance-20 --zone australia-southeast1-b
gcloud compute instances list >/home/wch19990119/list.txt