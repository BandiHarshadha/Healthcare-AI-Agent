def appointment_agent(symptoms: str, triage: dict):
    symptoms_lower = symptoms.lower()

    if triage.get("risk") == "HIGH":
        return {
            "priority": "Emergency",
            "department": "Emergency / ER",
            "suggestion": "Visit the nearest hospital immediately."
        }

    if "chest pain" in symptoms_lower or "heart" in symptoms_lower:
        department = "Cardiologist"
    elif "skin" in symptoms_lower or "rash" in symptoms_lower:
        department = "Dermatologist"
    elif "stomach" in symptoms_lower or "vomit" in symptoms_lower:
        department = "Gastroenterologist"
    elif "fever" in symptoms_lower or "cough" in symptoms_lower:
        department = "General Physician"
    elif "headache" in symptoms_lower or "migraine" in symptoms_lower:
        department = "Neurologist / General Physician"
    else:
        department = "General Physician"

    return {
        "priority": "Normal",
        "department": department,
        "suggestion": f"Book an appointment with a {department}."
    }