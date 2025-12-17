import sys
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton, QTableWidgetItem
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.daily_tasks = []
        self.result_window = None
        self.read_task = QLineEdit(self)
        self.read_time = QLineEdit(self)
        self.read_duration = QLineEdit(self)
        self.HEADER = QLabel("DAILY ROUTINE GENERATOR", self)
        self.submit_button = QPushButton("Submit Tasks", self)
        self.instruction = QLabel("Enter Your routine", self)
        self.routine_button = QPushButton("Get Routine", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Routine Generator")
        self.move(300, 30)
        self.read_task.setPlaceholderText("Enter Task (eg. Do Math Homework)")
        self.read_time.setPlaceholderText("Enter Time of the day to start the Task (eg. 4 PM)")
        self.read_duration.setPlaceholderText("Enter Duration of Task (eg. 2 Hours)")

        self.HEADER.setObjectName("HEADER")
        self.read_task.setObjectName("read_task")
        self.read_time.setObjectName("read_time")
        self.read_duration.setObjectName("read_duration")
        self.instruction.setObjectName("instruction")
        self.submit_button.setObjectName("submit_button")
        self.routine_button.setObjectName("routine_button")

        self.setStyleSheet("""
            QWidget {
                background-color: #222831;
            }

            QLabel#HEADER {
                font-size: 50px;
                font-family: Bold Font;
                font-weight: Bold;
                background-color: #393E46;
                padding: 20px;
                border-radius: 20px;
                margin-bottom: 10px;
                color: #EBD5AB;
            }

            QLineEdit#read_task {
                padding: 15px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 15px;
                background-color: #00ADB5;
                color: #222831;
            }

            QLineEdit#read_time {
                padding: 15px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 15px;
                background-color: #00ADB5;
                color: #222831;
            }

            QLineEdit#read_duration {
                padding: 15px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                background-color: #00ADB5;
                color: #222831;
            }

            QPushButton#submit_button {
                padding: 15px;
                background-color: whitesmoke;
                border-radius: 25px;
                font-size: 40px;
                font-family: Times New Roman;
            }

            QPushButton#submit_button:hover {
                background-color: #d3d3d3;
            }

            QLabel#instruction {
                margin-bottom: 10px;
                color: #EBD5AB;
                font-family: Calibri;
                font-size: 30px;
            }

            QPushButton#routine_button {
                padding: 20px;
                margin-top: 10px;
                background-color: #393E46;
                color: #EBD5AB;
                font-family: Calibri;
                font-size: 30px;
                border-radius: 15px;
                font-weight: Bold;
            }

            QPushButton#routine_button:hover {
                background-color: #00ADB5;
            }
        """)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction, alignment= Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.read_task)
        vbox.addWidget(self.read_time)
        vbox.addWidget(self.read_duration)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.routine_button)
        self.setLayout(vbox)

        self.submit_button.clicked.connect(self.get_tasks)
        self.routine_button.clicked.connect(self.show_ResultWindow)

    def get_tasks(self):
        task = self.read_task.text()
        time = self.read_time.text()
        duration = self.read_duration.text()

        if task != "" and time != "" and duration != "":
            self.daily_tasks.append({"task": task, "time": time, "duration": duration})
            self.read_task.clear()
            self.read_time.clear()
            self.read_duration.clear()
        else:
            self.instruction.setText("Error : Enter all the fields before submitting")
        print(self.daily_tasks)

    def show_ResultWindow(self):
        if self.result_window is None:
            self.result_window = ResultWindow(self.daily_tasks)
        else:
            self.result_window.update_tasks(self.daily_tasks)
        self.result_window.show()

class ResultWindow(QWidget):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks
        self.HEADER = QLabel("DAILY ROUTINE", self)
        self.table = QTableWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Routine")
        self.setGeometry(300, 30, 800, 600)

        self.HEADER.setObjectName("HEADER")
        self.table.setObjectName("routine_table")

        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.table)
        self.setLayout(vbox)
        
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(["Task", "Time", "Duration"])

        self.table.setColumnWidth(0, 260)
        self.table.setColumnWidth(1, 260)
        self.table.setColumnWidth(2, 260)

        self.populate_table()
        
        self.setStyleSheet("""
            QWidget {
                background-color: #222831;
            }

            QLabel#HEADER {
                font-size: 50px;
                font-family: Bold Font;
                font-weight: Bold;
                background-color: #393E46;
                padding: 20px;
                border-radius: 20px;
                margin-bottom: 20px;
                color: #EBD5AB;
            }

            QTableWidget#routine_table {
                background-color: #393E46;
                gridline-color: #00ADB5;
                font-size: 18px;
                border-radius: 10px;
            }

            QTableWidget#routine_table::item {
                padding: 10px;
                color: #EBD5AB;
            }

            QTableWidget#routine_table::item:selected {
                background-color: #00ADB5;
                color: #222831;
            }

            QHeaderView::section {
                background-color: #00ADB5;
                color: #222831;
                padding: 10px;
                font-weight: bold;
                font-size: 20px;
                border: none;
            }
        """)

    def populate_table(self):
        self.table.setRowCount(len(self.tasks))
        
        for index, task in enumerate(self.tasks):
            self.table.setItem(index, 0, QTableWidgetItem(task["task"]))
            self.table.setItem(index, 1, QTableWidgetItem(task["time"]))
            self.table.setItem(index, 2, QTableWidgetItem(task["duration"]))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()