#!/usr/bin/env bash

python -m experiment.gcloud.main

# 上面完成后再wait 3分钟
sleep 180
python -m experiment.gcloud.restart

for i in `seq 21`
do
	python -m experiment.client.machines.gcp.start(里面记得加一个删除所有client,才能再跑)

	# wait 1分钟
	sleep 60
	python -m experiment.client.main
		
	# wait 5分钟(等待写入数据库,或者check数据库写入)
	sleep 300
	mysql -u johnson --password=johnson serviceid_db -e "select * from measurements" > ~/export_data/measurements${i}.csv
	mysql -u johnson --password=johnson serviceid_db -e "select * from transfer_time" > ~/export_data/transfer_time${i}.csv
done