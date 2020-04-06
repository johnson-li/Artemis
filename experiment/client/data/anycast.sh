lb_list=$(gcloud compute addresses list)
lb_list=${lb_list#*ipv4}
lb_list=${lb_list%%EX*}
lb_ip=`echo $lb_list | sed 's/ //g'`
name=`curl $lb_ip:110`
echo $name
