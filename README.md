## 10MinuteMail.net

Python API Wrapper for [10minutemail.net](https://10minutemail.net) service. 10MinuteMail is a service which lets you use anonymous emails for free.

## Installation and Running on Windows

- Install [Python 3.10](https://www.python.org/downloads/release/python-3100). Don't forget to check the box next to "Add Python to Path".
- Install [git](https://git-scm.com/download/win).
- Installing with pip:

```bash
pip install git+https://github.com/cardisnotvalid/10MinuteMail.net
```

## Запуск под Windows

- Установите [Python 3.10](https://www.python.org/downloads/release/python-3100). Не забудьте поставить галочку напротив "Add Python to Path".
- Установите [git](https://git-scm.com/download/win).
- Установка библиотеки с помощью pip:

```bash
pip install git+https://github.com/cardisnotvalid/10MinuteMail.net
```

## General Options:

- `get_email`: Получение полной информации о почте.
- `get_email_address`: Получение почты.
- `get_mailbox`: Получение входящих сообщений.
- `wait_for_message`: Ожидание входящей сообщения.
- `get_message(mail_id)`: Получение сообщения по его ID.
- `get_last_message`: Получение последнего сообщения.
- `get_left_time`: Получение оставшегося времени жизни почты.
- `reset_10_minutes`: Обновить время жизни почты до 10 минут.
- `reset_100_minutes`: Обновить время жизни почты до 100 минут.
- `generate_new_email_address`: Получение новой почты.
- `recover_email_address`: Восстановить последнюю почту.

## Sample Code

```python
from temp_mail import TempMail

tm = TempMail()
email = tm.get_email_address() # hrr37455@zslsz.com
message = tm.wait_for_message() # Waiting for message
print(message)
```