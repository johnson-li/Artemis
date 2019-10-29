export GOOGLE_APPLICATION_CREDENTIALS="home/ws/code/key.json"
gcloud config set project project1-256208
gcloud compute instances create instance-1 --zone us-central1-a
gcloud compute instances create instance-2 --zone europe-west2-c
gcloud compute instances list >home/ws/code/list.txt
python handle.py