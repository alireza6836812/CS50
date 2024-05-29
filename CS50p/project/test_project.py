from datetime import date
from project import dooz

def test_get_minutes():
    assert just_to_do_task(1) == 1
    assert just_to_do_task(2) == 4
    assert just_to_do_task(3) == 9
