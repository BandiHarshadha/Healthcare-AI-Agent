def diagnosis_agent(symptoms: str):
    symptoms_lower = symptoms.lower()

    if "fever" in symptoms_lower and "cough" in symptoms_lower:
        return "Possible viral infection, flu, or respiratory infection. Consult a doctor if symptoms continue."

    if "headache" in symptoms_lower:
        return "Possible stress, migraine, dehydration, or fever-related headache."

    if "stomach pain" in symptoms_lower:
        return "Possible indigestion, acidity, infection, or other abdominal issue. Medical consultation is recommended."

    return "Symptoms need further medical review. Please consult a healthcare professional."