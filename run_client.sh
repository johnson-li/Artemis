python -m experiment.client.machines.aws.start
rm -r experiment/client/data/websites
sleep 120
python -m experiment.client.main
