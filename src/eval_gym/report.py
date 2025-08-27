def summarize(scores: list[float]) -> dict[str, float]:
    if not scores:
        return {"avg_score": 0.0}
    return {"avg_score": sum(scores) / len(scores)}
