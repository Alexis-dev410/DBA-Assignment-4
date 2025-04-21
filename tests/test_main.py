import pytest
from kivy.tests.common import GraphicUnitTest
from unittest.mock import MagicMock
from main import ToDoScreen


@pytest.fixture
def mock_task_manager():
    """Fixture to mock the TaskManager for UI tests."""
    mock_task_manager = MagicMock()
    mock_task_manager.load_tasks.return_value = [{"id": 1, "task_text": "Mock Task"}]
    mock_task_manager.add_task.return_value = 1
    return mock_task_manager


class TestToDoScreen(GraphicUnitTest):
    def test_load_tasks(self, mock_task_manager):
        """Test the task loading functionality in the UI."""
        screen = ToDoScreen()
        screen.task_manager = mock_task_manager
        screen.load_tasks()
        assert len(screen.ids.task_list.children) > 0  # Check if task items are added to the UI


    def test_add_task(self, mock_task_manager):
        """Test the add task functionality in the UI."""
        screen = ToDoScreen()
        screen.task_manager = mock_task_manager
        screen.ids.task_input.text = "New Task"
        screen.add_task()
        mock_task_manager.add_task.assert_called_once_with("New Task")
        assert screen.ids.task_input.text == ""  # Check if input field is cleared after adding
