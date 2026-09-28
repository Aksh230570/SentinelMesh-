# Shared contract for every agent. Inputs and outputs are defined here so each
# teammate can build their agent independently and the coordinator can merge
# them without surprises. Change this file only after agreeing as a team.

from typing import List, Optional, Literal
from pydantic import BaseModel, Field

Level = Literal["low", "medium", "high", "critical"]


class Alert(BaseModel):
    alert_id: str
    timestamp: str
    source_ip: str
    dest_ip: Optional[str] = None
    host: str
    event_summary: str
    raw_features: dict = Field(default_factory=dict)
    asset_criticality: Optional[Literal["low", "medium", "high"]] = None


class Citation(BaseModel):
    source: str                 # e.g. "MITRE ATT&CK", "NVD", "OTX"
    reference_id: str           # e.g. "T1110", "CVE-2023-41892"
    snippet: Optional[str] = None


class TriageOutput(BaseModel):
    verdict: Literal["discard", "monitor", "escalate"]
    priority: Level
    confidence: float
    reasoning: str


class ThreatIntelOutput(BaseModel):
    indicator: str
    reputation: Literal["clean", "suspicious", "malicious", "unknown"]
    campaign: Optional[str] = None
    confidence: float
    citations: List[Citation] = Field(default_factory=list)


class VulnerabilityOutput(BaseModel):
    asset: str
    cve_ids: List[str] = Field(default_factory=list)
    max_cvss: Optional[float] = None
    patch_status: Literal["patched", "unpatched", "unknown"] = "unknown"
    exploit_available: Optional[bool] = None
    citations: List[Citation] = Field(default_factory=list)


class AttackMappingOutput(BaseModel):
    techniques: List[str]       # e.g. ["T1110", "T1046"]
    tactic: Optional[str] = None
    confidence: float
    citations: List[Citation] = Field(default_factory=list)


class RiskOutput(BaseModel):
    score: Level
    compliance_flags: List[str] = Field(default_factory=list)   # e.g. ["ISO27001 A.9"]
    basis: str
    decision_path: Literal["auto_remediate_pending_approval", "escalate_to_human"]
    escalate_to: Optional[str] = None                           # role, if escalating


class InvestigationReport(BaseModel):
    alert: Alert
    triage: TriageOutput
    threat_intel: ThreatIntelOutput
    vulnerability: VulnerabilityOutput
    attack_mapping: AttackMappingOutput
    risk: RiskOutput
    summary: str
    recommended_actions: List[str]
