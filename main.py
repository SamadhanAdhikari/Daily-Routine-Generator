import sys
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem, QComboBox
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.daily_tasks = []
        self.result_window = None
        self.read_task = QLineEdit(self)
        self.read_time = QLineEdit(self)
        self.read_minutes = QLineEdit(self)
        self.read_duration = QLineEdit(self)
        self.HEADER = QLabel("DAILY ROUTINE GENERATOR", self)
        self.submit_button = QPushButton("Submit Tasks:", self)
        self.instruction = QLabel("Enter Your routine: Please Enter Chronologically", self)
        self.routine_button = QPushButton("Get Routine", self)
        self.AP_selection = QComboBox()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Routine Generator")
        self.move(300, 30)
        self.read_task.setPlaceholderText("Enter Task (eg. Do Math Homework)")
        self.read_time.setPlaceholderText("Enter Time (eg. 4)")
        self.read_minutes.setPlaceholderText("Enter Minutes (eg. 30)")
        self.AP_selection.addItems(['AM', 'PM'])
        self.read_duration.setPlaceholderText("Enter Duration of Task (eg. 2 Hours)")

        self.HEADER.setObjectName("HEADER")
        self.read_task.setObjectName("read_task")
        self.read_time.setObjectName("read_time")
        self.read_duration.setObjectName("read_duration")
        self.instruction.setObjectName("instruction")
        self.submit_button.setObjectName("submit_button")
        self.routine_button.setObjectName("routine_button")
        self.read_minutes.setObjectName("read_minutes")
        self.AP_selection.setObjectName("AP_selection")

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
                           
            QLineEdit#read_minutes {
                padding: 15px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                margin-top: 10px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QComboBox#AP_selection {
                padding: 15px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                margin-top: 10px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QComboBox#AP_selection::drop-down {
                           border: 15px;
                           }

            QComboBox#AP_selection  QAbstractItemView {
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
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.read_time)
        hbox.addWidget(self.read_minutes)
        hbox.addWidget(self.AP_selection)

        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction, alignment= Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.read_task)
        vbox.addLayout(hbox)
        vbox.addWidget(self.read_duration)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.routine_button)
        self.setLayout(vbox)

        self.submit_button.clicked.connect(self.get_tasks)
        self.routine_button.clicked.connect(self.show_ResultWindow)

    def get_tasks(self):
        task = self.read_task.text()
        time = self.read_time.text()
        minutes = self.read_minutes.text()
        AP = self.AP_selection.currentText()
        duration = self.read_duration.text()

        if task != "" and time != "" and duration != "":
            self.daily_tasks.append({"task" : task, "time" : time, "minutes" : minutes, "AP" : AP, "duration" : duration})
            self.read_task.clear()
            self.read_time.clear()
            self.read_minutes.clear()
            self.read_duration.clear()
        else:
            self.instruction.setText("Error : Enter all the fields before submitting")

    def show_ResultWindow(self):
        if self.result_window is None:
            self.result_window = ResultWindow(self.daily_tasks)
        else:
            self.result_window(self.daily_tasks)
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

        self.make_table()
        
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
            }

            QTableWidget#routine_table::item {
                padding: 10px;
                color: #EBD5AB;
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

    def make_table(self):
        self.table.setRowCount(len(self.tasks))
        
        for index, task in enumerate(self.tasks):
            self.table.setItem(index, 0, QTableWidgetItem(task["task"]))
            self.table.setItem(index, 1, QTableWidgetItem(f"{task['time']} : {task['minutes']} {task['AP']}"))
            self.table.setItem(index, 2, QTableWidgetItem(task["duration"]))

            self.table.setRowHeight(index, 50)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()