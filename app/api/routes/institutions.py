from fastapi import APIRouter, Body, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from typing import Optional
from pydantic import Field
from ofxtools.Client import OFXClient

from app.models.schemas.institutions import Institution, ListOfInstitutions, ConnectInstitution, ConnectInstitutionResponse

router = APIRouter()


# yapf: disable
@router.post("",
    response_model=ListOfInstitutions,
    name="institutions:get_institution"
)
async def get_institution(
    id: Optional[int] = None
) -> ListOfInstitutions:
    ints = [
        Institution(id=10,
                    url="http://test.com",
                    name="Name of Inst",
                    fid_id=23882,
                    fid_org="BANK ORG"),
        Institution(id=20,
                    url="http://test2.com",
                    name="Name of Inst2",
                    fid_id=54354,
                    fid_org="BANK ORG2")
    ]

    found = [x for x in ints if x.id_ == id]

    if (not found):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Institution does not exist"
        )
    else:
        ints = found


    return ListOfInstitutions(institutions=ints)

@router.post("/connect",
    response_model=ConnectInstitutionResponse,
    name="institutions:connect"
)
async def connect_institution(
    institution: ConnectInstitution
) -> ConnectInstitutionResponse:

    client = OFXClient(
        url=institution.url,
        appid=institution.app_id,
        appver=institution.app_ver,
        language=institution.language,
        userid=institution.username,
        org=institution.fi_org,
        fid=institution.fi_id,
        version=institution.ofx_version,
        bankid=institution.bank_id,
        brokerid=institution.broker_id,
        clientuid=institution.client_uuid,
        close_elements=institution.close_elements
    )

    data = (client.request_accounts(
                password=institution.password,
                dtacctup=institution.datetime_request
            ).read()).decode('UTF-8')

    return ConnectInstitutionResponse(ofx_data=data)
