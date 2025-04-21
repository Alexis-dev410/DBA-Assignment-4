This section provides a detailed overview of the app's architecture, API references, and guidelines for future enhancements.

API Reference
-------------

### `Database` Class (db_layer.py)

The `Database` class handles MySQL database operations for the app. It includes methods for CRUD operations on tasks.

Methods:
--------

- **`create_table()`**: Creates the tasks table in the database if it doesn't already exist.
- **`fetch_all_tasks()`**: Fetches all tasks from the database.
- **`add_task(task_text)`**: Adds a new task to the database.
- **`update_task(task_text, task_id)`**: Updates the task text for a given task ID.
- **`delete_task(task_id)`**: Deletes a task from the database.
- **`close()`**: Closes the database connection.

`TaskManager` Class (logic_layer.py)

The `TaskManager` class acts as the bridge between the app's logic layer and the database. It calls methods from the `Database` class to perform operations on tasks.

Methods:
--------

- **`load_tasks()`**: Loads all tasks from the database.
- **`add_task(task_text)`**: Adds a new task by calling the `add_task` method in the `Database` class.
- **`update_task(task_text, task_id)`**: Updates a task in the database.
- **`delete_task(task_id)`**: Deletes a task from the database.
- **`close()`**: Closes the database connection.

`ToDoScreen` Class (main.py)

The `ToDoScreen` class is the main screen of the Kivy app. It contains UI elements for displaying tasks, adding new tasks, and interacting with existing ones.

Key Methods:
------------

- **`load_tasks()`**: Loads tasks from the database and populates the task list in the UI.
- **`add_task()`**: Adds a new task to the task list and the database.
- **`update_task()`**: Updates a task in both the UI and the database.
- **`delete_task()`**: Deletes a task from the UI and the database.
- **`open_popup()`**: Opens the task update popup.

Design Decisions
----------------

- **Kivy for UI**: Kivy is used for its flexibility and cross-platform capabilities. The app works on both Windows and Linux.
- **MySQL for Persistence**: MySQL is chosen as the database for its scalability and widespread use in production systems.
- **Layered Architecture**: The app follows a clean, maintainable layered architecture, separating the UI, logic, and database layers.

Future Enhancements
-------------------

- **Search Functionality**: Allow users to search tasks by description.
- **Task Prioritization**: Add functionality to prioritize tasks and sort them accordingly.
- **User Authentication**: Implement user authentication to allow different users to manage their own tasks.

Contributing
------------

If you'd like to contribute to the development of this app, feel free to fork the repository, make changes, and create a pull request. Ensure that your code follows the PEP-8 guidelines.
