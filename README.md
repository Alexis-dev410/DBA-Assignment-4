# 📝 Assignment 4 – Task List App

This project is a simple Task List App built with **Kivy** for the user interface and **MySQL** for persistent storage. It also includes **unit tests** for the database layer and **documentation** generated using **Sphinx**.

---

## ⚙️ Setup Instructions

### 🔧 Install Dependencies

Before running the application or tests, make sure the following are installed:

- Python 3.x
- Required Python packages:

pip install -r requirements.txt

run the tests using **pytest** while in the tests folder
Ex: pytest tests/test_main.py

📚 Building and Viewing Sphinx Documentation
📦 Prerequisite: Sphinx installed (pip install sphinx)

1. Navigate to the docs/ directory:
    cd docs

2. build the HTML documentation
    sphinx-build -b html source build

3. open the documentation on your browser
    open build/index.html  # On macOS
# OR
xdg-open build/index.html  # On Linux
# OR manually open the file on Windows