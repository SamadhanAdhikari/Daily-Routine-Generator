from PyQt6.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QMessageBox
from PyQt6.QtCore import Qt
from Daily_Routine_Generator_Routine_Output import Daily_Routine_Timetable_Output

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

        self.Apply_CSS()

    def Apply_CSS(self):
        try:
            with open("style.css", "r", encoding="utf-8") as file:
                css_content = file.read()
                self.setStyleSheet(css_content)
        except FileNotFoundError:
            self.instruction.setText("⚠ Style file not found - using defaults")
        except Exception as e:
            self.instruction.setText(f"✗ Error loading stylesheet: {e}")

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
        self.result_window = Daily_Routine_Timetable_Output(self.daily_tasks)
        self.result_window.show()