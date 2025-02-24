import sys
import csv
import mysql.connector
import speech_recognition as sr
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QInputDialog,
    QMessageBox, QCalendarWidget, QListWidgetItem
)
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QColor
from plyer import notification
from datetime import date

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost", user="root", password="kunal", database="todo_db"
)
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task_name VARCHAR(255),
        status VARCHAR(25) DEFAULT 'pending',
        priority ENUM('High', 'Medium', 'Low') DEFAULT 'Medium',
        due_date DATE
    )
""")

# Default Dark Mode Style
dark_style = """
    QWidget { background-color: #282C34; color: white; font-size: 16px; }
    QPushButton { background-color: #61AFEF; color: white; border-radius: 5px; padding: 8px; }
    QPushButton:hover { background-color: #528BDF; }
    QListWidget { background-color: #1E2127; border: 1px solid #61AFEF; }
"""

# Light Mode Style
light_style = """
    QWidget { background-color: #FFFFFF; color: black; font-size: 16px; }
    QPushButton { background-color: #007BFF; color: white; border-radius: 5px; padding: 8px; }
    QPushButton:hover { background-color: #0056b3; }
    QListWidget { background-color: #F5F5F5; border: 1px solid #007BFF; color: black; }
"""

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 550)
        self.setStyleSheet(dark_style)

        self.layout = QVBoxLayout()
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Buttons
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.complete_button = QPushButton("Mark Complete")
        self.complete_button.clicked.connect(self.mark_complete)
        self.layout.addWidget(self.complete_button)

        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.export_button = QPushButton("Export to CSV")
        self.export_button.clicked.connect(self.export_tasks)
        self.layout.addWidget(self.export_button)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.load_tasks)
        self.layout.addWidget(self.refresh_button)

        self.dark_mode_button = QPushButton("Toggle Dark Mode")
        self.dark_mode_button.clicked.connect(self.toggle_theme)
        self.layout.addWidget(self.dark_mode_button)

        self.setLayout(self.layout)
        self.load_tasks()

    def load_tasks(self):
        self.task_list.clear()
        today = date.today()  # Convert today into a datetime.date object

        cursor.execute("SELECT id, task_name, priority, due_date FROM tasks WHERE status='pending' ORDER BY FIELD(priority, 'High', 'Medium', 'Low')")
        for task in cursor.fetchall():
            item_text = f"{task[0]}. {task[1]} (Priority: {task[2]})"
            due_date = task[3]  # due_date is a datetime.date object

            if due_date:  # If due date exists
                item_text += f" | Due: {due_date.strftime('%Y-%m-%d')}"  # Format for display

                if due_date < today:  # Overdue tasks
                    item = QListWidgetItem(item_text)
                    item.setForeground(QColor("red"))  # Highlight overdue tasks
                    self.task_list.addItem(item)
                    continue  # Skip normal item addition if it's overdue

            self.task_list.addItem(QListWidgetItem(item_text))

    def add_task(self):
        option, ok = QInputDialog.getItem(self, "Add Task", "Choose input method:", ["Type", "Voice"], 0, False)
        if not ok:
            return

        if option == "Type":
            task_name, ok = QInputDialog.getText(self, "New Task", "Enter task name:")
        else:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                QMessageBox.information(self, "Voice Input", "Listening...")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    task_name = recognizer.recognize_google(audio)
                except sr.UnknownValueError:
                    QMessageBox.warning(self, "Error", "Could not understand speech.")
                    return
                except sr.RequestError:
                    QMessageBox.warning(self, "Error", "Speech Recognition service unavailable.")
                    return

        if not ok or not task_name:
            return

        # Ask for priority
        priority, ok = QInputDialog.getItem(self, "Set Priority", "Select task priority:", ["High", "Medium", "Low"], 1, False)
        if not ok:
            return

        # Ask for due date
        due_date = None
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        date_dialog = QMessageBox(self)
        date_dialog.setWindowTitle("Select Due Date")
        date_dialog.layout().addWidget(calendar)
        date_dialog.setFixedSize(300, 350)

        if date_dialog.exec() == QMessageBox.StandardButton.Ok:
            due_date = calendar.selectedDate().toString("yyyy-MM-dd")

        # Insert into database
        cursor.execute("INSERT INTO tasks (task_name, priority, due_date) VALUES (%s, %s, %s)", (task_name, priority, due_date))
        db.commit()
        self.load_tasks()

    def mark_complete(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_id = selected_item.text().split(".")[0]
            cursor.execute("UPDATE tasks SET status='completed' WHERE id=%s", (task_id,))
            db.commit()
            self.load_tasks()
            notification.notify(title="Task Completed 🎉", message=f"Task {task_id} marked as completed!", timeout=5)
        else:
            QMessageBox.warning(self, "Warning", "Select a task to mark complete.")

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_id = selected_item.text().split(".")[0]
            reply = QMessageBox.question(self, "Delete Task", "Are you sure you want to delete this task?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
                db.commit()
                self.load_tasks()

    def export_tasks(self):
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Task Name", "Status", "Priority", "Due Date"])
            writer.writerows(tasks)
        QMessageBox.information(self, "Export Successful", "Tasks exported to tasks.csv")

    def toggle_theme(self):
        if self.styleSheet() == dark_style:
            self.setStyleSheet(light_style)
        else:
            self.setStyleSheet(dark_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())
