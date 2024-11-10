# Пульт охраны банка #
Это внутренний репозиторий для сотрудников банка "Сияние".
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к у вас нет
доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованны запросы к БД.


Пульт охраны - это сайт,который можно подключить к удаленной базе данных с визитами
и карточками пропуска сотрудников нашего банка.

### Как установить ###
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
#### Вам потребуется создать в корне проекта файл '.env' и указать следующие переменные окружения: ####

DB_ENGINE - вид вашей базы данных

DB_HOST - хост для вашей базы данных

DB_PORT - порт

DB_NAME - имя базы данных

DB_USER - логи для входа в бд

DB_PASSWORD - пароль для входа в бд

SECRET_KEY - секретный ключ

ALLOWED_HOSTS - список хостов\доменов, для которых может работать данный сайт




### Цель проекта ###
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.