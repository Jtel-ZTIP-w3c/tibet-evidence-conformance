# TIBET Evidence Conformance - SPEC

Deterministic sandbox vectors for storage/evidence interop.

## v1 - Content Identity

```text
content_id := "sha256:" + sha256(bytes)
match := computed content_id == expected content_id
```

## v2 - Sealed Object Carrier

```text
accept := carrier_kind == "tza.sealed.v1"
          AND sha256(payload) == content_hash
          AND recipient == expected_recipient
```

Hash mismatch or wrong recipient quarantines.

## v3 - Continuity Envelope

Allowed transition:

```text
created -> arrived -> verified -> accepted
created -> arrived -> quarantined
```

Skipping `arrived` is invalid. `quarantined` is terminal.

## v4 - CBOM Chain

Each child object must name its parent and its transform.

```text
valid := child.parent_id == parent.object_id
         AND child.input_hash == parent.content_hash
```

## v5 - Wayback Snapshot

Restored state must match expected files and hashes.

## v6 - SBOM Ingest

Dependency evidence normalizes to `name`, `version`, `purl`, `source`.

## v7 - AI-SBOM Usage Event

Usage evidence must include actor, provider, model, purpose, and timestamp.

## v8 - Trail Query

Trace by `object_id`, `actor_id`, or `cascade_id` must return expected event ids.

## v9 - Report Pack

A report is valid only if required evidence references are present.
