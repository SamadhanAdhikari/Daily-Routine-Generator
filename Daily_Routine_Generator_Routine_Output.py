from PyQt6.QtWidgets import QWidget, QTableWidget, QLabel, QVBoxLayout, QTableWidgetItem, QFileDialog, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from dotenv import load_dotenv
import os
import json

class Daily_Routine_Timetable_Output(QWidget):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks
        self.HEADER = QLabel("DAILY ROUTINE", self)
        self.table = QTableWidget()
        self.instruction = QLabel("Double click on boxes to edit routine.", self)
        self.instruction2 = QLabel("(The changes made are not permanent and will be reverted after the window is closed.)", self)
        self.save_button = QPushButton("Save Routine", self)
        self.load_button = QPushButton("Load Routine", self)
        
        load_dotenv()
        self.save_directory = os.path.join("MyRoutines")
        
        if not self.save_directory:
            self.save_directory = os.path.join(os.path.expanduser("~"), "Documents", "MyRoutines")
        
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Routine")
        self.setGeometry(300, 30, 800, 600)

        self.HEADER.setObjectName("HEADER")
        self.table.setObjectName("routine_table")
        self.instruction.setObjectName("instruction")
        self.instruction2.setObjectName("instruction2")
        self.save_button.setObjectName("save_button")
        self.load_button.setObjectName("load_button")

        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction2, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.table)
        vbox.addWidget(self.save_button)
        vbox.addWidget(self.load_button)
        self.setLayout(vbox)
        
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(["Task", "Time", "Deadline"])

        self.table.setColumnWidth(0, 260)
        self.table.setColumnWidth(1, 260)
        self.table.setColumnWidth(2, 260)

        self.make_table()

        self.save_button.clicked.connect(self.save_routine)
        self.load_button.clicked.connect(self.load_routine)

        self.Apply_CSS()

    def Apply_CSS(self):
        try:
            with open("style.css", "r", encoding="utf-8") as file:
                css_content = file.read()
                self.setStyleSheet(css_content)
        except FileNotFoundError:
            QMessageBox.warning(self, "⚠ Style file not found", "using defaults")
        except Exception as error:
            QMessageBox.warning(self, "✗ Error loading stylesheet", error)

    def sort_by_time(self):
        def time_conversion(task):
            hours = int(task['time'])
            minutes = int(task['minutes'])
            ap = task['AP']

            if ap == 'PM' and hours != 12:
                hours += 12
            elif ap == 'AM' and hours == 12:
                hours = 0
            return hours * 60 + minutes

        self.tasks.sort(key = time_conversion)

    def make_table(self):
        self.sort_by_time()

        self.table.setRowCount(len(self.tasks))
        
        for index, task in enumerate(self.tasks):
            self.table.setItem(index, 0, QTableWidgetItem(task["task"]))
            self.table.setItem(index, 1, QTableWidgetItem(f"{task['time']} : {task['minutes']} {task['AP']}"))
            self.table.setItem(index, 2, QTableWidgetItem(f"{task['end_time']} : {task['end_minutes']} {task['end_AP']}"))

            self.table.setRowHeight(index, 50)

    def save_routine(self):
        if not self.tasks:
            QMessageBox.warning(self, "No Tasks", "No tasks to save!")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Save Routine", 
            self.save_directory,
            "JSON Files (*.json);;All Files (*)"
        )

        if filename:
            try:
                with open(filename, 'w') as f:
                    json.dump(self.tasks, f, indent=4)
                QMessageBox.information(self, "Success", "Routine saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{str(e)}")

    def load_routine(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, 
            "Load Routine", 
            self.save_directory,
            "JSON Files (*.json);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    self.tasks = json.load(f)
                self.make_table()
                QMessageBox.information(self, "Success", f"Loaded {len(self.tasks)} tasks!")
            except FileNotFoundError:
                QMessageBox.critical(self, "Error", "File not found!")
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Error", "Invalid JSON file!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file:\n{str(e)}")