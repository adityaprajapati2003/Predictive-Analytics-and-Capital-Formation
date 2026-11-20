from src.evaluation.ranking_metrics import ndcg_at_k, precision_at_k


def test_precision_at_k():
    assert precision_at_k({1, 2}, [1, 3, 2], 2) == 0.5


def test_ndcg_perfect():
    assert ndcg_at_k({1, 2}, [1, 2, 3], 2) == 1.0
