import pytest
from unittest.mock import MagicMock
from logic_layer import ToDoScreen, TaskItem


@pytest.fixture
def mock_task_manager():
    """Fixture to mock the TaskManager dependency."""
    task_manager = MagicMock()
    task_manager.load_tasks.return_value = [
        {"id": 1, "task_text": "Test Task 1"},
        {"id": 2, "task_text": "Test Task 2"},
    ]
    task_manager.add_task.return_value = 3  # Mocking the ID of the new task
    task_manager.update_task.return_value = None
    task_manager.delete_task.return_value = None
    return task_manager


@pytest.fixture
def todo_screen(mock_task_manager):
    """Fixture to create a ToDoScreen instance with a mocked task manager."""
    screen = ToDoScreen()
    screen.task_manager = mock_task_manager  # Inject the mock TaskManager
    return screen


def test_load_tasks(todo_screen):
    """Test loading tasks and displaying them in the UI."""
    tasks = todo_screen.task_manager.load_tasks()
    assert len(tasks) == 2
    assert tasks[0]["task_text"] == "Test Task 1"
    assert tasks[1]["task_text"] == "Test Task 2"


def test_add_task(todo_screen, mock_task_manager):
    """Test adding a task to the task manager and the UI."""
    todo_screen.ids.task_input.text = "New Task"
    todo_screen.add_task()
    mock_task_manager.add_task.assert_called_once_with("New Task")
    assert todo_screen.ids.task_input.text == ""  # Input should be cleared after adding


def test_update_task(todo_screen, mock_task_manager):
    """Test updating a task."""
    task_item = TaskItem(task_id=1, text="Test Task 1")
    todo_screen.update_task(task_item, "Updated Task")
    mock_task_manager.update_task.assert_called_once_with("Updated Task", 1)
    assert task_item.ids.task_label.text == "Updated Task"


def test_delete_task(todo_screen, mock_task_manager):
    """Test deleting a task."""
    task_item = TaskItem(task_id=1, text="Test Task 1")
    todo_screen.delete_task(task_item)
    mock_task_manager.delete_task.assert_called_once_with(1)
