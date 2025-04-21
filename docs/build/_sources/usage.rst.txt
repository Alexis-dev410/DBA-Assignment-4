The Task List App provides a simple user interface to manage tasks stored in a MySQL database.

Main Features
-------------
- Add a new task.
- Update an existing task.
- Delete a task.
- View all tasks.

Step-by-Step Guide
------------------

1. **Adding a New Task:**

   To add a new task, simply type the task description into the input field and press the "Add Task" button. The task will be added to the list and stored in the database.

2. **Updating a Task:**

   To update a task, click the "Edit" button next to the task. A popup will appear allowing you to edit the task description. After editing, press the "Update" button to save the changes.

3. **Deleting a Task:**

   To delete a task, click the "Delete" button next to the task. This will remove the task both from the UI and the database.

4. **Viewing Tasks:**

   All tasks will be displayed in a list on the main screen. You can scroll through the list to view tasks.

Example UI Interactions:
-------------------------

**Adding a task:**
task_manager.add_task("Buy groceries")
task_manager.update_task("Buy groceries and cook dinner", task_id)
task_manager.delete_task(task_id)

