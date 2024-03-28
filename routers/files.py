from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import File, UploadFile
from typing import List
import os

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
    compartment_ocid = os.environ['compartment_ocid']
    tmp_input_path = "tmp_inputs"
    tmp_output_path = "tmp_outputs"
    file_object = Files(tmp_input_path, tmp_output_path, compartment_ocid)
    for file in files:
        try:
            contents = file.file.read()
            with open(f"{tmp_input_path}/{file.filename}", 'wb') as f:
                f.write(contents)
                file_id, summary_text = file_object.convert_to_text(file.filename)
        except Exception as e:
            return {"message": f"There was an error uploading the file(s)- {e}"}
        finally:
            file.file.close()
    return {"message": "Successfully uploaded", "file_id": f"{file_id}", "summary": summary_text}
