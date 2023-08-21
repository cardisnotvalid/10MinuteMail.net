from pydantic import BaseModel
from typing import List, Union


class MailResponsePermalink(BaseModel):
    host: str = None
    mail: str = None
    url:  str = None
    key:  str = None
    time: int = None
    

class MailResponseMailList(BaseModel):
    mail_id:   str = None
    from_:     str = None
    subject:   str = None
    datetime:  str = None
    datetime2: str = None
    timeago:   Union[int, str] = None
    isread:    Union[bool, str] = None


class MailResponse(BaseModel):
    mail_get_user:    str = None
    mail_get_mail:    str = None
    mail_get_host:    str = None
    mail_get_time:    int = None
    mail_get_duetime: int = None
    mail_server_time: int = None
    mail_get_key:     str = None
    mail_left_time:   int = None
    mail_recovering_key:  Union[str, None] = None
    mail_recovering_mail: Union[str, None] = None
    session_id: str = None
    permalink: MailResponsePermalink = None
    mail_list: List[MailResponseMailList] = None