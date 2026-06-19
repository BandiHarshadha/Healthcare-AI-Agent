def triage_agent(symptoms: str):
    emergency_keywords = [
        "chest pain",
        "breathing difficulty",
        "unconscious",
        "severe bleeding",
        "stroke",
        "heart attack",
        "suicide",
        "seizure"
    ]

    symptoms_lower = symptoms.lower()

    for keyword in emergency_keywords:
        if keyword in symptoms_lower:
            return {
                "risk": "HIGH",
                "message": "Emergency symptoms detected. Please contact emergency services or visit the nearest hospital immediately."
            }

    return {
        "risk": "NORMAL",
        "message": "No emergency symptoms detected. Continue with symptom analysis."
    }