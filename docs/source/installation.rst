Follow the steps below to install and run the Task List App on your system.

Prerequisites
-------------

Before starting, make sure you have the following installed:

- Python 3.6 or higher
- MySQL server
- pip (Python package manager)

Step-by-Step Setup
------------------

1. **Clone the repository or download the code.**
   
   You can clone the repository using Git:
   
   .. code-block:: bash
      git clone https://github.com/Alexis-dev410/DBA-Assignment-4

2. **Navigate to the project directory.**

   After cloning, navigate to the project directory:
   
   .. code-block:: bash
      cd task-list-app

3. **Install the required Python dependencies.**

   Install Kivy, MySQL connector, and Python-dotenv by running:
   
   .. code-block:: bash
      pip install kivy mysql-connector python-dotenv

4. **Set up your MySQL database.**

   Create a MySQL database and configure the connection. You'll need to create a `.env` file in the root of the project directory with the following contents:
   
   .. code-block:: bash
      DB_HOST=your_host
      DB_USER=your_user
      DB_PASSWORD=your_password
      DB_NAME=your_database_name

5. **Run the app.**

   Once everything is set up, run the following command to start the application:
   
   .. code-block:: bash
      python main.py
