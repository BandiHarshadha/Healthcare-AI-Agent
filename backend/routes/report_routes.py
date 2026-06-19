import os
import shutil
from fastapi import APIRouter, UploadFile, File
from agents.report_explainer_agent import extract_text_from_pdf, report_explainer_agent

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
def upload_report(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    report_text = extract_text_from_pdf(file_path)
    explanation = report_explainer_agent(report_text)

    return {
        "filename": file.filename,
        "explanation": explanation
    }