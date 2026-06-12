# TIBET Evidence Conformance Kit

**Prove that evidence objects can be stored, sealed, traced, restored, and reported without trusting the vendor.**

This is a sandbox prototype for the storage/evidence branch of TIBET conformance. It mirrors
the zero-trust style of `ztip-conformance` and `tibet-comms-conformance`: vectors are the
contract; reference code is only one implementation.

## What this repo is

This is an **evidence interoperability kit, not a storage SDK**.

The contract is the JSON vector set in [`vectors/`](vectors/). A real conformance claim
requires an independent implementation that consumes those vectors and returns the same
results without importing [`ref/`](ref/).

## Quickstart

No third-party dependencies.

```sh
./run.sh
```

Expected ending:

```text
YES IT PLAYS — evidence vectors are internally consistent. That is not interop.
Interop challenge: implement your own verifier against vectors/*.json.
```

## Levels

| Level | Primitive | Vector |
|---:|---|---|
| v1 | content identity | `vectors/content_hash_v1.json` |
| v2 | sealed object carrier | `vectors/sealed_object_v2.json` |
| v3 | continuity envelope | `vectors/continuity_v3.json` |
| v4 | CBOM chain | `vectors/cbom_chain_v4.json` |
| v5 | Wayback snapshot | `vectors/wayback_snapshot_v5.json` |
| v6 | SBOM ingest | `vectors/sbom_ingest_v6.json` |
| v7 | AI-SBOM usage event | `vectors/ai_sbom_usage_v7.json` |
| v8 | trail query | `vectors/trail_query_v8.json` |
| v9 | report pack | `vectors/report_pack_v9.json` |

## Package Branch

This maps the branch carried by:

```text
tibet-zip / TBZ · tibet-continuityd · tibet-cbom · tibet-sbom · tibet-ai-sbom
tibet-wayback · tibet-trail · tibet-report · tibet-audit · tibet-nis2
```

Products and UI layers are out of scope.

---

## Part of the conformance family

Four runnable kits, one per branch of the stack. Run any, implement your own verifier against its
vectors, interoperate with no vendor in the loop. Together they let a second implementation
reconstruct the whole spine from the vectors alone.

- [ztip-conformance](https://github.com/Jtel-ZTIP-w3c/ztip-conformance) — identity / attestation / ceremony
- [tibet-comms-conformance](https://github.com/Jtel-ZTIP-w3c/tibet-comms-conformance) — communication / routing
- [tibet-evidence-conformance](https://github.com/Jtel-ZTIP-w3c/tibet-evidence-conformance) — storage / evidence
- [tibet-security-conformance](https://github.com/Jtel-ZTIP-w3c/tibet-security-conformance) — policy / enforcement

Primitive atlas: https://github.com/Jtel-ZTIP-w3c/Jtel-ZTIP-w3c.github.io (INTEROP.md).
