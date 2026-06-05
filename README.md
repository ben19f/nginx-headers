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
