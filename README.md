# Инструкция запуска

### для настройки серверов запустите плейбук
ansible-playbook -i inventory.ini proxmox-preparing.yml


## приложение на питоне

### локальный тест скрипта
###### (образец моего вывода)
host01:~$ curl http://localhost:8000
{"headers":{"Accept":"*/*","Host":"localhost:8000","User-Agent":"curl/7.88.1"},"remote_addr":"127.0.0.1","x_forwarded_for":null}


host01:~$ curl -H "X-Forwarded-For: 1.2.3.4"      http://localhost:8000
{"headers":{"Accept":"*/*","Host":"localhost:8000","User-Agent":"curl/7.88.1","X-Forwarded-For":"1.2.3.4"},"remote_addr":"127.0.0.1","x_forwarded_for":"1.2.3.4"}



собираем контейнер
sudo docker compose up -d --build


для теста после создания смотрим адресс контейнера
sudo docker inspect app | grep -w "IPAddress"





пример вывода 
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.30:80
{"headers":{"Accept":"*/*","Host":"172.30.0.30","User-Agent":"curl/8.14.1","X-Forwarded-For":", 172.30.0.1, 172.30.0.30, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":", 172.30.0.1, 172.30.0.30, 172.30.0.20"}
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.20:80
{"headers":{"Accept":"*/*","Host":"172.30.0.20","User-Agent":"curl/8.14.1","X-Forwarded-For":", 172.30.0.1, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":", 172.30.0.1, 172.30.0.20"}
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.10:80
{"headers":{"Accept":"*/*","Host":"172.30.0.10","User-Agent":"curl/8.14.1","X-Forwarded-For":", 172.30.0.1"},"remote_addr":"172.30.0.10","x_forwarded_for":", 172.30.0.1"}
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.4:8000
{"headers":{"Accept":"*/*","Host":"172.30.0.4:8000","User-Agent":"curl/8.14.1"},"remote_addr":"172.30.0.1","x_forwarded_for":null}
youruser@nginxHeaders:~/nginx-headers$ 
