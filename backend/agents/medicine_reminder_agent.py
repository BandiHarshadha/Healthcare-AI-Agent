def medicine_reminder_agent(medicine_name: str, dosage: str, time: str):
    return {
        "medicine_name": medicine_name,
        "dosage": dosage,
        "time": time,
        "reminder_message": f"Reminder set: Take {dosage} of {medicine_name} at {time}.",
        "status": "Reminder created successfully."
    }