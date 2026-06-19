<div align="center">

<!-- BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Healthcare%20AI%20Agent&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Intelligent%20Multi-Agent%20Healthcare%20Assistant&descAlignY=60&descSize=18" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-FF6F00?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![Vite](https://img.shields.io/badge/Vite-5+-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](LICENSE)

<br/>

> **🩺 Your intelligent first-line healthcare companion.**  
> Analyze symptoms · Detect emergencies · Explain reports · Set medicine reminders  

<br/>

> ⚠️ **Disclaimer:** This application provides preliminary health guidance only. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional.

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works — Multi-Agent Pipeline](#-how-it-works--multi-agent-pipeline)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [API Reference](#-api-reference)
- [Example Use Cases](#-example-use-cases)
- [Future Enhancements](#-future-enhancements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

---

## 🌟 Overview

**Healthcare AI Agent** is a full-stack, AI-powered healthcare assistant built with a **LangGraph multi-agent architecture**. It streamlines health interactions by guiding users through symptom analysis, triage, specialist recommendations, medical report interpretation, and medication reminders — all in one seamless experience.

```
  Patient Input  ──►  FastAPI Backend  ──►  LangGraph Agent Pipeline  ──►  Health Summary
       │                                                                           │
       │         ┌──────────┐  ┌────────┐  ┌──────────┐  ┌─────────────┐        │
       └────────►│  Intake  │─►│ Triage │─►│Diagnosis │─►│ Appointment │────────►┘
                 └──────────┘  └────────┘  └──────────┘  └─────────────┘
                      +
             ┌─────────────────┐    ┌──────────────────┐
             │  Report Explainer│    │ Medicine Reminder │
             └─────────────────┘    └──────────────────┘
```

---

## ✨ Features

### 🔍 Symptom Checker
Collects patient details and runs them through a multi-agent pipeline to provide:
- Possible causes based on reported symptoms
- Risk-level assessment (Normal / High / Emergency)
- Clear, preliminary health guidance
- Referral advice to appropriate medical professionals

---

### 🚨 Emergency Detection
The **Triage Agent** instantly flags high-risk situations including:

| Emergency Trigger | Action |
|---|---|
| Chest pain | Immediate ER referral |
| Breathing difficulty | Immediate ER referral |
| Stroke symptoms | Immediate ER referral |
| Seizures | Immediate ER referral |
| Loss of consciousness | Immediate ER referral |
| Severe bleeding | Immediate ER referral |
| Suicidal ideation | Immediate ER referral |
| Heart attack symptoms | Immediate ER referral |

---

### 🏥 Appointment Recommendation
The **Appointment Agent** maps symptoms to the right specialist automatically:

| Symptoms | Recommended Specialist |
|---|---|
| Fever, cough | General Physician |
| Chest pain, heart-related | Cardiologist |
| Skin rash | Dermatologist |
| Stomach pain, vomiting | Gastroenterologist |
| Headache, migraine | Neurologist / General Physician |
| Other / unmatched | General Physician |

---

### 📄 Medical Report Explainer
Upload a PDF blood report and get:
- Extracted text from any standard lab report
- Detection of key health markers including:
  `Hemoglobin` · `WBC` · `RBC` · `Platelets` · `Glucose` · `HbA1c` · `Vitamin D` · `Vitamin B12` · `Cholesterol` · `Thyroid (TSH)` · `Creatinine`
- Plain-language summary with professional follow-up advice

---

### 💊 Medicine Reminder
Create personalized medication reminders by specifying:
- **Medicine Name** — e.g., Paracetamol
- **Dosage** — e.g., 500mg
- **Time** — e.g., 9:00 PM

Returns a confirmation with full reminder details and status.

---

## 🤖 How It Works — Multi-Agent Pipeline

The core of the system is a **LangGraph `StateGraph`** that passes a shared `HealthState` through four sequential agents:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        HealthState (TypedDict)                      │
│  name · age · symptoms · intake · triage · diagnosis · appointment  │
└────────────────────────────┬────────────────────────────────────────┘
                             │
             ╔═══════════════▼════════════════╗
             ║         1. INTAKE AGENT         ║
             ║  Collects & validates patient   ║
             ║  name, age, and symptoms        ║
             ╚═══════════════╤════════════════╝
                             │
             ╔═══════════════▼════════════════╗
             ║         2. TRIAGE AGENT         ║
             ║  Scans for emergency keywords   ║
             ║  → HIGH RISK or NORMAL          ║
             ╚═══════════════╤════════════════╝
                             │
             ╔═══════════════▼════════════════╗
             ║        3. DIAGNOSIS AGENT       ║
             ║  Pattern-matches symptoms to    ║
             ║  possible preliminary causes    ║
             ╚═══════════════╤════════════════╝
                             │
             ╔═══════════════▼════════════════╗
             ║       4. APPOINTMENT AGENT      ║
             ║  Recommends specialist and      ║
             ║  booking priority               ║
             ╚═══════════════╤════════════════╝
                             │
                         ┌───▼───┐
                         │  END  │
                         └───────┘
```

**Standalone Services (outside the graph):**

| Service | Input | Output |
|---|---|---|
| `report_explainer_agent` | Uploaded PDF | Extracted markers + summary |
| `medicine_reminder_agent` | Medicine name, dosage, time | Confirmation message |

---

## 🛠️ Tech Stack

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
<th>Purpose</th>
</tr>
<tr>
<td><b>Frontend</b></td>
<td>React 18 + Vite + Axios</td>
<td>Interactive UI, API calls, file uploads</td>
</tr>
<tr>
<td><b>Backend</b></td>
<td>Python + FastAPI + Uvicorn</td>
<td>REST API, routing, CORS, file handling</td>
</tr>
<tr>
<td><b>Agent Framework</b></td>
<td>LangGraph + LangChain + OpenAI</td>
<td>Multi-agent orchestration pipeline</td>
</tr>
<tr>
<td><b>PDF Processing</b></td>
<td>PyMuPDF (fitz) + pdfplumber</td>
<td>Text extraction from medical reports</td>
</tr>
<tr>
<td><b>Vector Store</b></td>
<td>ChromaDB</td>
<td>Future RAG / knowledge retrieval</td>
</tr>
<tr>
<td><b>Config</b></td>
<td>python-dotenv + Pydantic</td>
<td>Environment variables, data validation</td>
</tr>
<tr>
<td><b>Dev Tools</b></td>
<td>Git + GitHub + ESLint</td>
<td>Version control, code quality</td>
</tr>
</table>

---

## 📂 Project Structure

```
Healthcare-AI-Agent/
│
├── backend/                          # FastAPI application
│   ├── agents/                       # Multi-agent logic
│   │   ├── healthcare_graph.py       # LangGraph StateGraph pipeline
│   │   ├── intake_agent.py           # Patient data collection
│   │   ├── triage_agent.py           # Emergency keyword detection
│   │   ├── diagnosis_agent.py        # Symptom pattern matching
│   │   ├── appointment_agent.py      # Specialist recommendation
│   │   ├── report_explainer_agent.py # PDF report analysis
│   │   ├── medicine_reminder_agent.py# Medication reminder creation
│   │   ├── gemini_diagnosis_agent.py # (Experimental) Gemini integration
│   │   └── gemini_diagnosis.py       # Gemini helper utilities
│   │
│   ├── routes/                       # API route handlers
│   │   ├── health_routes.py          # /api/health/* endpoints
│   │   ├── report_routes.py          # /api/report/* endpoints
│   │   └── medicine_routes.py        # /api/medicine/* endpoints
│   │
│   ├── services/                     # External service integrations
│   │   └── uplai_service.py
│   │
│   ├── uploads/                      # Temporary upload storage
│   ├── main.py                       # FastAPI app entry point
│   └── requirements.txt              # Python dependencies
│
├── frontend/                         # React application
│   ├── src/
│   │   ├── App.jsx                   # Main application component
│   │   ├── App.css                   # Application styles
│   │   ├── main.jsx                  # React entry point
│   │   └── assets/                   # Static assets
│   │
│   ├── public/                       # Public assets
│   ├── index.html                    # HTML shell
│   ├── package.json                  # Node dependencies
│   └── vite.config.js                # Vite build config
│
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

| Tool | Version | Check |
|---|---|---|
| Python | 3.11+ | `python --version` |
| Node.js | 18+ | `node --version` |
| npm | 9+ | `npm --version` |
| Git | Any | `git --version` |

You'll also need an **OpenAI API key** for LangGraph/LangChain agents.

---

### Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/BandiHarshadha/Healthcare-AI-Agent.git
cd Healthcare-AI-Agent

# 2. Navigate to backend
cd backend

# 3. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create a .env file and add your API key
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env

# 6. Start the backend server
python -m uvicorn main:app --reload
```

✅ Backend runs at: **http://127.0.0.1:8000**  
📚 Swagger Docs: **http://127.0.0.1:8000/docs**  
🔁 ReDoc: **http://127.0.0.1:8000/redoc**

---

### Frontend Setup

```bash
# Open a new terminal from the project root
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

✅ Frontend runs at: **http://localhost:5173**

---

## 📡 API Reference

### Health Routes — `/api/health`

| Method | Endpoint | Description | Body |
|---|---|---|---|
| `POST` | `/api/health/check` | Run full multi-agent symptom analysis | `{ name, age, symptoms }` |

**Request:**
```json
{
  "name": "Rahul",
  "age": 25,
  "symptoms": "fever, cough, headache"
}
```

**Response:**
```json
{
  "intake": { "name": "Rahul", "age": 25, "symptoms": "fever, cough, headache" },
  "triage": { "risk": "NORMAL", "message": "No emergency symptoms detected." },
  "diagnosis": "Possible viral infection, flu, or respiratory infection. Consult a doctor if symptoms continue.",
  "appointment": {
    "priority": "Normal",
    "department": "General Physician",
    "suggestion": "Book an appointment with a General Physician."
  }
}
```

---

### Report Routes — `/api/report`

| Method | Endpoint | Description | Body |
|---|---|---|---|
| `POST` | `/api/report/upload` | Upload a PDF lab report for analysis | `multipart/form-data` (file) |

**Response:**
```json
{
  "summary": "Medical report text extracted and analyzed successfully.",
  "important_values_detected": ["hemoglobin", "glucose", "hba1c", "cholesterol"],
  "note": "This is a basic explanation. A doctor should review abnormal values."
}
```

---

### Medicine Routes — `/api/medicine`

| Method | Endpoint | Description | Body |
|---|---|---|---|
| `POST` | `/api/medicine/reminder` | Create a medicine reminder | `{ medicine_name, dosage, time }` |

**Response:**
```json
{
  "medicine_name": "Paracetamol",
  "dosage": "500mg",
  "time": "9:00 PM",
  "reminder_message": "Reminder set: Take 500mg of Paracetamol at 9:00 PM.",
  "status": "Reminder created successfully."
}
```

---

## 💡 Example Use Cases

<details>
<summary><b>Example 1: Symptom Analysis — Viral Infection</b></summary>

**Input:**
```
Name: Rahul  |  Age: 25  |  Symptoms: fever, cough, headache
```

**Output:**
- ✅ **Triage:** NORMAL — No emergency detected
- 🩺 **Diagnosis:** Possible viral infection, flu, or respiratory infection
- 🏥 **Appointment:** General Physician (Normal priority)

</details>

<details>
<summary><b>Example 2: Emergency Detection — Chest Pain</b></summary>

**Input:**
```
Name: Ananya  |  Age: 45  |  Symptoms: chest pain and breathing difficulty
```

**Output:**
- 🚨 **Triage:** HIGH RISK — Emergency symptoms detected
- 🏥 **Appointment:** Emergency / ER (Emergency priority)
- ⚡ **Action:** Visit the nearest hospital immediately

</details>

<details>
<summary><b>Example 3: Medical Report Upload</b></summary>

**Input:** Upload blood_report.pdf

**Output:**
```json
{
  "summary": "Medical report text extracted and analyzed successfully.",
  "important_values_detected": ["hemoglobin", "glucose", "vitamin b12", "tsh"],
  "note": "A doctor should review any abnormal values."
}
```

</details>

<details>
<summary><b>Example 4: Medicine Reminder</b></summary>

**Input:**
```
Medicine: Paracetamol  |  Dosage: 500mg  |  Time: 9:00 PM
```

**Output:**
```
✅ Reminder set: Take 500mg of Paracetamol at 9:00 PM.
   Status: Reminder created successfully.
```

</details>

---

## 🔮 Future Enhancements

The following improvements are planned for future versions:

| Feature | Description |
|---|---|
| 🤖 **Gemini / GPT-4 Diagnosis** | LLM-powered diagnosis via Gemini Pro or GPT-4 |
| 📚 **RAG Integration** | Retrieval-Augmented Generation with medical knowledge bases |
| 🔐 **User Authentication** | JWT-based login, registration, and session management |
| 🗄️ **PostgreSQL Database** | Persistent storage for patient history and reminders |
| 🔔 **Real-Time Notifications** | Push/email/SMS medicine reminders via background scheduler |
| 📷 **OCR for Scanned Reports** | Tesseract-based OCR for image PDFs |
| ☁️ **Cloud Deployment** | Docker + AWS / GCP / Railway deployment |
| 🎨 **Enhanced UI/UX** | Dashboard, health timeline, dark mode |
| 🌐 **Multi-language Support** | Hindi, Telugu, and regional language interfaces |
| 📊 **Health Analytics** | Track symptom trends and vitals over time |

---

## 🎯 Learning Outcomes

This project demonstrates hands-on experience with:

- ✅ **Multi-Agent Systems** — Designing stateful LangGraph pipelines
- ✅ **Healthcare AI** — Building responsible, safety-first health tools
- ✅ **FastAPI Development** — REST APIs, file uploads, CORS, routing
- ✅ **React + Vite** — Modern frontend development with hooks and Axios
- ✅ **Frontend–Backend Integration** — Full-stack JSON API consumption
- ✅ **PDF Processing** — Text extraction with PyMuPDF
- ✅ **Agent Orchestration** — LangGraph `StateGraph`, node design, edge routing
- ✅ **Software Architecture** — Separation of concerns, modular agent design
- ✅ **Git & GitHub** — Version control and collaborative workflows
- ✅ **End-to-End AI Apps** — Connecting LLMs to real-world interfaces

---

## 📜 License

This project is developed for **educational and learning purposes**. Feel free to fork, study, and build upon it — just give credit where it's due.

---

## 👩‍💻 Author

<div align="center">

**B Harshadha**

[![GitHub](https://img.shields.io/badge/GitHub-BandiHarshadha-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BandiHarshadha)

*Building intelligent systems, one agent at a time.*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
