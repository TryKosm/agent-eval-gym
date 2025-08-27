from .scenario import Scenario


def score_trajectory(scenario: Scenario, trajectory: list[str]) -> float:
    if not scenario.required_steps:
        return 1.0
    hits = sum(1 for step in scenario.required_steps if step in trajectory)
    return hits / len(scenario.required_steps)
