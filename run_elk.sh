docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it \
	-v /home/owen/Documents/viscode/jupyter_logs:/opt/logstash \
	-e ES_HEAP_SIZE="4g" \
	-e LS_HEAP_SIZE="4g" \
	--name elk \
	-d \
	sebp/elk
