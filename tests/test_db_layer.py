import pytest
from db_layer import Database


@pytest.fixture
def db():
    db = Database(host="localhost", user="test_user", password="test_password", database="test_db")
    db.create_table()
    db.cursor.execute("DELETE FROM tasks")
    db.conn.commit()
    yield db
    db.close()



def test_add_task(db):
    """Test adding a task."""
    task_text = "Test Task"
    task_id = db.add_task(task_text)
    assert task_id is not None
    tasks = db.fetch_all_tasks()
    assert any(task["task_text"] == task_text for task in tasks)


def test_update_task(db):
    """Test updating a task."""
    task_text = "Test Task"
    task_id = db.add_task(task_text)
    new_text = "Updated Task"
    db.update_task(new_text, task_id)
    tasks = db.fetch_all_tasks()
    assert any(task["task_text"] == new_text for task in tasks)


def test_delete_task(db):
    """Test deleting a task."""
    task_text = "Test Task"
    task_id = db.add_task(task_text)
    db.delete_task(task_id)
    tasks = db.fetch_all_tasks()
    assert not any(task["task_text"] == task_text for task in tasks)


def test_fetch_all_tasks(db):
    """Test fetching all tasks."""
    task_text1 = "Task 1"
    task_text2 = "Task 2"
    db.add_task(task_text1)
    db.add_task(task_text2)
    tasks = db.fetch_all_tasks()
    assert len(tasks) >= 2
    assert any(task["task_text"] == task_text1 for task in tasks)
    assert any(task["task_text"] == task_text2 for task in tasks)