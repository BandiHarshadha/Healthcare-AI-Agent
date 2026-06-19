import requests

UPLAI_SCAN_URL = "http://localhost:3000/api/v3/scan"


def scan_with_uplai(text: str):
    try:
        response = requests.post(
            UPLAI_SCAN_URL,
            json={"text": text},
            timeout=5
        )
        return response.json()
    except Exception as e:
        return {
            "error": str(e),
            "message": "UPLAI scan failed. Make sure UPLAI is running on port 3000."
        }