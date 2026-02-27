# Daily Routine Generator

A PyQt6-based desktop application for creating and managing your daily routine with a modern, visually appealing interface.

## Features

- **Task Management**: Add tasks with specific start and end times
- **Time Validation**: Prevents overlapping tasks and validates time inputs
- **Visual Table Display**: View your daily routine in a sortable, editable table
- **12-Hour Format**: Easy-to-use AM/PM time selection
- **Modern UI**: Dark-themed interface with custom styling
- **Duplicate Detection**: Prevents adding the same task multiple times
- **Confirmation Dialogs**: Confirms task submission before adding

## Screenshots

The application features two main windows:
1. **Main Window**: Input interface for adding tasks
2. **Routine Window**: Table view displaying your organized daily routine

## Requirements

- Python 3.x
- PyQt6

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install PyQt6
```

## Usage

1. Run the application:

```bash
python daily_routine_generator.py
```

2. **Adding Tasks**:
   - Enter a task name in the "Enter Task" field
   - Set the start time (hour, minutes, AM/PM)
   - Set the end time (hour, minutes, AM/PM)
   - Click "Submit Tasks" to add the task
   - Confirm your submission in the dialog box

3. **Viewing Your Routine**:
   - Click "Get Routine" to open the routine table window
   - Tasks are automatically sorted by start time
   - Double-click any cell to edit (changes are temporary)

## Color Scheme

The application uses a modern dark theme:
- Background: `#222831`
- Accent: `#00ADB5` (Teal)
- Secondary: `#393E46` (Dark Gray)
- Highlight: `#EBD5AB` (Beige)

## Code Structure

```
daily_routine_generator.py
--------- MainWindow (QWidget)
   |--------- Input fields for task and time
   |--------- Validation methods
   |--------- Task submission logic
--------- ResultWindow (QWidget)
   |--------- Table display
   |--------- Sorting functionality
   |--------- Editable cells
```

## Key Methods

### MainWindow
- `get_tasks()`: Handles task submission
- `Input_Validation()`: Validates all user inputs
- `Confirmation()`: Shows confirmation dialog
- `show_ResultWindow()`: Opens the routine table

### ResultWindow
- `make_table()`: Populates the table with tasks
- `sort_by_time()`: Sorts tasks chronologically

## Notes

- Changes made in the routine table are **temporary** and will reset when the window is closed
- The application uses 12-hour time format with AM/PM selection
- Tasks are automatically sorted by start time in the routine view

## Future Enhancements

Potential improvements for future versions:
- Save/load routines to/from files
- Export routine as PDF or image
- Set reminders/notifications
- Recurring tasks support
- Dark/light theme toggle
- Task categories and color coding

## License

This project is open source and available for personal and educational use.