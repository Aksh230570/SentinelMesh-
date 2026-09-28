# SentinelMesh

Coordinator-orchestrated multi-agent SOC platform for explainable cyber incident
investigation. Agents: triage, threat intel, vulnerability, attack mapping,
risk & compliance, report generation. Grounded via RAG on MITRE ATT&CK + NVD.

## Quickstart

    python -m venv venv
    venv\Scripts\activate          # Windows
    source venv/bin/activate         # macOS / Linux
    pip install -r requirements.txt
    copy .env.example .env           # Windows  (cp on macOS/Linux), then add your API key
    uvicorn backend.main:app --reload

Open http://127.0.0.1:8000/health - you should see {"status": "ok"}.

## Folder layout

| Folder | Purpose |
|---|---|
| data/raw, data/processed | CICIDS2017 / CSE-CIC-IDS2018 (git-ignored, too large) |
| data/knowledge | MITRE ATT&CK + NVD source files and vector store |
| ml | Baseline anomaly detection (Random Forest / Isolation Forest) |
| rag | Embedding, vector store, retrieval |
| agents | One module per agent + shared schemas.py |
| coordinator | LangGraph orchestration |
| backend | FastAPI app |
| governance | RBAC, audit trail, human-in-the-loop gate |
| dashboard | Analyst UI |
| evaluation | Metrics, RAGAS runs, comparison vs literature |

## Team conventions

- Never commit .env or datasets.
- One branch per feature (e.g. feature/triage-agent), merge via pull request.
- agents/schemas.py is the contract. Change it only after telling the team.
