FROM ubuntu:latest

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools && apt-get install jq -y &&  apt-get install curl -y

# add new config import dashboard sh
USER root

#ADD  ./CityCountDashBoard.ndjson /CityCountDashBoard.ndjson
ADD  ./DashBoardImport.sh /DashBoardImport.sh

RUN chmod +x ./DashBoardImport.sh

ENTRYPOINT ./DashBoardImport.sh





