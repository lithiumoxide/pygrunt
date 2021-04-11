# Sample Test passing with nose and pytest

from pygrunt import pygrunt as pg

def test_action_exit_code():
    assert type(pg.action('/path/')[1]) == int

def test_action_exit_message():
    assert type(pg.action('/path/')[0]) == str