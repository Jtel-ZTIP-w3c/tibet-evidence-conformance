# Implementer Guide

Build your own verifier against `vectors/*.json`.

| Level | What to implement |
|---:|---|
| v1 | content hash identity |
| v2 | sealed carrier accept/quarantine |
| v3 | continuity state transition validation |
| v4 | CBOM parent/child chain |
| v5 | snapshot restore hash comparison |
| v6 | SBOM dependency normalization |
| v7 | AI-SBOM usage event required fields |
| v8 | trail query selection |
| v9 | report required-reference check |

Do not import `ref/verify_all.py` and call that interop.
