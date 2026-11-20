import numpy as np


def precision_at_k(relevant: set, ranked: list, k: int) -> float:
    return len([x for x in ranked[:k] if x in relevant]) / k


def recall_at_k(relevant: set, ranked: list, k: int) -> float:
    return len([x for x in ranked[:k] if x in relevant]) / max(len(relevant), 1)


def ndcg_at_k(relevant: set, ranked: list, k: int) -> float:
    dcg = sum(1 / np.log2(i + 2) for i, x in enumerate(ranked[:k]) if x in relevant)
    ideal = sum(1 / np.log2(i + 2) for i in range(min(len(relevant), k)))
    return dcg / ideal if ideal else 0.0
