#!/bin/bash
gcloud compute instances create instance-1 --zone us-central1-a
gcloud compute instances create instance-2 --zone us-east1-b
gcloud compute instances create instance-3 --zone us-west2-a
gcloud compute instances create instance-4 --zone southamerica-east1-b
gcloud compute instances create instance-5 --zone europe-north1-a
gcloud compute instances create instance-6 --zone europe-west2-c
gcloud compute instances create instance-7 --zone europe-west6-a
gcloud compute instances create instance-8 --zone asia-northeast1-b
gcloud compute instances create instance-9 --zone asia-southeast1-b
gcloud compute instances create instance-10 --zone australia-southeast1-b
gcloud compute instances list >home/wch19990119/list.txt
