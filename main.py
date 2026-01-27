import sys
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem, QComboBox, QMessageBox
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.daily_tasks = []
        self.HEADER = QLabel("DAILY ROUTINE GENERATOR", self)
        self.instruction = QLabel("Enter Your routine", self)
        self.start_time_label = QLabel("Start Time:", self)
        self.end_time_label = QLabel("End Time:", self)
        self.read_task = QLineEdit(self)
        self.read_time = QLineEdit(self)
        self.read_minutes = QLineEdit(self)
        self.AP_selection = QComboBox()
        self.read_time2 = QLineEdit(self)
        self.read_minutes2 = QLineEdit(self)
        self.AP_selection2 = QComboBox()
        self.submit_button = QPushButton("Submit Tasks:", self)
        self.routine_button = QPushButton("Get Routine", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Routine Generator")
        self.move(300, 10)
        self.read_task.setPlaceholderText("Enter Task (eg. Do ______________ task)")
        self.read_time.setPlaceholderText("Enter Hour (eg. 4)")
        self.read_minutes.setPlaceholderText("Enter Minutes (eg. 30)")
        self.AP_selection.addItems(['AM', 'PM'])
        self.read_time2.setPlaceholderText("Enter Hour (eg. 4)")
        self.read_minutes2.setPlaceholderText("Enter Minutes (eg. 30)")
        self.AP_selection2.addItems(['AM', 'PM'])

        self.HEADER.setObjectName("HEADER")
        self.read_task.setObjectName("read_task")
        self.read_time.setObjectName("read_time")
        self.instruction.setObjectName("instruction")
        self.start_time_label.setObjectName("start_time_label")
        self.end_time_label.setObjectName("end_time_label")
        self.submit_button.setObjectName("submit_button")
        self.routine_button.setObjectName("routine_button")
        self.read_minutes.setObjectName("read_minutes")
        self.AP_selection.setObjectName("AP_selection")
        self.read_time2.setObjectName("read_time2")
        self.read_minutes2.setObjectName("read_minutes2")
        self.AP_selection2.setObjectName("AP_selection2")

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
                           
            QLabel#start_time_label {
                           font-size: 20px;
                           color: #EBD5AB;
                           }

            QLabel#end_time_label {
                           font-size: 20px;
                           color: #EBD5AB;
                           }

            QLineEdit#read_task {
                padding: 10px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 15px;
                background-color: #00ADB5;
                color: #222831;
            }

            QLineEdit#read_time {
                padding: 10px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 15px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QLineEdit#read_minutes {
                padding: 10px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                margin-top: 10px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QComboBox#AP_selection {
                padding: 10px;
                padding-right: 40px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                margin-top: 10px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QComboBox#AP_selection::drop-down {
                           border: none;
                           width: 30px;
                           }

            QComboBox#AP_selection::down-arrow {
                           image: none;
                           border: none;
                           border-left: 5px solid;
                           border-right: 5px solid;
                           border-top: 8px solid #222831;
                           }

            QComboBox#AP_selection  QAbstractItemView {
                           background-color: #00ADB5;
                           color: #222831;
                           }

            QLineEdit#read_time2 {
                padding: 10px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 15px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QLineEdit#read_minutes2 {
                padding: 10px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                margin-top: 10px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QComboBox#AP_selection2 {
                padding: 10px;
                padding-right: 40px;
                border-radius: 15px;
                font-size: 25px;
                margin-bottom: 25px;
                margin-top: 10px;
                background-color: #00ADB5;
                color: #222831;
            }
                           
            QComboBox#AP_selection2::drop-down {
                           border: none;
                           width: 30px;
                           }

            QComboBox#AP_selection2::down-arrow {
                           image: none;
                           border: none;
                           border-left: 5px solid;
                           border-right: 5px solid;
                           border-top: 8px solid #222831;
                           }

            QComboBox#AP_selection2  QAbstractItemView {
                           background-color: #00ADB5;
                           color: #222831;
                           }


            QPushButton#submit_button {
                padding: 10px;
                background-color: whitesmoke;
                color: #00ADB5;
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
                padding: 15px;
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
        
        input_start_time_horizontal = QHBoxLayout()
        input_start_time_horizontal.addWidget(self.read_time)
        input_start_time_horizontal.addWidget(self.read_minutes)
        input_start_time_horizontal.addWidget(self.AP_selection)

        input_end_time_horizontal = QHBoxLayout()
        input_end_time_horizontal.addWidget(self.read_time2)
        input_end_time_horizontal.addWidget(self.read_minutes2)
        input_end_time_horizontal.addWidget(self.AP_selection2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction, alignment= Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.read_task)
        vbox.addWidget(self.start_time_label)
        vbox.addLayout(input_start_time_horizontal)
        vbox.addWidget(self.end_time_label)
        vbox.addLayout(input_end_time_horizontal)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.routine_button)
        self.setLayout(vbox)

        self.submit_button.clicked.connect(self.get_tasks)
        self.routine_button.clicked.connect(self.show_ResultWindow)

    def Confirmation(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Confirmation")
        msg.setText(f"Are you sure you want to sumbit:\nTask: {self.read_task.text()}\nTime: {self.read_time.text()}:{self.read_minutes.text()} {self.AP_selection.currentText()}\nEnd Time: {self.read_time2.text()}:{self.read_minutes2.text()} {self.AP_selection2.currentText()}")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return msg.exec()
    
    def Input_Validation(self):

        def convert_to_minutes(hour, minutes, ap):
            h = hour
            if ap == 'PM' and h != 12:
                h += 12
            elif ap == 'AM' and h == 12:
                h = 0
            return h * 60 + minutes

        if not (self.read_task.text() and self.read_time.text() and self.read_minutes.text() and self.read_time2.text() and self.read_minutes2.text()):
            self.instruction.setText("Error: Enter all the fields before submitting")
            return None
        
        try:
            hour = int(self.read_time.text())
            minutes = int(self.read_minutes.text())
            hour2 = int(self.read_time2.text())
            minutes2 = int(self.read_minutes2.text())
        except ValueError:
            self.instruction.setText("Error: Time and minute must be numeric values")
            return None

        if hour < 1 or hour2 < 1:
            self.instruction.setText("Time error: Hour cannot be negative or zero")
            return None
        if hour > 12 or hour2 > 12:
            self.instruction.setText("Time error: Hour must be 12 or less (use 12-hour format)")
            return None
        if minutes < 0 or minutes > 59 or minutes2 < 0 or minutes2 > 59:
            self.instruction.setText("Time error: Minutes must be between 0 and 59")
            return None
        
        new_start = convert_to_minutes(hour, minutes, self.AP_selection.currentText())
        new_end = convert_to_minutes(hour2, minutes2, self.AP_selection2.currentText())
        
        if new_end <= new_start:
            self.instruction.setText("Time error: End time must be after start time")
            return None
        
        for dictionary in self.daily_tasks:
            if self.read_task.text().lower() == str(dictionary['task']).lower():
                self.instruction.setText(f'DuplicateTask: This task: "{dictionary['task']}" has been submitted already.')
                return None
            
            existing_start = convert_to_minutes(dictionary['time'], dictionary['minutes'], dictionary['AP'])
            existing_end = convert_to_minutes(dictionary['end_time'], dictionary['end_minutes'], dictionary['end_AP'])
        
            if (new_start < existing_end and new_end > existing_start):
                self.instruction.setText(f'Time overlap: This task overlaps with "{dictionary['task']}"')
                return None
        
        self.instruction.setText("Enter Your routine")
        return "Valid"
            
    def get_tasks(self):
        Validity = self.Input_Validation()
        if Validity == "Valid":
            choice = self.Confirmation()
            if choice == QMessageBox.StandardButton.Yes:
                self.daily_tasks.append({"task" : self.read_task.text(),
                                        "time" : int(self.read_time.text()),
                                        "minutes" : int(self.read_minutes.text()),
                                        "AP" : self.AP_selection.currentText(),
                                        "end_time" : int(self.read_time2.text()),
                                        "end_minutes" : int(self.read_minutes2.text()),
                                        "end_AP" : self.AP_selection2.currentText()})
                self.read_task.clear()
                self.read_time.clear()
                self.read_minutes.clear()
                self.read_time2.clear()
                self.read_minutes2.clear()

    def show_ResultWindow(self):
        self.result_window = ResultWindow(self.daily_tasks)
        self.result_window.show()

class ResultWindow(QWidget):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks
        self.HEADER = QLabel("DAILY ROUTINE", self)
        self.table = QTableWidget()
        self.instruction = QLabel("Double click on boxes to edit routine.", self)
        self.instruction2 = QLabel("(The changes made are not permanent and will be reverted after the window is closed.)", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Routine")
        self.setGeometry(300, 30, 800, 600)

        self.HEADER.setObjectName("HEADER")
        self.table.setObjectName("routine_table")
        self.instruction.setObjectName("instruction")
        self.instruction2.setObjectName("instruction2")

        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.instruction2, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.table)
        self.setLayout(vbox)
        
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(["Task", "Time", "Deadline"])

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

            QLabel#instruction {
                color: #EBD5AB;
                font-family: Calibri;
                font-size: 20px;
            }
                           
            QLabel#instruction2 {
                color: #EBD5AB;
                font-family: Calibri;
                font-size: 20px;
            }
        """)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())