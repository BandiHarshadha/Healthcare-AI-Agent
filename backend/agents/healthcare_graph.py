from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.intake_agent import intake_agent
from agents.triage_agent import triage_agent
from agents.diagnosis_agent import diagnosis_agent
from agents.appointment_agent import appointment_agent


class HealthState(TypedDict):
    name: str
    age: int
    symptoms: str
    intake: dict
    triage: dict
    diagnosis: str
    appointment: dict


def intake_node(state: HealthState):
    state["intake"] = intake_agent(
        state["name"],
        state["age"],
        state["symptoms"]
    )
    return state


def triage_node(state: HealthState):
    state["triage"] = triage_agent(state["symptoms"])
    return state


def diagnosis_node(state: HealthState):
    state["diagnosis"] = diagnosis_agent(state["symptoms"])
    return state


def appointment_node(state: HealthState):
    state["appointment"] = appointment_agent(
        state["symptoms"],
        state["triage"]
    )
    return state


def build_healthcare_graph():
    graph = StateGraph(HealthState)

    graph.add_node("intake", intake_node)
    graph.add_node("triage", triage_node)
    graph.add_node("diagnosis", diagnosis_node)
    graph.add_node("appointment", appointment_node)

    graph.set_entry_point("intake")

    graph.add_edge("intake", "triage")
    graph.add_edge("triage", "diagnosis")
    graph.add_edge("diagnosis", "appointment")
    graph.add_edge("appointment", END)

    return graph.compile()