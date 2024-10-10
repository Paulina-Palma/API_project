from fastapi import APIRouter, UploadFile


router = APIRouter(
    prefix='/attachments',
    tags=['attachments']
)


@router.post('/files')
async def create_upload_file(file: UploadFile):
    with open(file.filename, 'wb') as handler:
        handler.write(await file.read())

    return {'filename': file.filename, 'Content-Type': file.content_type}


# odbiera od razu całość
# @router.post('/files')
# async def create_upload_file(file: UploadFile):
#     return {'filename': file.filename, 'Content-Type': file.content_type}


# to niestety zapycha pamięć
# from fastapi import APIRouter, File
#
# router = APIRouter(
#     prefix='/attachments',
#     tags=['attachments']
# )
#
#
# @router.post('/files')
# async def upload_file(file: bytes = File()):
#     return {'file_size': len(file)}
