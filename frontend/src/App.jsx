import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    name: "",
    age: "",
    symptoms: ""
  });

  const [medicineForm, setMedicineForm] = useState({
    medicine_name: "",
    dosage: "",
    time: ""
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const [file, setFile] = useState(null);
  const [reportResult, setReportResult] = useState(null);
  const [medicineResult, setMedicineResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleMedicineChange = (e) => {
    setMedicineForm({ ...medicineForm, [e.target.name]: e.target.value });
  };

  const checkSymptoms = async () => {
    setError("");
    setResult(null);

    try {
      const res = await axios.post("/api/health/check", {
        name: form.name,
        age: Number(form.age),
        symptoms: form.symptoms
      });

      setResult(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || "Something went wrong");
    }
  };

  const uploadReport = async () => {
    if (!file) {
      setError("Please select a PDF report first");
      return;
    }

    setError("");
    setReportResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("/api/report/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });

      setReportResult(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || "Report upload failed");
    }
  };

  const createMedicineReminder = async () => {
    setError("");
    setMedicineResult(null);

    try {
      const res = await axios.post("/api/medicine/reminder", {
        medicine_name: medicineForm.medicine_name,
        dosage: medicineForm.dosage,
        time: medicineForm.time
      });

      setMedicineResult(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || "Medicine reminder failed");
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h1>Healthcare AI Agent 🩺</h1>
        <p className="subtitle">
          AI-powered symptom checker, UPLAI privacy scan, report explainer, and medicine reminder
        </p>

        <section>
          <h2>Symptom Checker</h2>

          <input
            name="name"
            placeholder="Patient name"
            value={form.name}
            onChange={handleChange}
          />

          <input
            name="age"
            placeholder="Age"
            type="number"
            value={form.age}
            onChange={handleChange}
          />

          <textarea
            name="symptoms"
            placeholder="Enter symptoms, example: fever cough headache phone 9876543210"
            value={form.symptoms}
            onChange={handleChange}
          />

          <button onClick={checkSymptoms}>Analyze Symptoms</button>
        </section>

        {error && <p className="error">{JSON.stringify(error)}</p>}

        {result && (
          <div className="result">
            <h2>Health Summary</h2>

            {result.uplai_privacy_scan && (
              <>
                <h3>UPLAI Privacy Scan 🔐</h3>
                <p><b>Risk Level:</b> {result.uplai_privacy_scan.risk_level}</p>
                <p><b>Risk Score:</b> {result.uplai_privacy_scan.risk_score}</p>
                <p><b>Total Findings:</b> {result.uplai_privacy_scan.total_findings}</p>
                <p><b>Action:</b> {result.uplai_privacy_scan.action}</p>
              </>
            )}

            <h3>Patient Info</h3>
            <p><b>Name:</b> {result.intake.patient_name}</p>
            <p><b>Age:</b> {result.intake.age}</p>
            <p><b>Symptoms:</b> {result.intake.reported_symptoms}</p>

            <h3>Triage</h3>
            <p><b>Risk:</b> {result.triage.risk}</p>
            <p>{result.triage.message}</p>

            <h3>Possible Causes</h3>
            <p>{result.diagnosis}</p>

            <h3>Appointment Recommendation</h3>
            <p><b>Priority:</b> {result.appointment.priority}</p>
            <p><b>Department:</b> {result.appointment.department}</p>
            <p>{result.appointment.suggestion}</p>

            <p className="disclaimer">{result.disclaimer}</p>
          </div>
        )}

        <section className="report-box">
          <h2>Upload Medical Report 📄</h2>

          <input
            type="file"
            accept="application/pdf"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <button onClick={uploadReport}>Explain Report</button>

          {reportResult && (
            <div className="result">
              <h3>Report Explanation</h3>
              <p><b>Filename:</b> {reportResult.filename}</p>
              <p><b>Summary:</b> {reportResult.explanation.summary}</p>
              <p>
                <b>Detected Values:</b>{" "}
                {reportResult.explanation.important_values_detected?.length > 0
                  ? reportResult.explanation.important_values_detected.join(", ")
                  : "No common values detected"}
              </p>
              <p>{reportResult.explanation.note}</p>
            </div>
          )}
        </section>

        <section className="report-box">
          <h2>Medicine Reminder 💊</h2>

          <input
            name="medicine_name"
            placeholder="Medicine name, example: Paracetamol"
            value={medicineForm.medicine_name}
            onChange={handleMedicineChange}
          />

          <input
            name="dosage"
            placeholder="Dosage, example: 500mg"
            value={medicineForm.dosage}
            onChange={handleMedicineChange}
          />

          <input
            name="time"
            placeholder="Time, example: 9:00 PM"
            value={medicineForm.time}
            onChange={handleMedicineChange}
          />

          <button onClick={createMedicineReminder}>Create Reminder</button>

          {medicineResult && (
            <div className="result">
              <h3>Reminder Created</h3>
              <p><b>Medicine:</b> {medicineResult.medicine_name}</p>
              <p><b>Dosage:</b> {medicineResult.dosage}</p>
              <p><b>Time:</b> {medicineResult.time}</p>
              <p>{medicineResult.reminder_message}</p>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;