# Инструкция запуска
### скачиваем реепозиторий 
sudo apt install git
git clone https://github.com/ben19f/nginx-headers.git 


### для настройки серверов запустите плейбук (если надо предварительно настроить ставим ансибл и запускаем)
##### (введи нужные адреса ssh-key и серверов в инвентори файле)
ansible-playbook -i inventory.ini proxmox-preparing.yml


## приложение реализовано на питоне

### локальный тест скрипта
###### (образец моего вывода)
host01:~$ curl http://localhost:8000
{"headers":{"Accept":"*/*","Host":"localhost:8000","User-Agent":"curl/7.88.1"},"remote_addr":"127.0.0.1","x_forwarded_for":null}


host01:~$ curl -H "X-Forwarded-For: 1.2.3.4"      http://localhost:8000
{"headers":{"Accept":"*/*","Host":"localhost:8000","User-Agent":"curl/7.88.1","X-Forwarded-For":"1.2.3.4"},"remote_addr":"127.0.0.1","x_forwarded_for":"1.2.3.4"}




# Cобираем контейнеры
cd nginx-headers

## запуск контейнеров
sudo docker compose up -d --build


### реализована следующая схема
client → nginx1 → app
client → nginx2 → nginx1 → app
client → nginx3 → nginx2 → nginx1 → app





### пример вывода  с хост машины без подделки заголовка
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.30:80
{"headers":{"Accept":"*/*","Host":"172.30.0.30","User-Agent":"curl/8.14.1","X-Forwarded-For":", 172.30.0.1, 172.30.0.30, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":", 172.30.0.1, 172.30.0.30, 172.30.0.20"}
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.20:80
{"headers":{"Accept":"*/*","Host":"172.30.0.20","User-Agent":"curl/8.14.1","X-Forwarded-For":", 172.30.0.1, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":", 172.30.0.1, 172.30.0.20"}
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.10:80
{"headers":{"Accept":"*/*","Host":"172.30.0.10","User-Agent":"curl/8.14.1","X-Forwarded-For":", 172.30.0.1"},"remote_addr":"172.30.0.10","x_forwarded_for":", 172.30.0.1"}
youruser@nginxHeaders:~/nginx-headers$ curl http://172.30.0.4:8000
{"headers":{"Accept":"*/*","Host":"172.30.0.4:8000","User-Agent":"curl/8.14.1"},"remote_addr":"172.30.0.1","x_forwarded_for":null}
youruser@nginxHeaders:~/nginx-headers$ 


### пример вывода с ДОВЕРЕННОЙ машины с подделкой заголовка
youruser@nginxHeaders:~/nginx-headers$ curl -H "X-Forwarded-For: 1.2.3.4"   http://localhost:8082
{"headers":{"Accept":"*/*","Host":"localhost","User-Agent":"curl/8.14.1","X-Forwarded-For":"1.2.3.4, 172.30.0.1, 172.30.0.30, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":"1.2.3.4, 172.30.0.1, 172.30.0.30, 172.30.0.20"}
youruser@nginxHeaders:~/nginx-headers$ curl -H "X-Forwarded-For: 1.2.3.4"   http://localhost:8081
{"headers":{"Accept":"*/*","Host":"localhost","User-Agent":"curl/8.14.1","X-Forwarded-For":"1.2.3.4, 172.30.0.1, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":"1.2.3.4, 172.30.0.1, 172.30.0.20"}
youruser@nginxHeaders:~/nginx-headers$ curl -H "X-Forwarded-For: 1.2.3.4"   http://localhost:8080
{"headers":{"Accept":"*/*","Host":"localhost","User-Agent":"curl/8.14.1","X-Forwarded-For":"1.2.3.4, 172.30.0.1"},"remote_addr":"172.30.0.10","x_forwarded_for":"1.2.3.4, 172.30.0.1"}


### пример с НЕдоверенной машины с подделкой заголовка 
ben@host01:~$ curl -H "X-Forwarded-For: 1.2.3.4"   http://192.168.91.5:8081
{"headers":{"Accept":"*/*","Host":"192.168.91.5","User-Agent":"curl/7.88.1","X-Forwarded-For":"192.168.91.10, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":"192.168.91.10, 172.30.0.20"}
ben@host01:~$ curl -H "X-Forwarded-For: 1.2.3.4"   http://192.168.91.5:8082
{"headers":{"Accept":"*/*","Host":"192.168.91.5","User-Agent":"curl/7.88.1","X-Forwarded-For":"192.168.91.10, 172.30.0.30, 172.30.0.20"},"remote_addr":"172.30.0.10","x_forwarded_for":"192.168.91.10, 172.30.0.30, 172.30.0.20"}
ben@host01:~$ curl -H "X-Forwarded-For: 1.2.3.4"   http://192.168.91.5:8080
{"headers":{"Accept":"*/*","Host":"192.168.91.5","User-Agent":"curl/7.88.1","X-Forwarded-For":"192.168.91.10"},"remote_addr":"172.30.0.10","x_forwarded_for":"192.168.91.10"}
ben@host01:~$ 
