# How to do the measurements

work_path: /home/ubuntu/wch19990119/Hestia

## step1  启动server机器
vim experiment/gcloud/main.py # (修改机器数量)
vim experiment/gcloud/config.py # (修改zones，确认测试的地点)
1. rm -r experiment/gcloud/data/resource
2. python -m experiment.gcloud.main
3. python -m experiment.gcloud.restart # (等步骤二完成2分钟后)

## step2 在aws上启动client机器并运行实验
vim experiment/aws/utils.py # (配置机器数量和位置)
1. python -m experiment.client.machines.aws.start
2. rm -r experiment/client/data/examples
3. python -m experiment.client.main # (等步骤二完成2分钟后)

## step3 查看并存储数据

### 3.1 查看数据
1. mysql -ujohnson -pjohnson
2. use serviceid_db;
3. select * from transfer_time; # (当数据库中有client数量*5条数据时，整个测量代码运行结束)

### 3.2 存储数据
文件名自取
1. mysql -u johnson --password=johnson serviceid_db -e "select * from measurements" > ~/export_data/measurements_0629_aws_us.csv
2. mysql -u johnson --password=johnson serviceid_db -e "select * from transfer_time" > ~/export_data/transfer_time_0629_aws_us.csv
3. cp machine.json ~/export_data/machine_0629_us.json

## step4 删除机器
1. python -m experiment.client.machines.aws.cleanup
2. 在google cloud网页版上删除除了test之外的所有机器