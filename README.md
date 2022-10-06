# GIT_DEMO_PROJECT
docker file çalıştırıldığında iki tane python (producer/comsumer) 3 tane elk (elastic, logstash, kibana) 1 tane kafka 1 tane mysql container ayağa kalkar.

python producer fake log üzereterek kafka topic'ine basıyor. python consumer kafka topic'ini okuyarak mysql tablosuna yazıyor.

ELK ise logları logstash aracılığı ile okuyarak elasticsearch'e indexliyor. İndex ise canlı metrikleri içeren bir dashboard'ı besliyor.

Elk'yı ayağa kaldırırken container'dan şu şekilde bir hata alınabiliniyor mevcut sisteme göre:

"bootstrap check failure [1] of [1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]".

Eğer benzer bir sorun olursa Desktop Docker için powershell'den şunları yazabilirsiniz:

wsl -d docker-desktop
sysctl -w vm.max_map_count=262144

Kibana-check container ı çalışmayı bitirip durduğunda grafik şu linkte hazır olacak:

http://localhost:5601/app/dashboards#/view/46c98770-5442-11ec-9c75-35056cad2234?_g=(filters:!(),refreshInterval:(pause:!f,value:1000),time:(from:now-15m,to:now))

MYSql için bağlantı bilgileri:

      ROOT_PASSWORD: demo_user
      USER: demo_user
      PASSWORD: demo_user
      DATABASE: demodb

      Hostname: localhost
      Port: 3306
