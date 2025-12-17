# Daily Routine Generator

A beautiful and intuitive desktop application built with PyQt6 that helps you organize and visualize your daily tasks and routines.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-6.0%2B-green)

## Features

✨ **Easy Task Entry**: Simple form to add tasks with time and duration  
📊 **Visual Table Display**: View all your tasks in a clean, organized table  
🎨 **Modern Dark Theme**: Beautiful dark color scheme with teal and cream accents  
💾 **Persistent Sessions**: Tasks remain available during your session  
🔄 **Real-time Updates**: Table updates automatically when you add new tasks  
🖱️ **Intuitive Interface**: User-friendly design with hover effects and clear navigation

### Main Window
The main input window where you enter your daily tasks:
- Task name (e.g., "Do Math Homework")
- Start time (e.g., "4 PM")
- Duration (e.g., "2 Hours")

### Results Window
A table view displaying all your tasks with columns for Task, Time, and Duration.

## Installation

### Prerequisites
- Python 3.8 or higher
- PyQt6

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/SamadhanAdhikari/Daily-Routine-Generator.git
cd daily-routine-generator
```

2. **Install dependencies**
```bash
pip install PyQt6
```

3. **Run the application**
```bash
python main.py
```

## Usage

### Adding Tasks

1. Launch the application
2. Enter your task details:
   - **Task**: What you need to do (e.g., "Study Python")
   - **Time**: When you'll start (e.g., "6 PM")
   - **Duration**: How long it will take (e.g., "2 Hours")
3. Click **"Submit Tasks"** to add the task to your routine
4. Repeat for all your daily tasks

### Viewing Your Routine

1. After adding all tasks, click **"Get Routine"**
2. A new window opens showing your tasks in a table format
3. The table displays all tasks with their times and durations
4. You can add more tasks and click "Get Routine" again to update the display

### Tips

- Fill out all three fields before submitting
- You can add as many tasks as you need
- The result window updates automatically when you add new tasks
- Clear task information is displayed in an easy-to-read table format

## Project Structure

```
daily-routine-generator/
│
├── main.py                 # Main application file
├── README.md              # Project documentation
```

## Code Overview

### Main Classes

**`MainWindow`**: The primary input window
- Handles task entry with three input fields
- Validates input before adding tasks
- Manages the connection to the results window

**`ResultWindow`**: The results display window
- Shows tasks in a formatted table
- Three columns: Task, Time, Duration
- Updates dynamically when new tasks are added

### Key Methods

- `get_tasks()`: Validates and stores task information
- `show_ResultWindow()`: Opens or updates the results window
- `populate_table()`: Fills the table with task data
- `update_tasks()`: Refreshes the table with new tasks

## Color Scheme

The app uses a modern dark theme:

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Gray | `#222831` |
| Headers | Medium Gray | `#393E46` |
| Accent/Highlights | Teal | `#00ADB5` |
| Text | Cream | `#EBD5AB` |
| Buttons | White Smoke | `whitesmoke` |

## Requirements

```
PyQt6>=6.0.0
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Ideas for Contributions

- Add ability to save routines to file
- Implement task editing functionality
- Add task deletion from the table
- Include time sorting/ordering
- Add task priority levels
- Export routine to PDF or Excel
- Add reminder/notification system
- Dark/Light theme toggle

## Known Issues

- Tasks are cleared when the application closes (no persistent storage yet)
- No edit functionality for submitted tasks
- No task deletion from the table view

## Future Enhancements

- [ ] Save routines to JSON/database
- [ ] Load previous routines
- [ ] Edit tasks after submission
- [ ] Delete individual tasks
- [ ] Sort tasks by time
- [ ] Add task categories/tags
- [ ] Export to PDF/Excel
- [ ] Add reminders/notifications
- [ ] Statistics and analytics
- [ ] Multi-day routine planning

## Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed: `python --version`
- Verify PyQt6 is installed: `pip show PyQt6`
- Reinstall PyQt6 if needed: `pip install --upgrade PyQt6`

### Window appears then disappears
- Check that `self.result_window` is initialized in `__init__`
- Ensure all parentheses are present in method calls

### Input fields not visible
- Check that QLineEdit has background-color set in stylesheet
- Verify color contrast between background and text

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Your Name**
- GitHub: [SamadhanAdhikari](https://github.com/SamadhanAdhikari)
- Email: adhikarisamadhan@gmail.com

## Acknowledgments

- Built with PyQt6
- Inspired by the need for simple daily routine management
- Color scheme inspired by modern dark themes

## Version History

### v1.0.0 (Current)
- Initial release
- Basic task entry functionality
- Table view display
- Modern dark theme UI

---

**Made with Python**

*Stay organized, stay productive!* 📅✨