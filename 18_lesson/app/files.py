import os
import shutil

from fastapi import Depends, APIRouter, Form, File, UploadFile, HTTPException
from app.schemas import ImageProcessionOptions
from fastapi.responses import FileResponse
from app.users import current_active_user
from app.db import User
from app.utils import process_image


file_router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@file_router.post("/upload/")
async def upload_file(
        file: UploadFile = File(...),
        resize: str = Form(None),
        convert_to: str = Form(None),
        grayscale: bool = Form(None),
        flip: str = Form(None),
        user: User = Depends(current_active_user)
    ):
        options = ImageProcessionOptions(
            resize=resize,
            convert_to=convert_to,
            grayscale=grayscale,
            flip=flip
        )
        print(options)
        user_folder = f"{UPLOAD_DIR}/{user.id}"
        os.makedirs(user_folder, exist_ok=True)

        file_location = os.path.join(user_folder, file.filename)

        with open(file_location, "wb") as buffers:
            shutil.copyfileobj(file.file, buffers)

        processed_file_location = process_image(file_location, options)
        return {os.path.basename(processed_file_location), processed_file_location}

@file_router.get("/download/{filename}", response_class=FileResponse)
async def download_file(filename: str, user: User = Depends(current_active_user)):
    user_folder = f"{UPLOAD_DIR}/{user.id}"
    file_location = os.path.join(user_folder, filename)
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="file is not found")
    return FileResponse(file_location)