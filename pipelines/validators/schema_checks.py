"""Provenance validation: every feature must carry unit, period, source, collected_on, verified."""
REQUIRED_PROVENANCE = {"unit", "period", "source", "collected_on", "verified"}


def validate(record: dict) -> list[str]:
    problems = []
    for name, meta in record.items():
        if not isinstance(meta, dict):
            problems.append(f"{name}: not a provenance dict")
            continue
        missing = REQUIRED_PROVENANCE - meta.keys()
        if missing:
            problems.append(f"{name}: missing {sorted(missing)}")
    return problems
