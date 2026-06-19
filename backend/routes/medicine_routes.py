from fastapi import APIRouter
from pydantic import BaseModel
from agents.medicine_reminder_agent import medicine_reminder_agent

router = APIRouter()


class MedicineRequest(BaseModel):
    medicine_name: str
    dosage: str
    time: str


@router.post("/reminder")
def create_medicine_reminder(data: MedicineRequest):
    reminder = medicine_reminder_agent(
        data.medicine_name,
        data.dosage,
        data.time
    )

    return reminder