import pytest
import old_task

def test_task_1():
    ref = [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    res = old_task.task_1()
    assert res == ref

def test_task_2():
    ref = [98, 35, 15, 213, 54, 119]
    res = old_task.task_2()
    assert res == ref

def test_task_3():
    ref = {3: 57.14, 2: 42.86}
    res = old_task.task_3()
    assert res == ref
