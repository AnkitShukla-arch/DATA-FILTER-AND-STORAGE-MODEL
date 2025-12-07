<h1 align="center">🚀 DATA-FILTER-AND-STORAGE-MODEL</h1>


<p align="center">
  <img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg" alt="GitHub Snake Animation" width="100%">
</p>

---

## 📌 Overview

A modular, production-focused data filtering and storage engine designed to **ingest → clean → classify → store** heterogeneous datasets.

---

## 🧩 Key Features

* **Unified Ingestion Layer** for CSV / JSON / Logs.
* **Deterministic Cleaning Engine** with configurable missing-value policy.
* **Threat-Class Filtering** (IP / fingerprint / anomaly extraction).
* **Isolated Storage Layer** (clean vs suspicious datasets).
* **Stateless, Reproducible, Modular** code structure.

---

## 🏗 Architecture

```
modules/
│
├── cleansing.py      # normalization, NaN policies, formatting
├── filtering.py      # IP extraction, suspicious pattern isolation
├── storage.py        # file output, directory handling
└── utils.py          # helpers, constants

main.py               # pipeline orchestrator
```

Pipeline:

```
Raw Input → Validation → Cleansing → Threat Filtering → Storage
```

---

## 🔧 Configuration Philosophy

Minimal interfaces. Explicit behavior. No silent assumptions.

### Cleaning Policies

```
Categorical NaN → "Unknown"
Numeric NaN      → "DummyValue"
Whitespace Trim  → Enabled
Case Normalization → Enabled
```

### Filtering Rules

```
IP Regex:        Enabled
Fingerprint Scan: Enabled
Suspicious Log Isolation: Enabled
```

---

## 🚀 Usage

### Install

```
pip install -r requirements.txt
```

### Run Pipeline

```
python main.py
```

### Outputs

```
data/cleaned_output.csv
data/suspicious_output.csv
```

---

## 🧪 Sample Flow (Reference)

```
[INPUT]   → raw_data.csv
[CLEAN]   → normalized fields / NaN resolved
[FILTER]  → 32 items flagged as suspicious
[STORE]   → cleaned_output.csv / suspicious_output.csv
```

---

## 🧠 Design Principles

* **Determinism** → Same input = same output.
* **Isolation** → Cleaning and filtering are orthogonal.
* **Observability‑Ready** → Functions structured for logging integration.
* **Replaceable Modules** → Swap any stage without redesign.

---

## 📦 Potential Extensions

* FastAPI service layer
* Kafka or Kinesis ingestion
* ML-based anomaly detection
* Integration with Airflow / Prefect
* PostgreSQL / MinIO storage backend

---

<h3 align="center">🌐 Connect With Me</h3>

<p align="center">
  <a href="monishukla727538@gmail.com">
    <img src="https://img.shields.io/badge/Contact%20HQ-Email%20Now-00FFFF?style=for-the-badge&logo=gmail&logoColor=black" />
  </a>
  <a href="https://www.linkedin.com/in/ankit-shukla-877705285/">
    <img src="https://img.shields.io/badge/LinkedIn-Connected-ff007f?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/AnkitShukla-arch">
    <img src="https://img.shields.io/badge/GitHub-Repository-7fff00?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>



