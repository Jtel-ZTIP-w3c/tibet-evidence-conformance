# EVIDENCE.md - TIBET Evidence Primitive Atlas

The evidence branch answers one question:

```text
Can bytes be stored, sealed, recovered, traced, and reported with proof that no one silently changed them?
```

## Invariant

```text
content id = hash of bytes
object state = append-only continuity
history = parent/child transform chain
report = references, not prose alone
```

## Atlas

```text
L8 compliance pack      NIS2 / DORA / audit export
L7 report              tibet-report
L6 trail               tibet-trail
L5 materials           SBOM / AI-SBOM
L4 snapshot            Wayback
L3 history             CBOM
L2 arrival             continuity envelope / continuityd
L1 sealed carrier      TBZ / .tza / tibet-zip
L0 content identity    content hash / canonical metadata
floor                  JIS + TIBET provenance
```

## What Belongs Here

- content-addressed object identity;
- sealed carrier accept/quarantine rules;
- continuity state transitions;
- object history chains;
- restore/snapshot checks;
- SBOM and AI-SBOM normalization;
- trail queries;
- report packs with required references.

## What Does Not Belong Here

- app UX;
- generic databases;
- model routing;
- policy decisions that belong to `tibet-security-conformance`.
