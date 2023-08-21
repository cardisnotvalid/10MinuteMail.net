import time
import json
import requests

from typing import List, Dict
from temp_mail.types.mail_content import MailContent
from temp_mail.types.mail_response import MailResponse, MailResponseMailList


class TenMinuteMail:
    def __init__(self):
        self._session = requests.Session()

    def _response(self) -> MailResponse | None:
        url = "https://10minutemail.net/address.api.php"
        response = self._session.get(url)
        json_data = json.loads(response.text)
        json_data["mail_list"] = [
            MailResponseMailList(
                mail_id=item["mail_id"],
                from_=item["from"],
                subject=item["subject"],
                datetime=item["datetime"],
                datetime2=item["datetime2"],
                timeago=item["timeago"],
                isread=item["isread"]
            )
            for item in json_data["mail_list"]    
        ]
        try:
            return MailResponse(**json_data)
        except Exception as ex:
            print(ex)
            return None

    def _content(self, params: Dict[str, str]) -> MailContent | None:
        url = "https://10minutemail.net/mail.api.php"
        response = self._session.get(url, params=params)
        json_data = json.loads(response.text)
        json_data["from_"] = json_data["from"]
        try:
            return MailContent(**json_data)
        except Exception as ex:
            print(ex)
            return None
    
    def wait_for_message(self, timeout: int = 10):
        timeout_time = 1
        while timeout > timeout_time:
            email = self.get_last_email()
            if email:
                return email.body[0].body
            timeout_time += 1
            time.sleep(1)
        print("Timed out waiting for message")
        
    def get_email_address(self) -> MailResponse | None:
        response = self._response()
        return response
    
    def get_email_content(self, mail_id: str) -> MailContent | None:
        response = self._content(params={"mailid": mail_id})
        return response

    def get_all_email_content(self) -> List[str]:
        response = self._response()
        return [self.get_email_content(mail_info.mail_id).body for mail_info in response.mail_list]

    def get_last_email(self) -> MailContent:
        response = self._response()
        mail_id = response.mail_list[0].mail_id
        if mail_id != "welcome":
            return self.get_email_content(mail_id)
    
    def reset_10_minutes(self) -> None:
        url = "https://10minutemail.net/more.html"
        self._session.get(url)

    def reset_100_minutes(self) -> None:
        url = "https://10minutemail.net/more100.html"
        self._session.get(url)

    def generate_new_email_address(self) -> None:
        url = "https://10minutemail.net/new.html"
        self._session.get(url)

    def recover_email_address(self) -> None:
        url = "https://10minutemail.net/recover.html"
        self._session.get(url)
