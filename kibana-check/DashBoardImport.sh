#!/bin/sh
# use while loop to check if kibana is running 
while true
do
    response=$(curl -X POST elk:5601/api/saved_objects/_import -H "kbn-xsrf: true" --form file=@/CityCountDashBoard.ndjson | grep -oE "^\{\"success")
	echo $response
    if [ '{"success' = $response ]
        then
            echo "Running import dashboard.."
            #curl -X POST elk:5601/api/saved_objects/_import -H "kbn-xsrf: true" --form file=@/etc/elasticsearch/CityCountDashBoard.ndjson
            break
        else
            echo "Kibana is not running yet"
            sleep 10
    fi
done 