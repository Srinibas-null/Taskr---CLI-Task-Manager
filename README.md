# Taskr - CLI Task Manager

#### Description 🖋:

Taskr is a command-line task manager built in Python. Instead of
opening an app or a browser, the user manages their to-do list
entirely from the terminal by typing simple commands. Tasks are
saved to a JSON file so they persist between sessions, closing
the terminal does not erase anything.

## Why I Built This ⚒️

I wanted to build something practical that I would actually use.
A task manager felt like the right choice because it covers the
core pillars of Python — functions, file I/O, error handling,
and working with data structures — without being a toy project.
The command-line interface also felt like a natural fit given
that CS50P is fundamentally about writing Python programs that
run in a terminal environment.

## How To Run 🏃‍♂️

Install dependencies first:
pip install -r requirements.txt

Then use the following commands:
python project.py add "Your task here"

python project.py list

python project.py complete <id>

python project.py delete <id>

python project.py q

## Project Files 📂

### project.py

This is the main file containing all the logic. It has a main()
function and four additional functions — add_task(), list_task(),
complete_task(), and delete_task().

The main() function reads sys.argv to detect what command the
user typed and routes to the correct function. If no command is
provided, or if a required argument is missing, the program exits
with a helpful error message.

add_task() takes a task name and a filepath as arguments. It
loads existing tasks from the JSON file, checks if the task
already exists to avoid duplicates, and appends the new task
with a default completed status of False. Tasks are stored with
their name in title case.

list_task() loads all tasks and displays them in a formatted
table using the rich library. Each task shows an ID, the task
name, and a status symbol — a checkmark for completed tasks and
a cross for pending ones. If no tasks exist yet, it prints a
friendly message instead of an empty table.

complete_task() accepts a task ID number rather than a task
name. This design choice made the user experience simpler —
typing an ID is faster and less error-prone than retyping an
exact task name. It converts the ID to a zero-based index,
validates it, checks if the task is already completed, and
marks it as done.

delete_task() follows the same ID-based approach as
complete_task(). It validates the ID, removes the task from
the list using pop(), and writes the updated list back to the
file.

### test_project.py

This file contains three pytest tests — one each for add_task(),
complete_task(), and delete_task(). Each test uses pytest's
built-in tmp_path fixture to create a temporary JSON file so
that tests never touch the real tasks.json file. This was an
important design decision — tests should be isolated and
repeatable without side effects.

### tasks.json

This file is created automatically the first time a task is
added. It stores all tasks as a JSON array of objects, each
with a task name and a completed boolean. Using JSON was a
deliberate choice over CSV because the data is structured —
each task has multiple fields — and Python's built-in json
module handles it cleanly without any extra dependencies.

### requirements.txt

Lists the only external dependency — rich. This library provides
the styled table output in list_task(). Everything else in the
project uses Python's standard library.

## Design Choices ⚙️

The biggest design decision was switching complete_task() and
delete_task() from name-based matching to ID-based matching.
The original approach required the user to type the exact task
name including correct capitalisation. This was frustrating in
practice. Switching to IDs made the interface feel much more
natural — you run list, see the IDs, then act on a number.

Another deliberate choice was adding filepath as a default
parameter to every function. This made the functions testable
without touching real data, while keeping normal usage identical
since the default value is always tasks.json.

Error handling was added at every file operation rather than
assuming the file exists. This means the program behaves
gracefully on first run, when the file is missing, or if the
file gets corrupted.

## Author ✍️
- Srinibas 
