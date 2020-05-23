#!/usr/bin/env bash

python -m experiment.gcloud.main

# 上面完成后再wait 500秒
sleep 500
python -m experiment.gcloud.restart

for i in `seq 21`
do
	python -m experiment.client.machines.gcp.start-single ${i}
	# (里面记得加一个删除所有client,才能再跑)

	# wait 1分钟
	sleep 60
	python -m experiment.client.main
		
	# wait 5分钟(等待写入数据库,或者check数据库写入)
	sleep 300
	mysql -u johnson --password=johnson serviceid_db -e "select * from measurements" > ~/export_data/measurements_0521_${i}.csv
	mysql -u johnson --password=johnson serviceid_db -e "select * from transfer_time" > ~/export_data/transfer_time_0521_${i}.csv
done
