from enum import Enum
from pydantic import BaseModel

class RSVPStatus(str, Enum):
    going = "Going"
    maybe = "Maybe"
    not_going = "NotGoing"

class RSVP(BaseModel):
    name: str
    event_id: int
    status: RSVPStatus