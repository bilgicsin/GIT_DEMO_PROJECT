FROM sebp/elk

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools && apt-get install jq -y

WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-integration-kafka
# add new config
ADD ./kafka_input.conf /etc/logstash/conf.d/kafka_input.conf

# add new config import dashboard sh
#USER root

#ADD  ./CityCountDashBoard.ndjson /etc/elasticsearch/CityCountDashBoard.ndjson
#ADD  ./DashBoardImport.sh /etc/elasticsearch/DashBoardImport.sh

#RUN chmod +x /etc/elasticsearch/DashBoardImport.sh

#ENTRYPOINT nohup /etc/elasticsearch/DashBoardImport.sh &
#CMD /etc/elasticsearch/DashBoardImport.sh
#CMD ["bash","-c","/etc/elasticsearch/DashBoardImport.sh"]
#CMD ["&"]


#RUN /etc/elasticsearch/DashBoardImport.sh &
#RUN nohup bash -c "/etc/elasticsearch/DashBoardImport.sh" >/dev/null 2>&1 &

#RUN curl -X POST elk:5601/api/saved_objects/_import -H "kbn-xsrf: true" --form file=@/etc/elasticsearch/CityCountDashBoard.ndjson


#USER root






