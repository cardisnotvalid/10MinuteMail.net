## 10MinuteMail.net

Python API Wrapper for [10minutemail.net](https://10minutemail.net) service. 10MinuteMail is a service which lets you use anonymous emails for free.

## Installation

- Installing [Python 3.10](https://www.python.org/downloads/release/python-3100), checking "Add Python to Path".
- Installing [git](https://git-scm.com/download/win).
- Installing with pip:

```bash
pip install git+https://github.com/cardisnotvalid/10MinuteMail.net
```

## Using

```python
from temp_mail import TempMail

tm = TempMail()
email = tm.get_email_address() # hrr37455@zslsz.com
message = tm.wait_for_message() # Waiting for message

```