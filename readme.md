# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к бд, но можете свободно использовать код верстки для просмотра как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.

  ## Как установить


  - ***Операционная система:***  
    - Windows 10 или новее
    - macOS 10.14 или новее
    - Linux (разные дистрибутивы)

  - ***Язык программирования:***  
    - Python 3.8 или новее


  ## Установка окружения

  1. Склонируйте репозиторий:
   [link](https://github.com/ArtyomRom/django-orm-watching-storage.git)

  2. Создайте виртуальное окружение:
        ```bash
        python -m venv venv
        ```

  3. Активируйте виртуальное окружение:
   
    - На Windows:
      ```bash
      venv\Scripts\activate
      ```
    - На macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

  4. Установите зависимости:
    ```bash
       pip install -r requirements.txt
    ```
  5.  Настройки проекта

Этот проект использует файл `.env` для хранения конфигурационных переменных среды. Ниже представлен список основных переменных, которые вы можете настроить:

### Переменные окружения

- **SECRET_KEY**: Это строка, используемая для обеспечения безопасности вашего приложения. Она необходима для шифрования данных.

- **DB_ENGINE**: Определяет тип базы данных, которую использует ваше приложение.

- **DB_HOST**: Это адрес хоста для вашей базы данных.

- **DB_PORT**: Порт, на котором работает база данных.

- **DB_NAME**: Имя вашей базы данных. 

- **DB_USER**: Имя пользователя, которое используется для подключения к базе данных. 

- **DB_PASSWORD**: Пароль для пользователя базы данных. 

- **ALLOWED_HOSTS**: Список доменных имен или IP-адресов, с которых ваше приложение может принимать запросы. 

- **DEBUG**: Определяет, включен ли режим отладки. Если установлено в True, приложение будет выводить детализированные ошибки и отладочную информацию. 


  6. Запустите проект:
    ```bash
       python manage.py runserver 0.0.0.0:8000
    ```