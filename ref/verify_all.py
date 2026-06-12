#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "vectors"


def load(name: str) -> dict:
    with (V / name).open(encoding="utf-8") as f:
        return json.load(f)


def h(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode()).hexdigest()


def show(ok: bool, name: str, got, expect) -> int:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:24s} got={got!r} expect={expect!r}")
    return int(ok)


def content_hash():
    d = load("content_hash_v1.json")
    print("### v1 - content identity")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        got = h(c["bytes"]) == c["expected_hash"]
        passed += show(got == c["expect_match"], c["name"], got, c["expect_match"])
    return passed, total


def sealed_object():
    d = load("sealed_object_v2.json")
    print("### v2 - sealed object")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        x = c["carrier"]
        got = "accept" if x["carrier_kind"] == "tza.sealed.v1" and h(x["payload"]) == x["content_hash"] and x["recipient"] == d["expected_recipient"] else "quarantine"
        passed += show(got == c["expect_decision"], c["name"], got, c["expect_decision"])
    return passed, total


def continuity():
    d = load("continuity_v3.json")
    allowed = {("created", "arrived"), ("arrived", "verified"), ("verified", "accepted"), ("arrived", "quarantined")}
    print("### v3 - continuity envelope")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        states = c["states"]
        got = states[0] == "created" and all((a, b) in allowed for a, b in zip(states, states[1:]))
        passed += show(got == c["expect_valid"], c["name"], got, c["expect_valid"])
    return passed, total


def cbom():
    d = load("cbom_chain_v4.json")
    print("### v4 - CBOM chain")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        p, child = c["parent"], c["child"]
        got = child["parent_id"] == p["object_id"] and child["input_hash"] == p["content_hash"]
        passed += show(got == c["expect_valid"], c["name"], got, c["expect_valid"])
    return passed, total


def wayback():
    d = load("wayback_snapshot_v5.json")
    print("### v5 - Wayback snapshot")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        got = c["restored"] == d["expected"]
        passed += show(got == c["expect_match"], c["name"], got, c["expect_match"])
    return passed, total


def sbom():
    d = load("sbom_ingest_v6.json")
    print("### v6 - SBOM ingest")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        dep = c["dependency"]
        got = all(dep.get(k) for k in ("name", "version", "purl", "source"))
        passed += show(got == c["expect_valid"], c["name"], got, c["expect_valid"])
    return passed, total


def ai_sbom():
    d = load("ai_sbom_usage_v7.json")
    print("### v7 - AI-SBOM usage")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        e = c["event"]
        got = all(e.get(k) for k in d["required"]) and str(e.get("actor_id", "")).startswith("jis:")
        passed += show(got == c["expect_valid"], c["name"], got, c["expect_valid"])
    return passed, total


def trail():
    d = load("trail_query_v8.json")
    print("### v8 - trail query")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        q = c["query"]
        key, value = next(iter(q.items()))
        got = [e["event_id"] for e in d["events"] if e.get(key) == value]
        passed += show(got == c["expect_event_ids"], c["name"], got, c["expect_event_ids"])
    return passed, total


def report():
    d = load("report_pack_v9.json")
    print("### v9 - report pack")
    total = passed = 0
    for c in d["cases"]:
        total += 1
        refs = c["refs"]
        got = all(refs.get(k) for k in d["required_refs"])
        passed += show(got == c["expect_valid"], c["name"], got, c["expect_valid"])
    return passed, total


def main() -> int:
    suites = [content_hash, sealed_object, continuity, cbom, wayback, sbom, ai_sbom, trail, report]
    passed = total = 0
    for s in suites:
        p, t = s()
        passed += p
        total += t
        print()
    if passed == total:
        print("YES IT PLAYS — evidence vectors are internally consistent. That is not interop.")
        print("Interop challenge: implement your own verifier against vectors/*.json.")
        return 0
    print(f"FAIL — {passed}/{total} cases passed")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
