import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton,
    QDateTimeEdit, QLabel, QSlider, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QDateTime, QTime

DB_FILE = "todo.db"
# TodoTaskクラス: 変更なし
class TodoTask:
    def __init__(self, id=None, title="", description="", deadline=None, estimated_time=0, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.estimated_time = estimated_time
        self.completed = completed

# TodoAppクラス: データベース対応
class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('todo_app.ui', self)
        except Exception as e:
            QMessageBox.critical(self, "UIファイルエラー", f"UIファイルの読み込みに失敗しました: {e}\n'todo_app.ui' が存在するか、パスが正しいか確認してください。")
            sys.exit(1)

        self.setWindowTitle("TODOリストアプリ")

        self.task_input = self.findChild(QLineEdit, 'task_input')
        self.add_button = self.findChild(QPushButton, 'add_button')
        self.task_deadline = self.findChild(QDateTimeEdit, 'task_deadline')
        self.task_estimated_time_slider = self.findChild(QSlider, 'task_estimated_time')
        self.task_estimated_time_disp = self.findChild(QLabel, 'task_estimated_time_disp')
        self.todo_list_widget = self.findChild(QTableWidget, 'todo_list_widget')
        self.sort_by_deadline_button = self.findChild(QPushButton, 'sort_by_deadline_button')
        self.sort_by_estimated_time_button = self.findChild(QPushButton, 'sort_by_estimated_time_button')
        self.sort_by_priority_button = self.findChild(QPushButton, 'sort_by_priority_button')

        self.init_db()
        self.tasks = self.load_tasks()

        # --- 初期設定メソッドの呼び出し (変更なし) ---
        self.setup_table_widget()
        self.setup_estimated_time_slider()

        now = QDateTime.currentDateTime()
        self.task_deadline.setDateTime(self.set_time(now))

        # --- シグナルとスロットの接続 (変更なし) ---
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.sort_by_deadline_button.clicked.connect(self.sort_tasks_by_deadline)
        self.sort_by_estimated_time_button.clicked.connect(self.sort_tasks_by_estimated_time)
        if self.sort_by_priority_button:
            self.sort_by_priority_button.clicked.connect(self.sort_tasks_by_priority)

        self.update_table_display()

    def init_db(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                deadline TEXT,
                estimated_time INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def load_tasks(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, deadline, estimated_time FROM tasks")

        tasks_from_db = []
        for row in cursor.fetchall():
            # QDateTime.fromStringでテキストから日時に変換
            deadline_dt = QDateTime.fromString(row[2], Qt.ISODate)
            task = TodoTask(
                id=row[0],
                title=row[1],
                deadline=deadline_dt,
                estimated_time=row[3]
            )
            tasks_from_db.append(task)

        conn.close()
        return tasks_from_db

    def add_task(self):
        task_text = self.task_input.text().strip()
        if not task_text:
            QMessageBox.warning(self, "入力エラー", "タスクを入力してください。")
            return

        deadline_dt = self.task_deadline.dateTime()
        estimated_time = self.task_estimated_time_slider.value()


        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        deadline_str = deadline_dt.toString(Qt.ISODate)
        cursor.execute(
            "INSERT INTO tasks (title, deadline, estimated_time) VALUES (?, ?, ?)",
            (task_text, deadline_str, estimated_time)
        )
        new_id = cursor.lastrowid # 自動採番されたIDを取得
        conn.commit()
        conn.close()

        new_task = TodoTask(
            id=new_id,
            title=task_text,
            deadline=deadline_dt,
            estimated_time=estimated_time
        )
        self.tasks.append(new_task)

        self.update_table_display()
        self.task_input.clear()
        self.task_input.setFocus()

    def mark_task_completed_and_remove(self, task_to_remove):
        reply = QMessageBox.question(self, 'タスク完了', f'「{task_to_remove.title}」を完了として削除しますか？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_to_remove.id,))
            conn.commit()
            conn.close()

            self.tasks.remove(task_to_remove)
            self.update_table_display()


    def setup_table_widget(self):
        self.todo_list_widget.verticalHeader().setVisible(False)
        self.todo_list_widget.setColumnCount(5)
        self.todo_list_widget.setHorizontalHeaderLabels(["タスク", "期限", "見込み時間", "優先度", "アクション"])
        self.todo_list_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.todo_list_widget.horizontalHeader().setStretchLastSection(False)
        self.todo_list_widget.setColumnWidth(0, 355)
        self.todo_list_widget.setColumnWidth(1, 130)
        self.todo_list_widget.setColumnWidth(2, 80)
        self.todo_list_widget.setColumnWidth(3, 60)
        self.todo_list_widget.setColumnWidth(4, 74)
        self.todo_list_widget.setEditTriggers(QTableWidget.NoEditTriggers)

    def setup_estimated_time_slider(self):
        self.task_estimated_time_slider.setMinimum(1)
        self.task_estimated_time_slider.setMaximum(10)
        self.task_estimated_time_slider.valueChanged.connect(self.update_estimated_time_label)
        self.update_estimated_time_label(self.task_estimated_time_slider.value())

    def update_estimated_time_label(self, value):
        self.task_estimated_time_disp.setText(str(value))

    def sort_tasks_by_deadline(self):
        self.tasks.sort(key=lambda task: task.deadline)
        self.update_table_display()

    def sort_tasks_by_estimated_time(self):
        self.tasks.sort(key=lambda task: task.estimated_time, reverse=True)
        self.update_table_display()
    
    def sort_tasks_by_priority(self):
        self.tasks.sort(key=lambda task: self.calculate_priority(task), reverse=True)
        self.update_table_display()

    def calculate_priority(self, task):
        WEIGHT_URGENCY = 0.6
        WEIGHT_ESTIMATED_TIME = 0.4
        now = QDateTime.currentDateTime()
        remaining_secs = now.secsTo(task.deadline)
        if remaining_secs <= 0:
            urgency_score = 100.0
        else:
            remaining_days = remaining_secs / 86400.0
            urgency_score = 1.0 / (remaining_days + 0.1)
        estimated_time_score = task.estimated_time
        priority_score = (WEIGHT_URGENCY * urgency_score) + (WEIGHT_ESTIMATED_TIME * estimated_time_score)
        return priority_score

    def update_table_display(self):
        self.todo_list_widget.setRowCount(0)
        if not self.tasks:
            return
        scores = [self.calculate_priority(task) for task in self.tasks]
        min_score = min(scores)
        max_score = max(scores)
        score_range = max_score - min_score
        for i, task in enumerate(self.tasks):
            row_position = self.todo_list_widget.rowCount()
            self.todo_list_widget.insertRow(row_position)
            self.todo_list_widget.setItem(row_position, 0, QTableWidgetItem(task.title))
            self.todo_list_widget.setItem(row_position, 1, QTableWidgetItem(task.deadline.toString("yyyy/MM/dd HH:mm")))
            self.todo_list_widget.setItem(row_position, 2, QTableWidgetItem(str(task.estimated_time)))
            current_score = scores[i]
            if score_range == 0:
                level = 3
            else:
                normalized_score = (current_score - min_score) / score_range
                level = round(1 + normalized_score * 4)
            level_item = QTableWidgetItem(str(level))
            level_item.setTextAlignment(Qt.AlignCenter)
            self.todo_list_widget.setItem(row_position, 3, level_item)
            complete_button = QPushButton("完了")
            complete_button.clicked.connect(lambda _, t=task: self.mark_task_completed_and_remove(t))
            self.todo_list_widget.setCellWidget(row_position, 4, complete_button)

    @staticmethod
    def set_time(now):
        minute = now.time().minute()
        rounded_datetime = QDateTime(now.date(), QTime(now.time().hour(), 0, 0))
        if minute <= 30:
            rounded_datetime = rounded_datetime.addSecs(30 * 60)
        else:
            rounded_datetime = rounded_datetime.addSecs(60 * 60)
        return rounded_datetime

# アプリケーションのエントリポイント
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())