from fastapi import Depends, APIRouter, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != 'fake-super-secret-token':
        raise HTTPException(status_code=400, detail='X-token header invalid')


async def verify_key(x_key: str = Header()):
    if x_key != 'fake-super-secret-key':
        raise HTTPException(status_code=400, detail='X-Key header invalid')
    return x_key


router = APIRouter(
    prefix='/tests',
    tags=['tests']
)


async def pagination(skip: int = 0, limit: int = 100):
    return {'skip': skip, 'limit': limit}


async def from_header(content_type=Header('Content-Type')):
    return {'type': content_type}


async def blocker():
    raise HTTPException(status_code=400, detail='X-token header invalid')


@router.get("/one-endpoint/")
async def one_endpoint(params: dict = Depends(pagination)):
    return params


@router.get("/second-endpoint/")
async def second_endpoint(params: dict = Depends(pagination)):
    return params
