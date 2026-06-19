import fitz  # PyMuPDF


def extract_text_from_pdf(file_path: str):
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()
    return text


def report_explainer_agent(report_text: str):
    if not report_text.strip():
        return {
            "summary": "No readable text found in the report.",
            "important_values": [],
            "advice": "Please upload a clear PDF report."
        }

    important_keywords = [
        "hemoglobin", "hb", "wbc", "rbc", "platelet",
        "glucose", "hba1c", "vitamin d", "vitamin b12",
        "cholesterol", "thyroid", "tsh", "creatinine"
    ]

    found = []

    lower_text = report_text.lower()

    for keyword in important_keywords:
        if keyword in lower_text:
            found.append(keyword)

    return {
        "summary": "Medical report text extracted and analyzed successfully.",
        "important_values_detected": found,
        "note": "This is a basic explanation. A doctor should review abnormal values."
    }