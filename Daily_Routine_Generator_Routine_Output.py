from PyQt6.QtWidgets import QWidget, QTableWidget, QLabel, QVBoxLayout, QTableWidgetItem
from PyQt6.QtCore import Qt

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
            print(self.tasks)