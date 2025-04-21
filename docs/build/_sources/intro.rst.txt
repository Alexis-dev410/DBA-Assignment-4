The Task List App is a simple yet effective application for managing tasks. It allows users to add, update, delete, and view tasks stored in a MySQL database.

High-Level Design
-----------------

The application follows a layered architecture:

- **UI Layer**: Built using Kivy, a Python framework for creating cross-platform user interfaces.
- **Logic Layer**: Responsible for handling the application's business logic. It interacts with the database and provides CRUD functionality for tasks.
- **Database Layer**: Uses MySQL to persist tasks. This layer includes operations to create, read, update, and delete tasks from the database.

The app aims to provide a clean, intuitive interface while allowing for persistence through the MySQL database.

Features:
---------

- Add new tasks to the task list.
- Update and delete existing tasks.
- View all tasks in a user-friendly interface.
- Persist tasks in a MySQL database for future use.