import binascii
from typing import Annotated

from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = file.file.read()
    return PlainTextResponse(binascii.hexlify(contents,"\n",16))
