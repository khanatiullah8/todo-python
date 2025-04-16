# Todo Application in Python

This project is a simple **Todo Application** built using core Python, utilizing file handling, custom modules, and custom packages.

## Features

- **Class Implementation**: Includes a `Todo` class with instance methods for:
  - Creating new todo items.
  - Reading all todo items.
  - Updating existing todo items.
  - Deleting specific todo items.
  - Generating unique IDs for each item.
  - Resetting the application.
- **Utility Functions**: Contains helper functions to validate operations like checking if a specific ID matches during update and delete operations.
- **Persistent Storage**:
  - Todo items are stored in a `todo_item.json` file.
  - The next unique ID is maintained in a `next_todo_id.txt` file, ensuring continuity when the program is closed and reopened.
- **Reset Functionality**:
  - The reset method clears all todo items in `todo_item.json` and resets the next unique ID to `1000` in `next_todo_id.txt`.

## Structure

- **Main File**: `todo_app.py` for executing operations.
- **Storage Files**:
  - `todo_item.json` for storing todo data.
  - `next_todo_id.txt` for maintaining the next unique ID.

## Requirements

- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **Virtual Environment**: It's recommended to use a virtual environment for isolating dependencies. Follow these steps:
  1. Create a virtual environment using `python -m venv env`.
  2. Activate the virtual environment:
     - For Windows: `env\Scripts\activate`
     - For macOS/Linux: `source env/bin/activate`.
- **Install Dependencies**: Install the necessary libraries using the following command:
  ```bash
  pip install -r requirements.txt

## How to Use

1. Clone the repository.
2. Run the `todo_app.py` file.
3. Follow the prompts to create, read, update, or delete todo items.

## Reset Functionality

Run the reset method to:
- Clear all todo items.
- Restart the ID sequence from `1000`.