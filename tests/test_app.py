from app import rps


def test_rps_function_runs():
    game = rps("Tester")
    assert callable(game)
