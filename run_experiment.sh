rm -r experiment/gcloud/data/websites
python -m experiment.gcloud.main
sleep 120
python -m experiment.gcloud.restart
python -m experiment.client.machines.aws.start
rm -r experiment/client/data/websites
sleep 120
python -m experiment.client.main
