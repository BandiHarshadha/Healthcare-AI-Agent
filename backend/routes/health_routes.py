from fastapi import APIRouter
from pydantic import BaseModel
import uuid
import time
import re

from agents.healthcare_graph import build_healthcare_graph
from services.uplai_service import scan_with_uplai

router = APIRouter()
healthcare_graph = build_healthcare_graph()


class SymptomRequest(BaseModel):
    name: str
    age: int
    symptoms: str


def mask_pii(text: str):
    if not text:
        return text

    # Mask phone numbers
    text = re.sub(r"\b\d{10}\b", "[REDACTED_PHONE]", text)

    # Mask emails
    text = re.sub(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "[REDACTED_EMAIL]",
        text
    )

    return text


def detect_prompt_injection(text: str):
    risky_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "developer message",
        "secret key",
        "api key",
        "bypass",
        "jailbreak"
    ]

    lowered = text.lower()
    return any(phrase in lowered for phrase in risky_phrases)


@router.post("/check")
def check_symptoms(data: SymptomRequest):
    start_time = time.time()
    trace_id = str(uuid.uuid4())

    safe_symptoms = mask_pii(data.symptoms)

    if detect_prompt_injection(safe_symptoms):
        return {
            "output": {
                "status": "blocked",
                "reason": "Unsafe instruction detected. Please enter only health-related symptoms.",
                "disclaimer": "This AI assistant does not provide a final medical diagnosis. Please consult a qualified doctor."
            },
            "trace_id": trace_id,
            "finish_reason": "blocked_prompt_injection",
            "latency_ms": round((time.time() - start_time) * 1000, 2),
            "cost_usd": 0.0
        }

    combined_text = f"""
    Patient name: [REDACTED_NAME]
    Age: {data.age}
    Symptoms: {safe_symptoms}
    """

    try:
        uplai_result = scan_with_uplai(combined_text)
    except Exception:
        uplai_result = {
            "summary": {
                "risk_level": "unknown",
                "risk_score": 0
            },
            "total_findings": 0,
            "enforcement": {
                "overall_action": "scan_failed"
            }
        }

    result = healthcare_graph.invoke({
        "name": "[REDACTED_NAME]",
        "age": data.age,
        "symptoms": safe_symptoms,
        "intake": {},
        "triage": {},
        "diagnosis": "",
        "appointment": {}
    })

    output = {
        "uplai_privacy_scan": {
            "risk_level": uplai_result.get("summary", {}).get("risk_level", "unknown"),
            "risk_score": uplai_result.get("summary", {}).get("risk_score", 0),
            "total_findings": uplai_result.get("total_findings", 0),
            "action": uplai_result.get("enforcement", {}).get("overall_action", "scan_failed")
        },
        "intake": {
            "age": data.age,
            "symptoms": safe_symptoms
        },
        "triage": result.get("triage"),
        "diagnosis": result.get("diagnosis"),
        "appointment": result.get("appointment"),
        "disclaimer": "This AI assistant does not provide a final medical diagnosis. Please consult a qualified doctor."
    }

    return {
        "output": output,
        "trace_id": trace_id,
        "finish_reason": "completed",
        "latency_ms": round((time.time() - start_time) * 1000, 2),
        "cost_usd": 0.0
    }