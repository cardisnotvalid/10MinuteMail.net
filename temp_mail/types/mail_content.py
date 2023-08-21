from pydantic import BaseModel
from typing import List, Union


class MailContentBody(BaseModel):
    content:    str = None
    charset:    str = None
    bodylength: int = None
    body: Union[str, None] = None


class MailContent(BaseModel):
    from_:      str = None
    gravatar:   str = None
    subject:    str = None
    datetime:   str = None
    timestamp:  int = None
    datetime2:  str = None
    urls: List[str] = None
    body: Union[str, None] = None
    attachment: List[str] = None
    html: List[str] = None