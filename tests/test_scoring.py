from eval_gym.scenario import Scenario
from eval_gym.scoring import score_trajectory


def test_score_trajectory_partial_success() -> None:
    s = Scenario("checkout", ["open", "add", "pay"])
    assert score_trajectory(s, ["open", "pay"]) == 2 / 3
