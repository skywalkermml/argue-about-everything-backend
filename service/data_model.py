from enum import Enum
from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional, Any

if TYPE_CHECKING:
    from argument_analyst import ArgumentAnalyst


class SessionData(BaseModel):
    username: str
    argument_analyst: Any # Amu'ArgumentAnalyst'

    class Config:
        arbitrary_types_allowed = True




class ElaborateTypeEnum(str, Enum):
    PREMISE = "premise"
    PREMISE_CREDIT = "premise_credit"
    CONCLUSION = "conclusion"
    ASSESSMENT = "assessment"


class ElaborateReq(BaseModel):
    type: ElaborateTypeEnum
    id: Optional[int]
