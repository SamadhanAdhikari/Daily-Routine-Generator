import sys
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.daily_tasks = []
        self.read_task = QLineEdit(self)
        self.read_time = QLineEdit(self)
        self.read_duration = QLineEdit(self)
        self.HEADER = QLabel("DAILY ROUTINE GENERATOR", self)
        self.submit_button = QPushButton("Submit", self)
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
        self.submit_button.setObjectName("submit_button")

        self.setStyleSheet("""
            MainWindow {
                    background-color: #222831;
                           }

            QLabel#HEADER {
                           font-size: 50px;
                           font-family: Bold Font;
                           font-weight: Bold;
                           background-color: #393E46;
                           padding: 30px;
                           border-radius: 20px;
                           margin-bottom: 100px;
                           color: #EBD5AB;
                           }

            QLineEdit#read_task {
                           padding: 25px;
                           border-radius: 15px;
                           font-size: 25px;
                           margin-bottom: 15px;
                           color: #00ADB5;
                           }

            QLineEdit#read_time {
                           padding: 25px;
                           border-radius: 15px;
                           font-size: 25px;
                           margin-bottom: 15px;
                           color: #00ADB5;
                           }

            QLineEdit#read_duration {
                           padding: 25px;
                           border-radius: 15px;
                           font-size: 25px;
                           margin-bottom: 25px;
                           color: #00ADB5;
                           }

            QPushButton#submit_button {
                           padding: 25px;
                           background-color: whitesmoke;
                           border-radius: 25px;
                           font-size: 40px;
                           font-family: Times New Roman;
                           }
        """)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.HEADER, alignment = Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.read_task)
        vbox.addWidget(self.read_time)
        vbox.addWidget(self.read_duration)
        vbox.addWidget(self.submit_button)
        self.setLayout(vbox)

        self.submit_button.clicked.connect(self.get_tasks)

    def get_tasks(self):

        task = self.read_task.text()
        time = self.read_time.text()
        duration = self.read_duration.text()

        if self.read_task.text() != "" and self.read_time.text() != "" and self.read_duration.text() != "":
            self.daily_tasks.append({task, time, duration})
        print(self.daily_tasks)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()