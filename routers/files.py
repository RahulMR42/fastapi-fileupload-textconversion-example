from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import File, UploadFile
from typing import List

from resources.files import Files

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/files",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)

@router.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    tmp_input_path = "tmp_inputs"
    file_object = Files(tmp_input_path)

    for file in files:
        try:
            contents = file.file.read()
            with open(f"{tmp_input_path}/{file.filename}", 'wb') as f:
                f.write(contents)
                file_object.convert_to_text(file.filename)

        except Exception as e:
            return {"message": f"There was an error uploading the file(s)- {e}"}
        finally:
            file.file.close()

    return {"message": "Successfully uploaded"}
