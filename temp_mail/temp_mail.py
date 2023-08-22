import time
import json
import requests

from typing import List, Dict, Union
from .types.mail_content import MailContent
from .types.mail_response import MailResponse
from .mail_exceptions import APIError, TimeoutError


class TempMail:
    base_url = "https://10minutemail.net/"
    
    def __init__(self):
        self._session = requests.Session()

    def _response(self) -> MailResponse | None:
        response = self._session.get(self.base_url + "address.api.php")
        if response.status_code != 200:
            raise APIError(response.status_code, "Failed to get response data")
        
        json_data = json.loads(response.text)
        permalink = {
            key: json_data["permalink"][key] 
            for key in json_data["permalink"].keys()
        }
        mail_list = [
            {key: item[key] for key in item.keys()} 
            for item in json_data["mail_list"]
        ]
        data = {key: json_data[key] for key in json_data.keys()}
        data.update(permalink=permalink, mail_list=mail_list)
        return MailResponse(**data)

    def _content(self, params: Dict[str, str]) -> MailContent | None:
        response = self._session.get(self.base_url + "mail.api.php", params=params)
        if response.status_code != 200:
            raise APIError(response.status_code, "Failed to get content data")
        
        json_data = json.loads(response.text)
        json_data["from_"] = json_data["from"]
        return MailContent(**json_data)
        
    def get_email(self) -> MailResponse | None:
        return self._response()
    
    def get_mailbox(self) -> List[Union[str, None]]:
        return [
            self.get_message(mail_info.mail_id).body 
            for mail_info in self._response().mail_list
        ]
    
    def get_message(self, mail_id: str) -> MailContent | None:
        return self._content(params={"mailid": mail_id})
    
    def get_last_message(self) -> MailContent | None:
        mail_id = self._response().mail_list[0].mail_id
        if mail_id != "welcome":
            return self.get_message(mail_id)
        else:
            return None
    
    def wait_for_message(self, timeout: int = 10) -> str:
        timeout_time = 1
        while timeout > timeout_time:
            email = self.get_last_email()
            if email: 
                return email.body[0].body
            timeout_time += 1
            time.sleep(1)
        TimeoutError("Timed out waiting for message")
    
    def get_email_address(self) -> str:
        return self._response().mail_get_mail
    
    def get_left_time(self) -> int:
        return self._response().mail_left_time
    
    def reset_10_minutes(self) -> None:
        self._session.get(self.base_url + "more.html")

    def reset_100_minutes(self) -> None:
        self._session.get(self.base_url + "more100.html")

    def generate_new_email_address(self) -> None:
        self._session.get(self.base_url + "new.html")

    def recover_email_address(self) -> None:
        self._session.get(self.base_url + "recover.html")
