from typing import List, Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class InstitutionBase(BaseModel):
    url: str
    ofx_version: Optional[int] = None
    app_id: Optional[str] = None
    app_ver: Optional[str] = None
    fi_id: Optional[str] = None
    fi_org: Optional[str] = None
    language: Optional[str] = None
    client_uuid: Optional[str] = None
    bank_id: Optional[str] = None
    broker_id: Optional[str] = None
    close_elements: Optional[bool] = None


class Institution(InstitutionBase, IDModelMixin, DateTimeModelMixin):
    name: str
    description: Optional[str] = None
    enabled: Optional[bool] = True
