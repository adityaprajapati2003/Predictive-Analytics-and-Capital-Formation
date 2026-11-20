from .embeddings import cosine
from .rules import passes


def rank(startup: dict, investors: list[dict], top_k: int = 10):
    """Compatibility ranking. The score is not a probability of investment."""
    scored = []
    for inv in investors:
        if not passes(startup, inv):
            continue
        sim = cosine(startup["embedding"], inv["embedding"]) if "embedding" in startup else 0.0
        scored.append({"investor_id": inv["id"], "compatibility": sim})
    return sorted(scored, key=lambda x: -x["compatibility"])[:top_k]
