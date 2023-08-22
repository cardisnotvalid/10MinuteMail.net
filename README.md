## 10MinuteMail.net

Python API Wrapper for [10minutemail.net](https://10minutemail.net) service. 10MinuteMail is a service which lets you use anonymous emails for free.

## Installation and Running on Windows

- Install [Python 3.10](https://www.python.org/downloads/release/python-3100). Don't forget to check the box next to "Add Python to Path".
- Install [git](https://git-scm.com/download/win).
- Installing with pip:

```bash
pip install git+https://github.com/cardisnotvalid/10MinuteMail.net
```

## Example

```python
from temp_mail import TempMail

tm = TempMail()
email = tm.get_email_address() # hrr37455@zslsz.com
message = tm.wait_for_message() # Waiting for message

```

## Запуск под Windows

- Установите [Python 3.10](https://www.python.org/downloads/release/python-3100). Не забудьте поставить галочку напротив "Add Python to Path".
- Установите [git](https://git-scm.com/download/win).
- Установка библиотеки с помощью pip:

```bash
pip install git+https://github.com/cardisnotvalid/10MinuteMail.net
```

## Пример

```python
from temp_mail import TempMail

tm = TempMail()
email = tm.get_email_address() # hrr37455@zslsz.com
message = tm.wait_for_message() # Waiting for message

```