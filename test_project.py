import pytest
import json
from project import add_task, complete_task, delete_task


def test_add_task(tmp_path):
    filepath = tmp_path / "test_tasks.json"
    add_task("Study FastAPI", filepath)
    with open(filepath, 'r') as file:
        tasks = json.load(file)
    assert len(tasks) == 1
    assert tasks[0]['task'] == "Study FastAPI"
    assert tasks[0]['completed'] == False


def test_complete_task(tmp_path):
    filepath = tmp_path / "test_tasks.json"
    add_task("Study FastAPI", filepath)
    complete_task('1', filepath)
    with open(filepath, 'r') as file:
        tasks = json.load(file)
    assert tasks[0]['completed'] == True


def test_delete_task(tmp_path):
    filepath = tmp_path / "test_tasks.json"
    add_task("Study FastAPI", filepath)
    delete_task("1", filepath)
    with open(filepath, 'r') as file:
        tasks = json.load(file)
        assert len(tasks) == 0
