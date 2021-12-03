FROM sebp/elk

WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-integration-kafka
# add new config
ADD ./kafka_input.conf /etc/logstash/conf.d/kafka_input.conf





