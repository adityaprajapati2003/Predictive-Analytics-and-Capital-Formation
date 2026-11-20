"""Investor compatibility ranking (a ranking score, NOT a probability of investment)."""


def hard_filter(startup: dict, investors: list[dict]) -> list[dict]:
    out = []
    for inv in investors:
        if inv.get("stages") and startup["stage"] not in inv["stages"]:
            continue
        if inv.get("subsectors") and startup["subsector"] not in inv["subsectors"]:
            continue
        ask = startup.get("ask")
        if ask and inv.get("check_max") and ask > inv["check_max"] * 5:
            continue
        out.append(inv)
    return out


def rank(startup: dict, investors: list[dict], top_k: int = 10) -> list[dict]:
    candidates = hard_filter(startup, investors)
    # TODO: add embedding similarity (pgvector) and geography/thesis features.
    scored = [{**inv, "compatibility": 1.0} for inv in candidates]
    return sorted(scored, key=lambda x: x["compatibility"], reverse=True)[:top_k]
