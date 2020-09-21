from typing import List, Optional

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from app.models.domain.institution import Institution, InstitutionBase
from app.core.helper import get_ofxdatetime


class ListOfInstitutions(BaseModel):
    institutions: List[Institution]


class ConnectInstitutionResponse(BaseModel):
    ofx_data: str


class ConnectInstitution(InstitutionBase):
    username: str
    password: str
    datetime_request: Optional[str] = get_ofxdatetime()
